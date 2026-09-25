"""The status board: every theory of the bank, its status, and each strategy drawn from it with the
gate it reached, with the links. Rejected strategies stay on it.

    python -m lab.status        # writes alpha-lab/STATUS.md; every run of lab.report does too
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

from lab import registry

LAB = Path(__file__).resolve().parent.parent
STATUSES = ("untouched", "in-progress", "tested-conclusive", "tested-inconclusive", "not-testable")
PUBLIC = "https://github.com/Sami-Andaloussi/alpha-factory"          # the lab's public repository
PAPER_PAGE = f"{PUBLIC}/blob/paper/paper/README.md"                  # the paper trading job's page, on its branch
ENDED = "gate-8.md"   # a strategy's gate 8 concluded, in its folder: it leaves paper trading


def front_matter(path: Path) -> dict:
    """The YAML block between the two `---` lines that open a bank file."""
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    return yaml.safe_load(text[4:text.index("\n---", 4)]) or {}


def theories(lab: Path = LAB) -> list[dict]:
    rows = []
    for path in sorted((lab / "bank").glob("*.md")):
        meta = front_matter(path)
        if meta.get("id"):
            rows.append({**meta, "file": path.relative_to(lab).as_posix()})
    return rows


def runs_by_card(registry_path: Path = registry.REGISTRY) -> dict[str, dict]:
    """The registry's runs, one per card, found by the hash of the card that ran."""
    return {line["card_hash"]: line for line in registry.lines(registry_path)}


def strategies(lab: Path = LAB, registry_path: Path = registry.REGISTRY) -> list[dict]:
    """Every strategy folder, named by the folder, with its card, and what its run, if any, reached:
    found by the card's hash, or else by the folder's name, which is the id its run was made under,
    when the card was edited after its run and no other folder holds the card that ran. A card copied
    into another folder is not that run while the folder it ran in still holds it; once that folder
    holds it no more, the folder was renamed."""
    runs = runs_by_card(registry_path)
    by_id = {line["card"]: line for line in runs.values()}
    cards = sorted((lab / "strategies").glob("*/card.yaml"))
    held = {card.parent.name: hashlib.sha256(card.read_bytes()).hexdigest() for card in cards}
    rows = []
    for card in cards:
        try:
            spec = yaml.safe_load(card.read_text())
        except yaml.YAMLError:                    # the runner refuses such a card: the board still lists it
            spec = None
        spec = spec if isinstance(spec, dict) else {}
        folder = card.parent
        run = runs.get(held[folder.name])
        if run and run["card"] != folder.name and held.get(run["card"]) == run["card_hash"]:
            run = None                            # a copy of a run card is not that run
        edited = by_id.get(folder.name)
        if run is not None or (edited and edited["card_hash"] in held.values()):
            edited = None                         # the card that ran under this name is in a folder of its own
        rows.append({"id": folder.name, "theory": spec.get("theory", ""), "folder": folder.relative_to(lab).as_posix(),
                     "run": run or edited, "changed": edited is not None,
                     "renamed": run is not None and run["card"] != folder.name,
                     "pending": (folder / ".run.pkl").exists(), "report": (folder / "report.ipynb").exists(),
                     "verdict": (folder / "verdict.md").exists()})
    return rows


def paper_trading(lab: Path = LAB) -> dict:
    """Each strategy under paper trading, as the job's branch showed it when it was last taken
    (`python -m lab.paper --take`): `paper/live.json`. One whose folder holds its gate 8's
    conclusion is traded no more, whatever the branch last said."""
    path = lab / "paper" / "live.json"
    live = json.loads(path.read_text()) if path.exists() else {}
    for strategy, shown in live.items():
        if (lab / "strategies" / strategy / ENDED).exists():
            shown["trading"] = False
    return live


def gate_8(live: dict) -> str:
    """A strategy's paper trading, in a few words, with the link to the job's page."""
    role = "" if live["role"] == "survivor" else ", a test of the chain"
    when = f"since {live['since']}" if live.get("trading", True) else f"from {live['since']} to {live['last']}"
    return (f"gate 8 {when}{role}: {live['identical']} of {live['compared']} signals identical, "
            f"{live['return']:+.2%} ([log]({PAPER_PAGE}))")


def outcome(run: dict | None) -> str:
    if run is None:
        return "not run"
    if run.get("void"):
        return "void"
    return "passes" if run["survivor"] else f"gate {run['failed']}"


def outcomes(runs: list[dict]) -> str:
    """The strategies counted by what their run reached."""
    reached = Counter(outcome(s["run"]) for s in runs)
    parts = [f"{reached['passes']} passing gates 1 to 7"]
    parts += [f"{reached[f'gate {n}']} stopped at gate {n}" for n in range(1, 8) if reached[f"gate {n}"]]
    parts += [f"{reached['void']} void"] if reached["void"] else []
    parts += [f"{reached['not run']} not run yet"] if reached["not run"] else []
    return ", ".join(parts)


def reached(strategy: dict) -> str:
    run = strategy["run"]
    if run is None:
        return "not run yet"
    said = (f"void: {run['void']}" if run.get("void") else
            "passes gates 1 to 7" if run["survivor"] else f"stops at gate {run['failed']}")
    if strategy["changed"]:
        said += " (its card was edited after the run)"
    elif strategy["renamed"]:
        said += f" (run as {run['card']}, the folder's name then)"
    return said


def reasoned(lab: Path = LAB) -> dict[str, list[str]]:
    """Strategy folders that hold a reasoning and no card, by the theory their name starts with: a
    theory recorded `not-testable` keeps its reason there, in `reasoning.md`, and no card is drawn."""
    found: dict[str, list[str]] = {}
    for folder in sorted(p for p in (lab / "strategies").glob("*/") if p.is_dir()):
        named = re.match(r"^(.+?)-\d{2}-", folder.name)
        if named and (folder / "reasoning.md").exists() and not (folder / "card.yaml").exists():
            found.setdefault(named.group(1), []).append(folder.relative_to(lab).as_posix())
    return found


def reason_cell(folder: str, status: str) -> str:
    what = "not testable" if status == "not-testable" else "no card"
    return f"[{folder.rsplit('/', 1)[-1]}]({folder}/) · {what}: [reasoning]({folder}/reasoning.md)"


def cell(strategy: dict, live: dict | None = None) -> str:
    links = [f"[{strategy['id']}]({strategy['folder']}/)", reached(strategy)]
    if strategy["id"] in (live or {}):
        links.append(gate_8(live[strategy["id"]]))
    if strategy["pending"]:
        links.append("report not yet drawn")
    elif strategy["report"]:
        links.append(f"[report]({strategy['folder']}/report.ipynb)")
    if strategy["verdict"]:
        links.append(f"[verdict]({strategy['folder']}/verdict.md)")
    return " · ".join(links)


def plural(n: int, one: str, many: str) -> str:
    return f"{n} {one if n == 1 else many}"


def render(lab: Path = LAB, registry_path: Path = registry.REGISTRY) -> str:
    bank, runs, live = theories(lab), strategies(lab, registry_path), paper_trading(lab)
    reasons = reasoned(lab)
    by_theory: dict[str, list[dict]] = {}
    for strategy in runs:
        by_theory.setdefault(strategy["theory"], []).append(strategy)
    counts = Counter(t.get("status", "untouched") for t in bank)
    out = ["# Status", "",
           "Every theory of the [bank](bank/), its status, and each strategy drawn from it with the gate it",
           "reached. Regenerated at every run; rejected strategies stay.", "",
           f"**{plural(len(bank), 'theory', 'theories')}**: "
           + " · ".join(f"{counts.get(s, 0)} {s}" for s in STATUSES) + ".", "",
           f"**{plural(len(runs), 'strategy', 'strategies')}**: {outcomes(runs)}"
           + (f"; {trading} under paper trading" if (trading := sum(s.get('trading', True) for s in live.values()))
              else "") + ".", "",
           "| Theory | Family | Status | Strategies |", "|---|---|---|---|"]
    for theory in bank:
        drawn = "<br>".join([*(cell(s, live) for s in by_theory.pop(theory["id"], [])),
                             *(reason_cell(f, theory.get("status", "untouched")) for f in reasons.get(theory["id"], []))])
        out.append(f"| [{theory['id']}]({theory['file']}) {theory.get('title', '')} | {theory.get('family', '')} "
                   f"| {theory.get('status', 'untouched')} | {drawn} |")
    orphans = [s for group in by_theory.values() for s in group]
    if orphans:
        out += ["", "Strategies whose theory is not in the bank:", ""]
        out += [f"- {cell(s, live)}" for s in orphans]
    folders = {s["run"]["card_hash"] for s in runs if s["run"]}
    gone = [line for key, line in runs_by_card(registry_path).items() if key not in folders]
    if gone:
        out += ["", "Runs in the registry whose card is no longer in a strategy folder:", ""]
        out += [f"- {line['card']}, run on {line['time'][:10]}" for line in gone]
    return "\n".join(out) + "\n"


def write(lab: Path = LAB, registry_path: Path = registry.REGISTRY, board: Path | None = None) -> Path:
    board = board or lab / "STATUS.md"
    board.write_text(render(lab, registry_path))
    return board


def main() -> int:
    try:
        print(write(), file=sys.stderr)
    except RuntimeError as error:                 # a registry line that is not one, named
        print(f"refused: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
