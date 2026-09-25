"""One run of a strategy folder: the battery, the registry lines, the notebook, the board.

    python -m lab.report --check strategies/<folder>      # the card, before it is locked
    python -m lab.report --try strategies/<folder>        # the strategy's targets, before the run
    python -m lab.report strategies/<folder>              # the run
    python -m lab.report --notebook strategies/<folder>   # the notebook again, after a failure

The folder, in the lab's `strategies/`, is named after the card's id and holds `card.yaml`,
committed alone before any code, and `strategy.py`, whose function `positions(market, **parameters)`
returns target weights. The run refuses:
- a card that fails its own checks (`--check` runs them), whose id is not its folder's name or is
  already in the registry, and a card already run: its holdout is opened once;
- any run while the registry is not whole, since gate 4 would count too few trials: while it lacks
  a line that a commit in the branch's history held, or the lines of a run this clone began;
- a card that was not committed alone, that changed since, or any file of its folder committed
  with it or before it, under its name or any name it was moved from (a copy is a new file);
- anything uncommitted, hidden from git, ignored by git or linked from elsewhere in the folder, and
  anything uncommitted or ignored in the lab's code (but Python's compiled files of this
  interpreter, each matching its source), templates, data manifest and pins, since the registry
  names the commit that ran; and registry lines not yet committed;
- libraries whose versions differ from `requirements.txt`, which the numbers depend on;
- a strategy that imports the lab: it reads the market it is given, nothing else. As a tripwire,
  not a sandbox, the run also compares the lab's code and constants before and after the strategy
  is imported and run, and refuses a strategy that changed them; changed during the run, after the
  battery has seen the holdout, the run is void, and its lines say so.
The strategy is compiled from its source: no compiled file of it is read. Once its checks pass, the
run records its card in the clone's record, then runs gates 1 to 7, appends the registry, executes
the report notebook into the folder with its outputs, and regenerates the status board. The
verdict itself, with what was learned, is written by hand in `verdict.md`, from the notebook.
"""
from __future__ import annotations

import argparse
import ast
import atexit
import copy
import errno
import hashlib
import importlib.metadata
import importlib.util
import json
import marshal
import os
import pickle
import platform
import shutil
import signal
import subprocess
import sys
import time
import types
from dataclasses import asdict
from datetime import date
from pathlib import Path, PurePosixPath

import numpy as np
import yaml

from lab import battery, costs, data, engine, registry, stats, status, universe
from lab.notebook import execute

LAB = Path(__file__).resolve().parent.parent
TEMPLATE = LAB / "templates" / "report.ipynb"
REQUIREMENTS = LAB / "requirements.txt"
EVIDENCE = ".run.pkl"          # handed to the notebook, then deleted: the notebook keeps its outputs
GATE_MARK = {True: "pass", False: "FAIL", None: "----"}
DEPENDS = ("lab", "templates", "data/manifest.json", "requirements.txt")   # what a run reads besides its folder
WATCHED = (battery, stats, engine, costs, registry, status, data, universe)   # and this module


class Recorded(RuntimeError):
    """The card has run, and something failed after the battery: its notebook, the board, the
    registry's write, or the lab changed as the strategy ran. `verdict` is the one to show, or None
    when the run has no verdict that stands."""

    def __init__(self, verdict: battery.Verdict | None, message: str):
        super().__init__(message)
        self.verdict = verdict


def git(*args, cwd: Path) -> str:
    done = subprocess.run(["git", "-c", "core.quotePath=false", *args], cwd=cwd, capture_output=True, text=True)
    if done.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {done.stderr.strip()}")
    return done.stdout.strip()


def card_hash_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_card(folder: Path, tickers=None) -> tuple[dict, battery.Card]:
    """The card of `folder`, refused when it breaks a rule a run could not repair afterwards."""
    path = folder / "card.yaml"
    if not path.exists():
        raise RuntimeError(f"{path}: no card")
    try:
        spec = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as error:
        raise RuntimeError(f"{path}: not YAML ({' '.join(str(error).split())})") from error
    if not isinstance(spec, dict):
        raise RuntimeError(f"{path}: a card is a mapping of fields, as in templates/card.yaml")
    missing = [f for f in ("id", "theory", "universe", "variants") if not spec.get(f)]
    if missing:
        raise RuntimeError(f"{path}: the card has no {', '.join(missing)}")
    if spec["id"] != folder.name:
        raise RuntimeError(f"{path}: the card's id, {spec['id']!r}, is not its folder's name, {folder.name!r}")
    if folder.parent.name != "strategies":
        raise RuntimeError(f"{path}: a strategy's folder lies in strategies/")
    try:
        json.dumps([spec["variants"], spec.get("neighbours")])
    except TypeError as error:
        raise RuntimeError(f"{path}: parameters are numbers, text or lists of them ({error})") from error
    neighbours, splits = spec.get("neighbours") or {}, spec.get("splits") or {}
    form = {"universe": isinstance(spec["universe"], list) and all(isinstance(t, str) for t in spec["universe"]),
            "variants": isinstance(spec["variants"], list) and all(isinstance(v, dict) for v in spec["variants"]),
            "neighbours": isinstance(neighbours, dict) and all(isinstance(steps, dict) and all(
                isinstance(v, list) and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in v)
                for v in steps.values()) for steps in neighbours.values()),
            "splits": isinstance(splits, dict) and all(isinstance(v, list) and len(v) == 2 and all(
                isinstance(d, date) for d in v) for v in splits.values())}
    wrong = [name for name, kept in form.items() if not kept]
    if wrong:
        raise RuntimeError(f"{path}: {', '.join(wrong)} not in the template's form (templates/card.yaml)")
    base = spec["variants"][0]
    textual = [p for p in neighbours if isinstance(base.get(p), bool) or not isinstance(base.get(p), (int, float))]
    if textual:
        raise RuntimeError(f"{path}: neighbours move a numeric parameter of the base variant, and "
                           f"{', '.join(map(repr, textual))} is not one")
    unknown = sorted(set(spec["universe"]) - set(tickers if tickers is not None else universe.TICKERS))
    if unknown:
        raise RuntimeError(f"{path}: tickers outside the lab's universe: {', '.join(map(str, unknown))}")
    try:
        return spec, card_of(spec)
    except (TypeError, ValueError) as error:
        raise RuntimeError(f"{path}: {error}") from error


def card_of(spec: dict) -> battery.Card:
    splits = spec.get("splits") or {}
    return battery.Card(spec["id"], tuple(spec["universe"]), tuple(spec["variants"]),
                        {p: {int(k): v for k, v in steps.items()} for p, steps in (spec.get("neighbours") or {}).items()},
                        tuple(str(d) for d in splits.get("in_sample", battery.IN_SAMPLE)),
                        tuple(str(d) for d in splits.get("holdout", battery.HOLDOUT)),
                        bool(spec.get("choose", False)), spec.get("memory", battery.MIN_SHIFT))


def locked(path: Path) -> str:
    """The commit that locked the card: the card committed alone, unchanged since, and every other
    file of the folder committed only after it, under its name or any name it had before."""
    folder = path.parent
    full = git("ls-files", "--full-name", path.name, cwd=folder)
    if not full:
        raise RuntimeError(f"{path}: the card is not committed; commit it alone before any code")
    if git("status", "--porcelain", "--", path.name, cwd=folder):
        raise RuntimeError(f"{path}: the card differs from its commit")
    commits = git("log", "--format=%H", "--", path.name, cwd=folder).split()
    if len(commits) != 1:
        raise RuntimeError(f"{path}: the card changed after the commit that locked it; a changed "
                           f"hypothesis is a new card")
    lock = commits[0]
    if git("show", "--name-only", "--format=", lock, cwd=folder).split() != [full]:
        raise RuntimeError(f"{path}: the commit that locked the card holds other files; the card is committed alone")
    for name in git("ls-files", "--full-name", cwd=folder).splitlines():
        if name == full:
            continue
        first = arrival(name, folder)
        after = subprocess.run(["git", "merge-base", "--is-ancestor", lock, first], cwd=folder).returncode == 0
        if first == lock or not after:
            raise RuntimeError(f"{path}: {name.rsplit('/', 1)[-1]} was committed before the card, or with it; the card "
                               f"comes first")
    return lock


def arrival(name: str, cwd: Path) -> str:
    """The commit that brought a file into the repository: the one that added it, or, when that
    commit moved it from another path, the one that brought it there. A copy is not followed: its
    source stays where it was, with its own card."""
    start = "HEAD"
    while True:
        commit = git("log", "--diff-filter=A", "--format=%H", start, "--", f":/{name}", cwd=cwd).split()[-1]
        moves = [row.split("\t") for row in git("show", "-M", "--name-status", "--format=", commit, cwd=cwd).splitlines()]
        source = next((row[1] for row in moves if row[0].startswith("R") and row[-1] == name), None)
        if source is None:
            return commit
        name, start = source, f"{commit}^"


def committed_code(folder: Path, lab: Path, registry_path: Path) -> str:
    """The commit the registry names, once everything a run reads is committed, and the registry's
    earlier lines with it."""
    paths = [str(folder), *(str(lab / d) for d in DEPENDS), str(registry_path)]
    hidden = [row[2:] for row in git("ls-files", "-v", "--", *paths, cwd=lab).splitlines()
              if row[:1].islower() or row[:1] == "S"]
    if hidden:
        raise RuntimeError(f"files whose changes git is told to overlook (assume-unchanged, skip-worktree): "
                           f"{', '.join(hidden)}")
    dirty = git("status", "--porcelain", "--untracked-files=all", "--", *paths, cwd=lab)   # whatever git's settings
    if dirty:
        raise RuntimeError(f"uncommitted files, which the registry could not name:\n{dirty}")
    hidden = filtered(paths, lab)
    if hidden:
        raise RuntimeError(f"files whose bytes differ from their commit, which a filter of git's settings hides: "
                           f"{', '.join(hidden)}")
    ignored = git("ls-files", "--others", "--ignored", "--exclude-standard", "--", *paths, cwd=lab).splitlines()
    named = [name for name in ignored if not kept(name)]
    if named:
        raise RuntimeError(f"files that git ignores, which the registry could not name: {', '.join(named)}")
    forged = [name for name in ignored if kept(name) and not compiled_as_source(lab / name)]
    if forged:
        raise RuntimeError(f"compiled files of the lab's code that Python would read in place of their source, and "
                           f"that hold other code: {', '.join(forged)}; they are removed as this run ends: run again")
    links = sorted(str(p.relative_to(folder)) for p in folder.rglob("*") if p.is_symlink())
    if links:
        raise RuntimeError(f"links to files elsewhere, which the registry could not name: {', '.join(links)}")
    return git("rev-parse", "HEAD", cwd=lab)


def kept(name: str) -> bool:
    """The only files git may ignore among those a run reads: Python's compiled files in a
    `__pycache__` folder of the lab's code, each checked against its source, and the temporary
    files Python writes them through (`*.pyc.<number>`), which it never reads. A strategy is compiled
    from its source, and its run's data is written after its run, which comes once: no ignored file
    of its folder is ever kept."""
    path = PurePosixPath(name)
    return path.parts[0] == "lab" and path.parent.name == "__pycache__" and \
        (path.suffix == ".pyc" or (path.suffix[1:].isdigit() and path.stem.endswith(".pyc")))


def compiled_as_source(path: Path) -> bool:
    """Whether a compiled file of the lab's code holds what its source compiles to, wherever this
    interpreter would read it in place of its source: when its header matches the source's time and
    size, or the source's hash, or asks for no check at all, the header's flags read as Python reads
    them. A file of another interpreter, one whose header Python would find stale or does not know,
    or one without its source, is never read, and passes; so does a temporary file, and a file gone
    before it is read. The runner reads its own code before any check: a file a strategy wrote is
    removed as its run ends (`uncompiled`)."""
    parts = path.name.split(".")
    source = path.parent.parent / f"{parts[0]}.py"
    try:
        body = path.read_bytes()
    except FileNotFoundError:                        # removed by another process of the lab: never read
        return True
    if parts[-1] != "pyc" or len(parts) < 3 or parts[1] != sys.implementation.cache_tag or not source.exists() \
            or body[:4] != importlib.util.MAGIC_NUMBER:
        return True
    flags = int.from_bytes(body[4:8], "little")
    if flags & ~0b11:                                # a flag Python does not know: never read
        return True
    if not flags & 0b01:                             # checked by the source's time and size
        stat = source.stat()
        if (int.from_bytes(body[8:12], "little"), int.from_bytes(body[12:16], "little")) != \
                (int(stat.st_mtime) & 0xFFFFFFFF, stat.st_size & 0xFFFFFFFF):
            return True
    elif flags & 0b10 and body[8:16] != importlib.util.source_hash(source.read_bytes()):
        return True                                  # checked by the source's hash, which differs
    optimize = int(parts[2][4:]) if len(parts) == 4 and parts[2].startswith("opt-") else 0
    try:
        return marshal.loads(body[16:]) == compile(source.read_bytes(), str(source), "exec", dont_inherit=True,
                                                   optimize=optimize)
    except Exception:
        return False


def filtered(paths: list[str], lab: Path) -> list[str]:
    """The tracked files whose bytes differ from their commit's although git sees no change: a
    filter of git's settings hides them. Links are left to the links' check. Git reads the paths it
    is handed on its input from the repository's top folder, of which the lab may be a subfolder:
    it is handed whole paths."""
    staged = [row.split(None, 3) for row in git("ls-files", "-s", "-z", "--", *paths, cwd=lab).split("\0") if row]
    files = [(blob, name) for mode, blob, _, name in staged if mode != "120000"]
    if not files:
        return []
    done = subprocess.run(["git", "hash-object", "--no-filters", "--stdin-paths"], cwd=lab, capture_output=True,
                          text=True, input="".join(str(lab / name) + "\n" for _, name in files))
    if done.returncode:
        raise RuntimeError(f"git hash-object: {done.stderr.strip()}")
    return [name for (blob, name), mine in zip(files, done.stdout.split()) if mine != blob]


def lab_imports(folder: Path) -> list[str]:
    """The folder's Python files that import the lab: a strategy reads the market it is given."""
    found = []
    for path in sorted(folder.rglob("*.py")):
        for node in ast.walk(ast.parse(path.read_text(), filename=path.name)):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0:
                names = [node.module or ""]
            else:
                continue
            found += [f"{path.relative_to(folder)} imports {n}" for n in names if n == "lab" or n.startswith("lab.")]
    return found


def versions() -> dict:
    """The libraries' versions that the numbers depend on, as installed."""
    names = [line.split("==")[0].strip() for line in REQUIREMENTS.read_text().splitlines()
             if "==" in line and not line.startswith("#")]
    return {"python": platform.python_version(), **{n: importlib.metadata.version(n) for n in names}}


def pinned_versions() -> dict:
    """The installed versions, refused when one differs from its pin in requirements.txt."""
    installed = versions()
    pins = dict(line.split("==") for line in REQUIREMENTS.read_text().split() if "==" in line)
    wrong = [f"{n} {installed[n]} (pinned {v})" for n, v in pins.items() if installed.get(n) != v]
    if wrong:
        raise RuntimeError(f"libraries other than requirements.txt pins: {', '.join(wrong)}")
    return installed


def dunder(name: str) -> bool:
    return name.startswith("__") and name.endswith("__")


def fingerprint(value):
    """What a name holds, in a form that changes when the name is rebound, a function's code or
    defaults are swapped, a class's attributes are (its methods, properties, static and class
    methods, and plain values), or a plain container's contents change."""
    if isinstance(value, types.FunctionType):
        return value, value.__code__, value.__defaults__, value.__kwdefaults__
    if isinstance(value, (staticmethod, classmethod)):
        return value, fingerprint(value.__func__)
    if isinstance(value, property):
        return value, fingerprint(value.fget), fingerprint(value.fset), fingerprint(value.fdel)
    if isinstance(value, type):
        return value, tuple((k, fingerprint(v)) for k, v in vars(value).items()
                            if not dunder(k) or isinstance(v, (types.FunctionType, staticmethod, classmethod, property)))
    if isinstance(value, (dict, list, set, tuple, frozenset)):
        try:
            return value, copy.deepcopy(value)
        except TypeError:                          # a container of modules: its members, by identity
            return (value, *value)
    return (value,)


def battery_code() -> dict:
    """Every name the run reads its code and thresholds from, as bound now: the battery, the
    statistics, the engine, the costs, the registry, the board, the data, the universe and this
    module, each with every name it holds but Python's own (`__name__` and the like). Each module's
    names are read from a copy: a warning raised as a value is copied adds Python's own registry of
    warnings to the module it names."""
    return {m.__name__: {name: fingerprint(value) for name, value in dict(vars(m)).items() if not dunder(name)}
            for m in (*WATCHED, sys.modules[__name__])}


def same(now, was) -> bool:
    try:
        return len(now) == len(was) and now[0] is was[0] and all(a is b or bool(a == b) for a, b in zip(now[1:], was[1:]))
    except Exception:                              # a comparison that cannot be made is a change
        return False


def unchanged(before: dict, same=same, fingerprint=fingerprint) -> list[str]:
    """The names whose code or contents differ from `before`, those gone, those added since, and the
    modules removed. Its helpers are bound where it is defined: rebinding them blinds nothing."""
    moved = []
    for module, names in before.items():
        found = sys.modules.get(module)
        if found is None:
            moved.append(f"{module} (removed)")
            continue
        held = {name: value for name, value in dict(vars(found)).items() if not dunder(name)}
        moved += [f"{module}.{name}" for name, was in names.items()
                  if name not in held or not same(fingerprint(held[name]), was)]
        moved += [f"{module}.{name} (added)" for name in held if name not in names]
    return sorted(moved)


def strategy_of(path: Path):
    """The strategy's `positions`, compiled from its source: a compiled file beside it is never read,
    and none is written."""
    module = types.ModuleType(f"strategy_{path.parent.name.replace('-', '_')}")
    module.__file__ = str(path)
    exec(compile(path.read_text(), str(path), "exec"), module.__dict__)
    return module.positions


def seed_of(card_hash: str) -> int:
    return int(card_hash[:8], 16)


def snapshot_of(root: Path = data.DATA) -> tuple[str, str]:
    """The frozen snapshot's name, joined by its additions', and a hash of the files its manifest
    lists: the snapshot's alone while it has no addition, so that a hash already recorded holds."""
    manifest = json.loads((root / "manifest.json").read_text())
    additions = manifest.get("additions", [])
    listed = [manifest["files"], *(addition["files"] for addition in additions)] if additions else manifest["files"]
    name = "+".join([manifest["snapshot"], *(addition["snapshot"] for addition in additions)])
    return name, hashlib.sha256(json.dumps(listed, sort_keys=True).encode()).hexdigest()


def check_card(folder: Path, tickers=None, registry_path: Path = registry.REGISTRY,
               done: list[str] | None = None) -> tuple[dict, battery.Card]:
    """The card of `folder`, refused when it breaks a rule, when its folder is not in the lab's
    `strategies/`, when its id is already in the registry, or when it already ran: its holdout is
    opened once. Refused too while the registry is not whole, since gate 4 would count too few
    trials: while it lacks a line that a commit in the branch's history held, or the lines of a run
    this clone began. `done` is the registry's committed lines, when already read."""
    folder = Path(folder).resolve()
    spec, card = read_card(folder, tickers)
    if folder.parent != Path(registry_path).resolve().parent.parent / "strategies":
        raise RuntimeError(f"{folder}: a strategy's folder lies in the lab's own strategies/")
    dropped = registry.dropped(registry_path, done)
    if dropped:
        raise RuntimeError(f"the registry lacks {len(dropped)} line{'s' if len(dropped) > 1 else ''} that a commit of it "
                           f"held, and it only grows: python -m lab.registry restore puts them back; commit it, "
                           f"then run")
    lost = registry.missing(registry_path, done)
    if lost:
        raise RuntimeError(f"this clone began the run of {len(lost)} card{'s' if len(lost) > 1 else ''} whose lines the "
                           f"registry does not hold ({', '.join(h[:12] for h in lost)}): a run still going, or lines "
                           f"put aside, lost or edited, or written for its card by hand; put them back: python -m "
                           f"lab.registry restore puts back the lines this clone kept and removes those its runs did not "
                           f"write, or names those it cannot tell, and for a run that wrote none, python -m lab.registry "
                           f"void writes void lines; commit them, then run")
    first = registry.opened(card_hash_of(folder / "card.yaml"), registry_path)
    if first is not None:
        raise RuntimeError(f"{folder.name}: this card ran on {first}, and its holdout is opened once; a new card is needed")
    if any(line["card"] == card.id for line in registry.lines(registry_path)):
        raise RuntimeError(f"{folder.name}: a card with this id already ran; a new card takes a new id")
    return spec, card


def older(folder: Path, than: float) -> bool:
    """Whether `folder` holds a file last changed before `than`, or one it cannot read."""
    errors = []
    for top, _, names in os.walk(folder, onerror=errors.append):
        for name in names:
            try:
                if os.stat(os.path.join(top, name)).st_ctime < than:
                    return True
            except FileNotFoundError:                      # removed as it is read
                continue
            except OSError:
                return True
    return any(not isinstance(error, FileNotFoundError) for error in errors)


def holds(folder: Path) -> bool:
    """Whether `folder` holds any entry, a link that leads nowhere among them, or cannot be read."""
    try:
        with os.scandir(folder) as entries:
            return any(True for _ in entries)
    except FileNotFoundError:
        return False
    except OSError:
        return True


def uncompiled(lab: Path, remove=shutil.rmtree, older=older, holds=holds) -> list[str]:
    """The compiled files of the lab's code removed, in `lab` and in the lab whose code runs: one
    that a strategy wrote as it ran would be read by the next run before any check could see it, the
    runner's own among them. Python writes them again from their sources. `remove`, and the lab's
    helpers that read the folders it leaves (not the standard library's functions they call), are
    bound as the runner is imported, before any strategy. A folder it fails to remove is removed
    once more; one still there is named, and returned, when the removal was refused (a permission, a
    flag, anything but a file already gone or a folder written again as it was removed) and it holds
    anything, a link among them, or cannot be read, or when, written again, it still holds a file
    changed before the removal began, or one it cannot read. Another process of the lab, writing
    into it meanwhile, leaves only newer files, and is not named."""
    left, began = [], time.time()
    for root in dict.fromkeys([Path(lab).resolve(), LAB]):
        for cache in sorted((root / "lab").rglob("__pycache__")):
            errors = []
            remove(cache, onexc=lambda function, path, error: errors.append(error))
            if errors and cache.exists():                  # once more: another process may write as it goes
                errors = []
                remove(cache, onexc=lambda function, path, error: errors.append(error))
            refused = [error for error in errors if not isinstance(error, FileNotFoundError)
                       and getattr(error, "errno", None) != errno.ENOTEMPTY]
            if cache.exists() and ((refused and holds(cache)) or (errors and older(cache, began))):
                left.append(str(cache.relative_to(root)))
    if left:
        print(f"warning: the lab's compiled files in {', '.join(left)} could not be removed: remove them before the "
              f"next run, which would read them", file=sys.stderr)
    return left


_AT_EXIT: set = set()


def at_exit(scrub, lab: Path) -> None:
    """`scrub` of `lab` also as the interpreter exits, registered once, before any strategy is
    imported, in a function of its own that a strategy cannot reach by the module's name (it can
    through the garbage collector: this is no guarantee); exit functions run last registered first,
    so it runs after any a strategy registers, and after the threads the interpreter waits for (not
    daemon threads) have ended. It calls the `scrub` bound as the run began, not the module's."""
    if lab not in _AT_EXIT:
        _AT_EXIT.add(lab)

        def remove_at_exit():
            scrub(lab)
        atexit.register(remove_at_exit)


def run(folder: Path, market=None, snapshot: str | None = None, snapshot_hash: str | None = None,
        registry_path: Path = registry.REGISTRY, lab: Path = LAB, board: Path | None = None,
        **options) -> battery.Verdict:
    """Run the card of `folder` once. `market` and the snapshot's name and hash default to the frozen
    snapshot; `options` go to the battery (the crypto assets and the clusters of a synthetic market).
    Once every check has passed, the card is recorded in the clone's record, before the battery opens
    its holdout: from then on the card has run, whatever happens next, and what fails afterwards is
    raised as `Recorded`. One run at a time holds the record, from its checks until its lines are
    written. However the run ends, the lab's compiled files are removed (`uncompiled`, bound before
    the strategy is imported), and again as the interpreter exits."""
    scrub = uncompiled
    at_exit(scrub, lab)
    try:
        return judged(folder, market, snapshot, snapshot_hash, registry_path, lab, board, **options)
    finally:
        scrub(lab)


def judged(folder: Path, market, snapshot: str | None, snapshot_hash: str | None, registry_path: Path, lab: Path,
           board: Path | None, **options) -> battery.Verdict:
    """The run itself (`run`)."""
    folder = Path(folder).resolve()
    if market is None:
        market = data.load(root=data.DATA)
        snapshot, snapshot_hash = snapshot_of(data.DATA)
    with registry.held(registry_path):                   # one run at a time, from its checks to its lines
        done = registry.committed(registry_path)          # the registry's history, read once
        spec, card = check_card(folder, list(market.prices.columns), registry_path, done)
        card_hash = card_hash_of(folder / "card.yaml")
        locked(folder / "card.yaml")
        commit = committed_code(folder, lab, registry_path)
        installed = pinned_versions()
        reads = lab_imports(folder)
        if reads:
            raise RuntimeError(f"{'; '.join(reads)}: a strategy reads the market it is given, not the lab")
        history = registry.history(registry_path, done)
        check, void, board_of, written, before = (unchanged, registry.void, status.write, registry.written,
                                                  battery_code())            # bound before the strategy
        try:
            strategy = strategy_of(folder / "strategy.py")
        except BaseException as error:              # an exit or an interrupt as it is imported: nothing ran
            raise RuntimeError(f"the strategy stopped as it was imported ({type(error).__name__}: {error}); nothing "
                               f"was recorded") from None
        moved = check(before)
        if moved:
            raise RuntimeError(f"the strategy changed the lab as it was imported: {', '.join(moved)}; nothing was recorded")
        registry.record(card_hash, registry.now(), registry_path)
        known = {"snapshot": snapshot or "unnamed", "snapshot_hash": snapshot_hash, "commit": commit,
                 "versions": installed, "thresholds": battery.THRESHOLDS}

        def voided(reason: str, then: str, trials=None) -> Recorded:
            try:
                void(card.id, card_hash, card.variants, reason, registry_path, trials=trials, **known)
            except Exception:                           # the record holds the card; the copy may hold its lines
                kept = any(registry.entry(text)["card_hash"] == card_hash for text in written(registry_path))
                return Recorded(None, f"{reason}; the run is void, and its lines could not be written: " +
                                ("this clone kept them, and python -m lab.registry restore puts them back" if kept
                                 else "python -m lab.registry void writes them"))
            said = f"{reason}; the run is void, and its lines say so: {then}"
            try:
                board_of(lab, registry_path, board)
            except Exception as error:
                said += f"; the board could not be written ({type(error).__name__}: {error}): run python -m lab.status"
            except BaseException as error:              # a second Ctrl-C, as the board is written
                said += f"; the board was not written ({type(error).__name__}): run python -m lab.status"
            return Recorded(None, said)

        try:
            verdict = battery.run(card, strategy, market, history, seed=seed_of(card_hash), **options)
        except Exception as error:
            raise voided(f"the run stopped ({type(error).__name__}: {error})",
                         "commit them at once, alone, and fix the cause; the card has run") from error
        except BaseException as error:                  # an interrupt, or a strategy that exits: the card has run
            raise voided(f"the run was interrupted ({type(error).__name__})",
                         "commit them at once, alone; the card has run") from error
        try:
            moved = check(before)
        except Exception as error:                      # a lab that cannot be compared has changed
            moved = [f"the lab could not be compared after the battery ({type(error).__name__}: {error})"]
        if moved:
            raise voided(f"the strategy changed the lab as it ran: {', '.join(moved)}",
                         "the battery had seen the holdout; commit them at once, alone; a new card is needed",
                         verdict.trials)
        failed = []
        try:
            registry.append(verdict, card_hash, card.variants, snapshot or "unnamed", snapshot_hash, commit,
                            installed, registry_path)
        except Exception as error:
            kept_lines = any(registry.entry(text)["card_hash"] == card_hash for text in written(registry_path))
            failed.append(f"the registry could not be written ({type(error).__name__}: {error}): " +
                          ("this clone kept its lines, and once the registry can be written, python -m lab.registry "
                           "restore puts them back" if kept_lines else "once the registry can be written, python -m "
                           "lab.registry void writes its lines without returns"))
    try:
        write_notebook(folder, spec, card, verdict, snapshot, lab)
    except Exception as error:
        failed.append((f"its notebook failed: {error}" if isinstance(error, RuntimeError)
                       else f"its notebook failed ({type(error).__name__}: {error})") +
                      ("" if (folder / EVIDENCE).exists() else ": its data was not written, and its report cannot be "
                                                               "drawn"))
    except BaseException as error:                      # an interrupt the notebook's client does not handle
        failed.append(f"its notebook was interrupted ({type(error).__name__}): " +
                      (f"run python -m lab.report --notebook strategies/{folder.name}" if (folder / EVIDENCE).exists()
                       else "its data was not written, and its report cannot be drawn"))
    try:
        status.write(lab, registry_path, board)
    except Exception as error:
        failed.append(f"the board could not be written ({type(error).__name__}: {error}); fix the cause, then run "
                      f"python -m lab.status")
    except BaseException as error:                      # a second Ctrl-C, as the board is written
        failed.append(f"the board was not written ({type(error).__name__}): run python -m lab.status")
    if failed:
        raise Recorded(verdict, "the card has run, and " + "; ".join(failed))
    return verdict


def clean(text: str, lab: Path) -> str:
    """A reason without the machine's paths: the repository's and the home folder's."""
    for root, short in ((lab.parent, ""), (lab, lab.name), (Path.home(), "~")):
        text = text.replace(f"{root}/", f"{short}/" if short else "").replace(str(root), short or ".")
    return text


def write_notebook(folder: Path, spec: dict, card: battery.Card, verdict: battery.Verdict, snapshot: str,
                   lab: Path = LAB) -> Path:
    """The report template, executed in the strategy's folder and saved with its outputs. The run's
    data is written whole or not at all: an interrupt or SIGTERM this thread would take is held back
    until it is in place."""
    gates = [{**asdict(gate), "reason": clean(gate.reason, lab)} for gate in verdict.gates]
    run = {"card": spec, "snapshot": snapshot, "thresholds": verdict.thresholds, "failed": verdict.failed,
           "gates": gates, "evidence": verdict.evidence,
           "constants": {"in sample": list(card.in_sample), "holdout": list(card.holdout),
                         "placebos": battery.PLACEBOS, "percentile": battery.PERCENTILE, "window": battery.WINDOW,
                         "floors": {"Sharpe": battery.MIN_SHARPE, "Sharpe at 2x costs": battery.MIN_SHARPE_DOUBLED}}}
    part = folder / f"{EVIDENCE}.part"
    held = signal.pthread_sigmask(signal.SIG_BLOCK, [])   # the mask as it is, read
    try:
        signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGINT, signal.SIGTERM})   # written whole, or not at all
        with part.open("wb") as handle:
            pickle.dump(run, handle)                 # plain data: the notebook needs no code of the lab
        os.replace(part, folder / EVIDENCE)
    finally:
        part.unlink(missing_ok=True)
        signal.pthread_sigmask(signal.SIG_SETMASK, held)
    return execute_notebook(folder)


def execute_notebook(folder: Path) -> Path:
    """Execute the template into `folder` from the data the run left; the data is deleted once the
    notebook has run, and kept when it fails, so that the notebook can be run again."""
    evidence = folder / EVIDENCE
    if not evidence.exists():
        raise RuntimeError(f"{folder.name}: no data of a run to draw ({EVIDENCE}); a notebook is written by a run")
    notebook = folder / "report.ipynb"
    notebook.write_text(TEMPLATE.read_text())
    try:
        execute(notebook, metadata={"alpha_lab": {"template": drawn_by()}})
    except Exception as error:
        said = told(error.evalue, error.ename) if getattr(error, "ename", None) else told(str(error))
        raise RuntimeError(f"{folder.name}: the notebook failed ({type(error).__name__}{': ' + said if said else ''}); "
                           f"the run's data is kept "
                           f"in {EVIDENCE}: fix the cause, then run python -m lab.report --notebook "
                           f"strategies/{folder.name}") from error
    evidence.unlink()
    return notebook


def told(text: str, name: str = "", most: int = 200) -> str:
    """The first line of an error's message that says something, after its name, `most` characters
    at most: a cell's error, not the cell."""
    line = next((line.strip() for line in str(text).splitlines() if line.strip()), "")
    line = f"{name}: {line}" if name and line else name or line
    return line if len(line) <= most else line[:most - 3] + "..."


def drawn_by() -> str | None:
    """The last commit of the report template, which the notebook records: `--notebook` may draw a
    run's report with a template later than the run's commit."""
    try:
        return git("log", "-1", "--format=%H", "--", TEMPLATE.name, cwd=TEMPLATE.parent) or None
    except RuntimeError:
        return None


def smaller_markets(market, crypto=costs.CRYPTO, cluster=universe.cluster_of) -> list:
    """The markets gate 6 runs the base variant on, with the assets each one leaves out: one cluster
    left out at a time, when there are two clusters at least, its assets untradable and their prices
    still read (`battery.unheld`), and bitcoin left out, removed, when the universe holds it and
    something else."""
    tickers = list(market.prices.columns)
    clusters = sorted({cluster(t) for t in tickers})
    out = [[t for t in tickers if cluster(t) == c] for c in clusters] if len(clusters) > 1 else []
    given = [(battery.unheld(market, left), left) for left in out]
    if set(tickers) & set(crypto) and set(tickers) - set(crypto):
        left = sorted(set(tickers) & set(crypto))
        given.append((battery.restrict(market, [t for t in tickers if t not in left]), left))
    return given


def try_strategy(folder: Path, market=None, crypto=costs.CRYPTO, cluster=universe.cluster_of) -> dict:
    """The strategy's variants on the in-sample years only: their targets checked like a run checks
    them, with gate 1's timing checks, and no returns, so that nothing is learned about their
    performance before the run. Gate 6's runs are tried too: every neighbour, whose timing is
    checked on ten dates where it sets a target and ten where it holds, as gate 7 checks the
    holdout's, and the base variant on each smaller market. The lab's compiled files are removed as
    it ends, as after a run."""
    scrub, lab = uncompiled, Path(folder).resolve().parent.parent
    at_exit(scrub, lab)
    try:
        return tried(folder, market, crypto, cluster)
    finally:
        scrub(lab)


def tried(folder: Path, market, crypto, cluster) -> dict:
    """The trial itself (`try_strategy`)."""
    folder = Path(folder).resolve()
    market = market if market is not None else data.load()
    spec, card = read_card(folder, tickers=list(market.prices.columns))
    reads = lab_imports(folder)
    if reads:
        raise RuntimeError(f"{'; '.join(reads)}: a strategy reads the market it is given, not the lab")
    inside = battery.restrict(market, card.universe).window(*card.in_sample)
    strategy = strategy_of(folder / "strategy.py")
    variants = [battery.targets(strategy, inside, p) for p in card.variants]
    for positions in variants:
        engine.check_positions(positions, inside.prices)
    named = [(parameter, value) for parameter, steps in card.neighbours.items()
             for value in dict.fromkeys(v for values in steps.values() for v in values)]
    moved = [{**card.variants[0], parameter: value} for parameter, value in named]
    neighbours = [battery.targets(strategy, inside, p) for p in moved]     # gate 6 moves these: they must run too
    for positions in neighbours:
        engine.check_positions(positions, inside.prices)
    for given, left in smaller_markets(inside, crypto, cluster):
        kept = [t for t in given.prices.columns if t not in left]
        engine.check_positions(battery.targets(strategy, given, card.variants[0], left_out=left)[kept],
                               given.prices[kept])
    start = battery.first_holding(variants[0])
    if start is None:
        return {"holds an asset": False}
    period = slice(start, inside.prices.index[-1])
    rng = np.random.default_rng(seed_of(card_hash_of(folder / "card.yaml")))
    timing = [battery.timing_breaks(strategy, p, inside, positions, period, rng, battery.CHECKED_DATES)
              for p, positions in zip(card.variants, variants)]
    memory = [battery.memory_breaks(strategy, p, inside, positions, period, rng, battery.CHECKED_DATES, card.memory)
              for p, positions in zip(card.variants, variants)]
    near = [battery.timing_breaks(strategy, p, inside, positions, period, rng, battery.HOLDOUT_CHECKED_DATES)
            for p, positions in zip(moved, neighbours)]
    blocks = sum(1 for first, last in battery.BLOCKS
                 if (inside.prices.loc[first:last].index > start).sum() >= battery.MIN_BLOCK_SESSIONS)
    tried = {"holds an asset": True, "from": str(start.date()),
             "sessions with a target": int(variants[0].loc[period].notna().any(axis=1).sum()),
             "clustered decisions": stats.decision_clusters(variants[0].loc[period]),
             "dates checked": sum(t.checked for t in timing),
             "look-ahead breaks": sum(len(t.look_ahead) for t in timing),
             "same-day breaks": sum(len(t.same_day) for t in timing),
             "memory": card.memory, "memory dates checked": sum(m[0] for m in memory),
             "memory breaks": sum(len(m[1]) for m in memory),
             "neighbours timed": len(moved), "neighbour dates checked": sum(t.checked for t in near),
             "neighbour look-ahead breaks": sum(len(t.look_ahead) for t in near),
             "neighbour same-day breaks": sum(len(t.same_day) for t in near),
             "blocks of gate 5 after the first target": blocks,
             "neighbours that hold the base": [f"{p}={v}" for (p, v), positions in zip(named, neighbours)
                                               if battery.same_rows(positions.loc[period], variants[0].loc[period])]}
    warnings = []
    if blocks < battery.MIN_POSITIVE_BLOCKS:
        warnings.append(f"after its first target, {blocks} blocks hold {battery.MIN_BLOCK_SESSIONS} sessions or "
                        f"more, and gate 5 needs {battery.MIN_POSITIVE_BLOCKS}: it would fail whatever the edge")
    if tried["neighbours that hold the base"]:
        warnings.append(f"{', '.join(tried['neighbours that hold the base'])} set the base's targets on every "
                        f"session from its first holding, and gate 6 fails a neighbour that does not move the "
                        f"strategy: it would fail whatever the edge")
    if tried["memory breaks"]:
        warnings.append(f"the targets change when the prices older than the card's memory of {card.memory} "
                        f"sessions are scrambled: gate 1 would fail; the card declares the memory its signal reads")
    if warnings:
        tried["warning"] = "; ".join(warnings)
    return tried


def drafted(folder: Path) -> list[str]:
    """What a folder holds beside its card and its reasoning while its card is not committed as it
    stands: the build plan and the code are written after the card is locked. The lock proves the
    order of commits; this keeps the order of work, as far as the folder shows it."""
    if not git("status", "--porcelain", "--untracked-files=all", "--", "card.yaml", cwd=folder):
        return []
    return sorted(path.name for path in folder.iterdir()
                  if path.name not in ("card.yaml", "reasoning.md") and not path.name.startswith("."))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="python -m lab.report", description="Run a strategy folder through the battery.")
    parser.add_argument("folder", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check the card, before it is locked")
    mode.add_argument("--try", dest="attempt", action="store_true", help="check the strategy's targets, no returns")
    mode.add_argument("--notebook", action="store_true", help="execute the notebook again from the run's data")
    args = parser.parse_args(argv)
    folder = args.folder.resolve()
    try:
        if args.check:
            check_card(folder)
            early = drafted(folder)
            if early:
                raise RuntimeError(f"{folder.name}: {', '.join(early)} already written: the card is committed alone, "
                                   f"from a folder that holds only it and its reasoning, and the build plan and the "
                                   f"code are written after it")
            print(f"{folder.name}: the card keeps the rules; commit it alone, then write the code")
        elif args.attempt:
            for key, value in try_strategy(folder).items():
                print(f"  {key}: {value}")
        elif args.notebook:
            dirty = git("status", "--porcelain", "--", str(TEMPLATE), cwd=LAB)
            if dirty:
                raise RuntimeError(f"the report template is not committed:\n{dirty}")
            print(execute_notebook(folder))
            status.write()
        else:
            show(run(folder))
    except Recorded as done:                        # the card has run: never "refused"
        if done.verdict is not None:
            show(done.verdict)
        print(" ".join(clean(str(done), LAB).split()), file=sys.stderr)
        return 1
    except Exception as error:                      # one line, never a trace: the run refused, or could not start
        said = str(error) if isinstance(error, (RuntimeError, ValueError)) else f"{type(error).__name__}: {error}"
        print(f"refused: {' '.join(clean(said, LAB).split())}", file=sys.stderr)
        return 1
    return 0


def show(verdict: battery.Verdict) -> None:
    print(f"{verdict.card}: " + (f"stops at gate {verdict.failed}" if verdict.failed else "passes gates 1 to 7"))
    for gate in verdict.gates:
        print(f"  {gate.number} {GATE_MARK[gate.passed]} {gate.name}: {clean(gate.reason, LAB)}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
