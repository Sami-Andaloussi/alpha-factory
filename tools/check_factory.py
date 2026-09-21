#!/usr/bin/env python3
"""Check the factory blueprint: page layout, navigation, links, flows and Notion leftovers.

Usage:  python3 tools/check_factory.py [--final] [-q]

Scope: every Markdown page under factory/ except factory/FRAMING.md. Three kinds of page:
sub-section pages (factory/sections/s*/s*.md), section pages (factory/sections/s*/README.md)
and top-level pages (all others). Each rule is stated below.

First use (warning only): after the TL;DR, the first use of a glossary term on any
page must be a link to its glossary entry, except on the three pages that define or list the terms
rather than use them: the glossary, the references and the index of sub-sections. Code, link texts, headings,
step summaries and bold labels (**Goal.**, **Service levels:**) are not uses. Terms and links
are read across the line breaks of a paragraph, so a term cut by a wrapped line is still found.
A word that is a glossary term but means something else on the page is reworded, so one word
keeps one meaning.

Interfaces notes (error): on a sub-section page, whatever follows the Interfaces table (what each
flow carries, the constraints, the service levels) sits in one <details> block with a <summary>,
so that the page, unfolded, shows its TL;DR, purpose, Interfaces table and gates.

Interfaces page (error): the generated block of factory/interfaces.md must be what
tools/build_interfaces.py builds from the 64 Interfaces tables today.

Overview (error): the first Mermaid diagram of factory/README.md is the first one of
factory/architecture.md, so that the front page and the architecture draw the same factory.

Build sequence (error): the phase table of factory/build-sequence.md places each of the 64
sub-sections in exactly one phase that counts steps, and gives each phase the number of steps,
design tasks, execution tasks and steps tagged with both that its pages carry, with its share of
all steps.

Cited in (error): each row of the books table in factory/references.md names, in its "Cited in"
column, exactly the sections whose pages (section or sub-section) cite that book by its anchor.

Prints one line per problem, naming the file and the line, then a summary. Exits with code 1
if there is any error; warnings alone keep it green. Standard library only.

  --final   all 64 sub-section pages must exist, every index row must link to its page, and
            every missing link target is an error.
  -q        print errors in full, and warnings as one count per kind.

Spelling (warning): British spelling (-ise, -yse, -ll-) everywhere, except in the bibliographic cell
of a row of factory/references.md, which quotes each title as published.

What is read where: Notion leftovers are searched on every line, fenced code included, since a
leftover is never legitimate anywhere. Everything else (navigation, headings, TL;DR, tables,
links, French detection) reads prose only: lines outside fenced code blocks, with inline code
spans (single or double backticks) removed. Indented code blocks are not used in the blueprint
and are read as prose.
"""
from __future__ import annotations

import argparse
import bisect
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
FACTORY = ROOT / "factory"
SECTIONS = FACTORY / "sections"
INDEX = SECTIONS / "README.md"
FACTORY_README = FACTORY / "README.md"
ROOT_README = ROOT / "README.md"
GLOSSARY = FACTORY / "glossary.md"
REFERENCES = FACTORY / "references.md"
INTERFACES_PAGE = FACTORY / "interfaces.md"
BUILD_SEQUENCE = FACTORY / "build-sequence.md"
ARCHITECTURE = FACTORY / "architecture.md"
MERMAID = re.compile(r"```mermaid\n(.*?)\n```", re.S)
EXCLUDED = {FACTORY / "FRAMING.md"}
FIRST_USE_EXEMPT = {GLOSSARY, REFERENCES, INDEX}  # they define or list the terms, not use them

SECTION_FOLDERS = [
    "s1-data-foundation",
    "s2-feature-label-factory",
    "s3-strategy-lab",
    "s4-validation",
    "s5-decision-execution",
    "s6-monitoring",
    "s7-lifecycle",
]
SUBSECTION_COUNTS = [8, 10, 9, 10, 9, 8, 10]
ALL_IDS = [f"S{s}.{k}" for s, n in enumerate(SUBSECTION_COUNTS, 1) for k in range(1, n + 1)]
VALID_IDS = set(ALL_IDS)

SUBSECTION_HEADINGS = ["TL;DR", "Purpose", "Interfaces", "Gates", "Steps", "Deliverables", "References"]
INTERFACE_COLUMNS = ["Direction", "Artifact", "From / To"]
DIRECTIONS = {"in", "out"}
ENDPOINTS = {"lab", "external"}
STEP_TAG = re.compile(r"— (?:Design task|Execution task|Design task \+ Execution task)$")
STEP_TAG_OF = re.compile(r"<summary>.*— (Design task \+ Execution task|Design task|Execution task)</summary>")
GATE_PARTS = ("Entry", "Exit", "Requalification")
TLDR_MAX_LINES = 3
TLDR_MAX_CHARS = 200  # rendered characters per TL;DR line; longer lines only warn

SUBSECTION_FILE = re.compile(r"^s([1-7])\.(\d{1,2})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LINK = re.compile(r"!?\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^()\s]+)(?:\s+\"[^\"]*\")?\)")
INLINE_CODE = re.compile(r"``.+?``|`[^`]*`")
EXPLICIT_ANCHOR = re.compile(r"\b(?:id|name)=\"([^\"]+)\"")
SUMMARY = re.compile(r"<summary>(.*?)</summary>")
EXTERNAL = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//)")

CHECKBOX = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\[[ xX]\]")
DOUBLE_SPACED_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.) {2,}\S")
TE_TAG = re.compile(r"\((?:TE|TNE)(?:\s*/\s*(?:TE|TNE))?\)")
STATUS_TAG = re.compile(r"\$\s*-\s*(?:full|partiel|survol)\s*\$", re.IGNORECASE)
NOTION_ID = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{32}(?![0-9a-fA-F])")
GLOSSARY_ENTRY = re.compile(r'<a id="([^"]+)"></a>\*\*(.+?)\*\*')
BOLD_LABEL = re.compile(r"\*\*[^*]+?[.:]\*\*")  # **Goal.**, **Service levels:** and the like

FRENCH_WORDS = {
    "le", "les", "des", "du", "une", "et", "pour", "avec", "dans", "qui", "que", "cette",
    "sont", "aux", "leur", "leurs", "selon", "donc", "ainsi", "être", "très", "mais", "nous",
    "vous", "ils", "elles", "doit", "peut", "chaque", "lorsque", "afin", "dont", "également",
    "sur", "pas", "où", "ces", "sans", "entre", "puis", "vers", "chez", "après", "avant",
}
FRENCH_LETTERS = set("àâçéèêëîïôûùüÿœ")
WORD = re.compile(r"[A-Za-zÀ-ÿœŒ]+")
# British spelling (-ise, -yse, -ll-); file names keep their original spelling, so link targets are not read.
AMERICAN = re.compile(r"\b[A-Za-z]{4,}?iz(?:e|es|ed|ing|ation|ations|er|ers)\b"
                      r"|\b(?:[Aa]nal|[Pp]araly|[Cc]ataly)yz(?:e|es|ed|ing|er|ers)\b"
                      r"|\b(?:[Ll]abe|[Mm]ode|[Cc]ance|[Ss]igna|[Ll]eve|[Tt]rave|[Ff]ue|[Tt]ota|[Jj]ourna)l(?:ing|ed)\b")
SIZE_WORDS = ("size", "sizes", "sized", "sizing")


# --------------------------------------------------------------------------- reporting

class Report:
    def __init__(self) -> None:
        self.errors: list[tuple[str, int, str]] = []
        self.warnings: list[tuple[str, int, str, str]] = []

    def error(self, path: Path, line: int, message: str) -> None:
        self.errors.append((rel(path), line, message))

    def warn(self, path: Path, line: int, kind: str, message: str) -> None:
        self.warnings.append((rel(path), line, kind, message))

    def print(self, quiet: bool) -> None:
        for path, line, message in sorted(self.errors):
            print(f"{path}:{line}: error: {message}")
        if quiet:
            for kind, count in sorted(Counter(w[2] for w in self.warnings).items()):
                print(f"warning: {count} x {kind}")
        else:
            for path, line, _, message in sorted(self.warnings):
                print(f"{path}:{line}: warning: {message}")
        print(f"check_factory: {len(self.errors)} error(s), {len(self.warnings)} warning(s)")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


# --------------------------------------------------------------------------- markdown helpers

def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def prose_lines(lines: list[str]):
    """Yield (line number, text) for every line outside fenced code blocks."""
    fence = None
    for number, line in enumerate(lines, 1):
        match = FENCE.match(line)
        if match:
            if fence is None:
                fence = match.group(1)
            elif line.strip().startswith(fence):
                fence = None
            continue
        if fence is None:
            yield number, line


def links_in(line: str) -> list[tuple[str, str]]:
    """Return (text, target) for every Markdown link on a line, ignoring inline code."""
    return [(m.group(1), m.group(2)) for m in LINK.finditer(INLINE_CODE.sub("", line))]


def rendered(text: str) -> str:
    """Approximate the text a reader sees: links become their text, markup disappears."""
    text = re.sub(r"!?\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.replace("`", "").replace("**", "").replace("*", "").strip()


def slugify(heading: str) -> str:
    """GitHub's heading anchor: lower case, punctuation dropped, spaces become hyphens."""
    kept = []
    for char in rendered(heading).lower():
        category = unicodedata.category(char)
        if char in " -_" or category[0] in "LN" or category == "Mn":
            kept.append(char)
    return "".join(kept).replace(" ", "-")


_anchor_cache: dict[Path, set[str]] = {}


def anchors_of(path: Path) -> set[str]:
    if path not in _anchor_cache:
        anchors: set[str] = set()
        seen: Counter[str] = Counter()
        for _, line in prose_lines(read_lines(path)):
            heading = HEADING.match(line)
            if heading:
                base = slugify(heading.group(2))
                anchors.add(base if seen[base] == 0 else f"{base}-{seen[base]}")
                seen[base] += 1
            anchors.update(EXPLICIT_ANCHOR.findall(line))
        _anchor_cache[path] = anchors
    return _anchor_cache[path]


def resolve(page: Path, target: str) -> tuple[Path, str]:
    path_part, _, anchor = target.partition("#")
    destination = page if not path_part else (page.parent / unquote(path_part)).resolve()
    return destination, anchor


def section_of(lines: list[str], title: str) -> list[tuple[int, str]]:
    """Lines under the level-2 heading `title`, up to the next level-1 or level-2 heading."""
    inside, out = False, []
    for number, line in prose_lines(lines):
        heading = HEADING.match(line)
        if heading and len(heading.group(1)) <= 2:
            if inside:
                break
            inside = len(heading.group(1)) == 2 and heading.group(2) == title
            continue
        if inside:
            out.append((number, line))
    return out


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


# --------------------------------------------------------------------------- the index

def read_index(report: Report) -> dict[str, Path]:
    """Map each sub-section ID to the page its index row links to."""
    pages: dict[str, Path] = {}
    listed: set[str] = set()
    if not INDEX.exists():
        report.error(INDEX, 0, "the sub-section index is missing")
        return pages
    for number, line in prose_lines(read_lines(INDEX)):
        cells = table_cells(line) if line.startswith("|") else []
        if not cells or not re.fullmatch(r"S\d+\.\d+", cells[0]):
            continue
        sub_id = cells[0]
        if sub_id not in VALID_IDS:
            report.error(INDEX, number, f"unknown sub-section ID {sub_id}")
            continue
        if sub_id in listed:
            report.error(INDEX, number, f"{sub_id} is listed twice")
            continue
        listed.add(sub_id)
        links = links_in(cells[1]) if len(cells) > 1 else []
        if not links:
            report.error(INDEX, number, f"the row of {sub_id} does not link to its page")
            continue
        target = links[0][1]
        section, sub = sub_id[1:].split(".")
        folder = SECTION_FOLDERS[int(section) - 1]
        name = target.split("/")[-1]
        match = SUBSECTION_FILE.match(name)
        if (not target.startswith(folder + "/") or target.count("/") != 1 or not match
                or (match.group(1), match.group(2)) != (section, sub)):
            report.error(INDEX, number,
                         f"{sub_id} links to '{target}', expected '{folder}/s{section}.{sub}-<slug>.md'")
            continue
        pages[sub_id] = (INDEX.parent / target).resolve()
    for sub_id in ALL_IDS:
        if sub_id not in listed:
            report.error(INDEX, 0, f"{sub_id} is missing from the index")
    return pages


# --------------------------------------------------------------------------- page checks

def kind_of(page: Path) -> str:
    parts = page.relative_to(FACTORY).parts
    if len(parts) == 3 and parts[0] == "sections":
        if parts[2] == "README.md":
            return "section"
        if parts[2].startswith("s"):
            return "subsection"
    return "top"


def required_navigation(page: Path, kind: str, index: dict[str, Path], sub_id: str | None) -> list[Path]:
    if kind == "top":
        return [ROOT_README if page == FACTORY_README else FACTORY_README]
    if kind == "section":
        folder = page.parent.name
        if folder not in SECTION_FOLDERS:
            return [INDEX]
        position = SECTION_FOLDERS.index(folder)
        targets = [INDEX]
        if position > 0:
            targets.append(SECTIONS / SECTION_FOLDERS[position - 1] / "README.md")
        if position < len(SECTION_FOLDERS) - 1:
            targets.append(SECTIONS / SECTION_FOLDERS[position + 1] / "README.md")
        return targets
    targets = [page.parent / "README.md"]
    if sub_id in VALID_IDS:
        position = ALL_IDS.index(sub_id)
        for neighbour in (position - 1, position + 1):
            if 0 <= neighbour < len(ALL_IDS) and ALL_IDS[neighbour] in index:
                targets.append(index[ALL_IDS[neighbour]])
    return targets


def check_frame(page: Path, lines: list[str], kind: str, index: dict[str, Path],
                sub_id: str | None, report: Report) -> None:
    """Navigation line, then the title, then the TL;DR."""
    prose = [(n, l) for n, l in prose_lines(lines) if l.strip()]
    if not prose:
        report.error(page, 1, "empty page")
        return
    nav_number, nav_line = prose[0]
    if HEADING.match(nav_line) or not links_in(nav_line):
        report.error(page, nav_number, "the first line must be the navigation line (links, above the title)")
        body = prose
    else:
        linked = {resolve(page, target)[0] for _, target in links_in(nav_line)
                  if not EXTERNAL.match(target)}
        for target in required_navigation(page, kind, index, sub_id):
            if target.resolve() not in linked:
                report.error(page, nav_number, f"navigation line does not link to {rel(target)}")
        body = prose[1:]

    titles = [(n, HEADING.match(l)) for n, l in body if HEADING.match(l)]
    if not body or not HEADING.match(body[0][1]) or len(HEADING.match(body[0][1]).group(1)) != 1:
        report.error(page, body[0][0] if body else nav_number, "the title (# heading) must follow the navigation line")
        return
    for number, heading in titles[1:]:
        if len(heading.group(1)) == 1:
            report.error(page, number, "more than one title (# heading)")
    if kind == "subsection" and sub_id and not re.match(rf"{re.escape(sub_id)}(?!\d)", body[0][1][2:].strip()):
        report.error(page, body[0][0], f"the title must start with the page's ID, {sub_id}")

    if len(body) < 2 or HEADING.match(body[1][1]) is None or body[1][1].strip() != "## TL;DR":
        report.error(page, body[0][0], "'## TL;DR' must come right after the title")
        return
    tldr = []
    for number, line in body[2:]:
        if HEADING.match(line):
            break
        tldr.append((number, line))
    if not tldr:
        report.error(page, body[1][0], "empty TL;DR")
    elif len(tldr) > TLDR_MAX_LINES:
        report.error(page, tldr[0][0], f"TL;DR has {len(tldr)} lines, at most {TLDR_MAX_LINES}")
    for number, line in tldr:
        if len(rendered(line)) > TLDR_MAX_CHARS:
            report.warn(page, number, "long TL;DR line",
                        f"TL;DR line of {len(rendered(line))} characters (aim for {TLDR_MAX_CHARS} at most)")


def check_subsection(page: Path, lines: list[str], index: dict[str, Path], seen_ids: dict[str, Path],
                     flows: dict[str, tuple[Path, list[Flow]]], report: Report) -> str | None:
    match = SUBSECTION_FILE.match(page.name)
    if not match:
        report.error(page, 0, "sub-section file name must be sN.K-<slug>.md")
        return None
    sub_id = f"S{match.group(1)}.{match.group(2)}"
    if sub_id not in VALID_IDS:
        report.error(page, 0, f"{sub_id} is not a sub-section ID")
        return None
    if sub_id in seen_ids:
        report.error(page, 0, f"a second page for {sub_id} (first: {rel(seen_ids[sub_id])})")
    seen_ids[sub_id] = page
    if sub_id in index and index[sub_id] != page.resolve():
        report.error(page, 0, f"{sub_id} is not the page the index names ({rel(index[sub_id])})")

    headings = [(n, HEADING.match(l)) for n, l in prose_lines(lines) if HEADING.match(l)]
    level_two = [(n, h.group(2)) for n, h in headings if len(h.group(1)) == 2]
    if [title for _, title in level_two] != SUBSECTION_HEADINGS:
        found = ", ".join(title for _, title in level_two) or "none"
        report.error(page, level_two[0][0] if level_two else 0,
                     f"the ## headings must be {', '.join(SUBSECTION_HEADINGS)} in this order (found: {found})")

    flows[sub_id] = (page, check_interfaces(page, lines, report))
    check_interfaces_fold(page, lines, report)
    check_gates(page, lines, report)
    check_steps(page, lines, report)
    for title in ("Deliverables", "References"):
        if not any(line.strip() for _, line in section_of(lines, title)) and title in [t for _, t in level_two]:
            report.warn(page, 0, "empty section", f"'## {title}' is empty")
    return sub_id


Flow = tuple  # (line number, direction, artifact key, artifact label, set of From / To values)


def check_interfaces(page: Path, lines: list[str], report: Report) -> list[Flow]:
    """Check the first Interfaces table and return its rows, for the cross-page check."""
    body = section_of(lines, "Interfaces")
    rows: list[tuple[int, str]] = []
    flows: list[Flow] = []
    for number, line in body:  # the first table only: notes and other tables may follow it
        if line.strip().startswith("|"):
            rows.append((number, line))
        elif rows:
            break
    if len(rows) < 3:
        report.error(page, body[0][0] if body else 0, "the Interfaces section needs a table with at least one row")
        return flows
    header_number, header = rows[0]
    if table_cells(header) != INTERFACE_COLUMNS:
        report.error(page, header_number, f"Interfaces columns must be: {' | '.join(INTERFACE_COLUMNS)}")
        return flows
    for number, line in rows[2:]:
        cells = table_cells(line)
        if len(cells) != 3:
            report.error(page, number, "an Interfaces row must have three cells")
            continue
        direction, artifact, endpoints = cells
        if direction not in DIRECTIONS:
            report.error(page, number, f"Direction must be 'in' or 'out', not '{direction}'")
        glossary_anchors = [anchor for destination, anchor in (resolve(page, t) for _, t in links_in(artifact))
                            if destination == GLOSSARY.resolve()]
        if not rendered(artifact):
            report.error(page, number, "empty Artifact cell")
        elif not glossary_anchors:
            report.warn(page, number, "artifact not linked to the glossary",
                        f"artifact '{rendered(artifact)}' does not link to a glossary term")
        values = [rendered(v) for v in endpoints.split(",")]
        if not any(values):
            report.error(page, number, "empty From / To cell")
        for value in values:
            if value not in VALID_IDS and value not in ENDPOINTS:
                report.error(page, number, f"From / To value '{value}' is not a sub-section ID, 'lab' or 'external'")
        key = glossary_anchors[0] if glossary_anchors else rendered(artifact).lower()
        flows.append((number, direction, key, rendered(artifact), set(values)))
    return flows


def check_flows(flows: dict[str, tuple[Path, list[Flow]]], report: Report) -> None:
    """Between two written sub-section pages, every flow must be declared at both ends: an out row
    naming a page needs an in row of the same artifact on that page, naming the sender, and back."""
    def declares(sub_id: str, direction: str, key: str, other: str) -> bool:
        return any(d == direction and k == key and other in values for _, d, k, _, values in flows[sub_id][1])

    for sub_id, (page, rows) in sorted(flows.items()):
        for number, direction, key, label, values in rows:
            for other in sorted(values & flows.keys()):
                if direction == "out" and not declares(other, "in", key, sub_id):
                    report.error(page, number, f"sends '{label}' to {other}, whose Interfaces has no "
                                               f"'in' row for it from {sub_id}")
                if direction == "in" and not declares(other, "out", key, sub_id):
                    report.error(page, number, f"receives '{label}' from {other}, whose Interfaces has no "
                                               f"'out' row for it to {sub_id}")


def check_interfaces_page(flows: dict[str, tuple[Path, list[Flow]]], report: Report) -> None:
    """The generated block of factory/interfaces.md must match the Interfaces tables."""
    if not INTERFACES_PAGE.exists():
        return
    import build_interfaces  # it imports this module, so it is imported here, not at the top

    text = INTERFACES_PAGE.read_text(encoding="utf-8")
    new = build_interfaces.rebuilt(text, {sub_id: rows for sub_id, (_, rows) in flows.items()})
    if new is None:
        report.error(INTERFACES_PAGE, 0, "the markers of the generated block are missing")
    elif new != text:
        report.error(INTERFACES_PAGE, 0, "out of date with the Interfaces tables: "
                                         "run python3 tools/build_interfaces.py")


def step_counts(lines: list[str]) -> tuple[int, int, int, int]:
    """(steps, design tasks, execution tasks, steps tagged with both) of a sub-section page."""
    tags = [m.group(1) for m in (STEP_TAG_OF.search(line) for _, line in prose_lines(lines)) if m]
    both = tags.count("Design task + Execution task")
    return len(tags), tags.count("Design task"), tags.count("Execution task"), both


def check_build_sequence(index: dict[str, Path], report: Report) -> None:
    """The phase table of factory/build-sequence.md must match the step tags of the 64 pages."""
    if not BUILD_SEQUENCE.exists():
        return
    lines = read_lines(BUILD_SEQUENCE)
    header = next((n for n, line in prose_lines(lines)
                   if table_cells(line)[:1] == ["Phase"] and "Steps" in table_cells(line)), None)
    if header is None:
        report.error(BUILD_SEQUENCE, 0, "no phase table with a 'Steps' column")
        return
    columns = table_cells(lines[header - 1])
    where = {name: columns.index(name) for name in ("Steps", "Design", "Execution", "Both", "Share")}
    ids_column = next(i for i, name in enumerate(columns) if name.startswith("Sub-sections"))
    counts = {sub_id: step_counts(read_lines(page)) for sub_id, page in index.items() if page.exists()}
    total = sum(c[0] for c in counts.values())
    placed: Counter = Counter()
    number = header + 1
    while number < len(lines) and lines[number].startswith("|"):
        number += 1
        cells = table_cells(lines[number - 1])
        if not cells[where["Steps"]].isdigit():
            continue
        ids = [i for i in re.findall(r"\bS\d\.\d+\b", rendered(cells[ids_column])) if i in VALID_IDS]
        placed.update(ids)
        sums = [sum(counts.get(i, (0, 0, 0, 0))[k] for i in ids) for k in range(4)]
        expected = dict(zip(("Steps", "Design", "Execution", "Both"), map(str, sums)))
        expected["Share"] = f"{round(100 * sums[0] / total)}%" if total else "0%"
        for name, value in expected.items():
            if cells[where[name]] != value:
                report.error(BUILD_SEQUENCE, number, f"phase {cells[0]}: '{name}' should be {value}")
    for sub_id in ALL_IDS:
        if placed[sub_id] != 1:
            report.error(BUILD_SEQUENCE, header, f"{sub_id} is placed in {placed[sub_id]} phases, not 1")


def check_overview(report: Report) -> None:
    """The front page's diagram must be the architecture's overview, character for character."""
    if not (ARCHITECTURE.exists() and FACTORY_README.exists()):
        return
    front = MERMAID.search(FACTORY_README.read_text(encoding="utf-8"))
    overview = MERMAID.search(ARCHITECTURE.read_text(encoding="utf-8"))
    if front and overview and front.group(1) != overview.group(1):
        report.error(FACTORY_README, 0, "its diagram differs from the overview of factory/architecture.md")


def check_cited_in(report: Report) -> None:
    """The "Cited in" column of the books table must name the sections whose pages cite each book."""
    cited: dict[str, set[int]] = {}
    for page in sorted(SECTIONS.glob("s*/*.md")):
        section = int(page.parent.name[1])
        for _, target in (link for _, line in prose_lines(read_lines(page)) for link in links_in(line)):
            path, _, anchor = unquote(target).partition("#")
            if anchor and Path(path).name == REFERENCES.name:
                cited.setdefault(anchor, set()).add(section)
    lines = read_lines(REFERENCES)
    header = next((n for n, line in prose_lines(lines) if table_cells(line)[-1:] == ["Cited in"]), None)
    if header is None:
        report.error(REFERENCES, 0, "no table with a 'Cited in' column")
        return
    for number, line in prose_lines(lines):
        match = EXPLICIT_ANCHOR.search(line)
        if number <= header or not match or not line.startswith("|"):
            continue
        listed: set[int] = set()
        for token in table_cells(line)[-1].split(","):
            bounds = re.findall(r"S([1-7])", token)
            if bounds:
                listed |= set(range(int(bounds[0]), int(bounds[-1]) + 1))
        actual = cited.get(match.group(1), set())
        if listed != actual:
            names = ", ".join(f"S{s}" for s in sorted(actual)) or "none"
            report.error(REFERENCES, number, f"'{match.group(1)}': 'Cited in' should list {names}")


def check_interfaces_fold(page: Path, lines: list[str], report: Report) -> None:
    """The notes under the Interfaces table sit in one <details> block, opened by its <summary>."""
    body = section_of(lines, "Interfaces")
    k = 0
    while k < len(body) and not body[k][1].strip().startswith("|"):
        k += 1
    while k < len(body) and body[k][1].strip().startswith("|"):
        k += 1
    notes = [(number, line.strip()) for number, line in body[k:] if line.strip()]
    if not notes:
        return
    folded = (notes[0][1] == "<details>" and notes[-1][1] == "</details>" and len(notes) > 2
              and SUMMARY.search(notes[1][1]) is not None
              and sum(line.count("<details>") for _, line in notes) == 1)
    if not folded:
        report.error(page, notes[0][0], "the notes under the Interfaces table go in one <details> block, "
                                        "its <summary> first, so that the page shows its table and its gates unfolded")


def check_gates(page: Path, lines: list[str], report: Report) -> None:
    text = " ".join(line for _, line in section_of(lines, "Gates"))
    for part in GATE_PARTS:
        if part not in text:
            report.warn(page, 0, "gate part missing", f"the Gates section does not name its '{part}' part")


def check_steps(page: Path, lines: list[str], report: Report) -> None:
    body = section_of(lines, "Steps")
    summaries = [(n, s) for n, l in body for s in SUMMARY.findall(l)]
    if not summaries:
        report.error(page, body[0][0] if body else 0, "no step found: each step is a <details> block with a <summary>")
    for number, summary in summaries:
        if not STEP_TAG.search(summary.strip()):
            report.error(page, number, "step tag must end the summary: '— Design task', '— Execution task' "
                                       "or '— Design task + Execution task'")
    opened = sum(l.count("<details>") for _, l in body)
    if opened != len(summaries):
        report.warn(page, body[0][0] if body else 0, "details/summary mismatch",
                    f"{opened} <details> blocks for {len(summaries)} <summary> lines")


def check_links(page: Path, lines: list[str], index_pages: set[Path], final: bool, report: Report) -> None:
    for number, line in prose_lines(lines):
        for _, target in links_in(line):
            if EXTERNAL.match(target):
                continue
            destination, anchor = resolve(page, target)
            if not destination.exists():
                if destination in index_pages and not final:
                    report.warn(page, number, "sub-section page not written yet",
                                f"link to {rel(destination)}, listed in the index, not written yet")
                else:
                    report.error(page, number, f"broken link '{target}'")
                continue
            if anchor and destination.is_file() and destination.suffix == ".md":
                if anchor not in anchors_of(destination):
                    report.error(page, number, f"link '{target}': no anchor '#{anchor}' in {rel(destination)}")


def check_leftovers(page: Path, lines: list[str], report: Report) -> None:
    for number, line in enumerate(lines, 1):
        if CHECKBOX.match(line):
            report.error(page, number, "Notion checkbox")
        if TE_TAG.search(line):
            report.error(page, number, "(TE)/(TNE) is the source's task tag: use 'Design task' / 'Execution task'; "
                                       "for tracking error, write the words in full")
        if STATUS_TAG.search(line):
            report.error(page, number, "Notion status tag ($-full$, $-partiel$, $-survol$)")
        if NOTION_ID.search(line):
            report.error(page, number, "32-hex Notion ID")
    for number, line in prose_lines(lines):
        if DOUBLE_SPACED_ITEM.match(line):
            report.warn(page, number, "double space after a list marker", "one space after '-' or '1.'")
        text = INLINE_CODE.sub("", re.sub(r"\]\([^)]*\)", "]", line)).lower()
        words = {w for w in WORD.findall(text)}
        french = words & FRENCH_WORDS
        accents = sum(1 for char in text if char in FRENCH_LETTERS)
        if len(french) >= 3 or (french and accents >= 2):
            report.warn(page, number, "line looks French", "line looks French")
        if page == REFERENCES and line.startswith("|") and EXPLICIT_ANCHOR.search(line):
            line = "|" + "|".join(table_cells(line)[1:])  # a title is quoted as published, in its own spelling
        american = [w for w in AMERICAN.findall(INLINE_CODE.sub("", re.sub(r"\]\([^)]*\)", "]", line)))
                    if not w.lower().endswith(SIZE_WORDS)]
        if american:
            report.warn(page, number, "American spelling",
                        f"British spelling expected (-ise, -yse, -ll-): {', '.join(american)}")


# --------------------------------------------------------------------------- glossary terms at first use

Terms = tuple  # (forms: lower-case form or upper-case acronym -> anchor, list of compiled patterns)


def glossary_terms() -> Terms:
    """Every written form of every glossary term, and the patterns that find them in a line.

    A form is the entry's name without its parenthesis. A name "A / B" gives both halves, and a
    last word the halves share goes to both: "Hard / soft constraint" gives "hard constraint" and
    "soft constraint". Acronyms match in upper case only; other forms in any case. A plural in -s
    or -es matches too."""
    forms: dict[str, str] = {}
    if GLOSSARY.exists():
        for anchor, name in GLOSSARY_ENTRY.findall(GLOSSARY.read_text(encoding="utf-8")):
            parts = [part.strip() for part in re.sub(r"\s*\([^)]*\)", "", name).split(" / ")]
            if len(parts) == 2 and " " not in parts[0] and " " in parts[1]:
                parts[0] += parts[1][parts[1].index(" "):]
            for part in parts:
                forms.setdefault(part if part.isupper() else part.lower(), anchor)
    patterns = []
    for upper in (True, False):
        words = sorted((form for form in forms if form.isupper() == upper), key=len, reverse=True)
        if words:
            body = "|".join(re.escape(word).replace(r"\ ", r"\s+") for word in words)
            patterns.append(re.compile(rf"(?<![\w-])(?:{body})(?:e?s)?(?![\w-])", 0 if upper else re.IGNORECASE))
    return forms, patterns


def term_uses(line: str, terms: Terms) -> list[tuple[int, int, str]]:
    """(start, end, anchor) of each glossary term used in the line's prose. Inline code, links
    (text and target) and bold labels are not uses; a longer term wins over a shorter one in it."""
    forms, patterns = terms
    chars = list(line)
    for regex in (INLINE_CODE, LINK, BOLD_LABEL):
        for match in regex.finditer(line):
            chars[match.start():match.end()] = "\0" * (match.end() - match.start())
    text = "".join(chars)
    found = []
    for pattern in patterns:
        for match in pattern.finditer(text):
            word = " ".join(match.group(0).split())
            for key in (word, word[:-2] if word.endswith("es") else "", word[:-1] if word.endswith("s") else ""):
                anchor = forms.get(key) or forms.get(key.lower())
                if key and anchor:
                    found.append((match.start(), match.end(), anchor))
                    break
    kept: list[tuple[int, int, str]] = []
    for start, end, anchor in sorted(found, key=lambda use: (use[0], use[0] - use[1])):
        if not kept or start >= kept[-1][1]:
            kept.append((start, end, anchor))
    return kept


def paragraphs(lines: list[str]):
    """Runs of consecutive prose lines, as lists of (line number, text). A blank line, a heading
    or a summary line stands alone, so that a term or a link is read across the line breaks of
    one paragraph, and never across two."""
    run: list[tuple[int, str]] = []
    for number, line in prose_lines(lines):
        alone = not line.strip() or HEADING.match(line) or SUMMARY.search(line)
        if run and (alone or run[-1][0] != number - 1):
            yield run
            run = []
        run.append((number, line))
        if alone:
            yield run
            run = []
    if run:
        yield run


def first_uses_unlinked(page: Path, lines: list[str], terms: Terms) -> list[tuple[int, int, int, str, str]]:
    """(line number, start, end, anchor, words) of each glossary term whose first use after the
    TL;DR comes before any link from the page to its glossary entry. Terms and links are read
    across the line breaks of a paragraph; a use that runs onto the next line ends, in the
    tuple, at the end of its first line, and its words give it whole."""
    after_tldr, in_tldr = None, False
    for number, line in prose_lines(lines):
        heading = HEADING.match(line)
        if heading and len(heading.group(1)) == 2:
            if in_tldr:
                after_tldr = number
                break
            in_tldr = heading.group(2) == "TL;DR"
    if after_tldr is None:
        return []
    linked: dict[str, tuple[int, int]] = {}
    unlinked, seen = [], set()
    for run in paragraphs(lines):
        text = " ".join(line for _, line in run)
        starts, offset = [], 0
        for _, line in run:
            starts.append(offset)
            offset += len(line) + 1

        def where(position: int) -> tuple[int, int, int]:
            k = bisect.bisect_right(starts, position) - 1
            return run[k][0], position - starts[k], len(run[k][1])

        for match in LINK.finditer(INLINE_CODE.sub(lambda m: "\0" * len(m.group(0)), text)):
            destination, anchor = resolve(page, match.group(2))
            if destination == GLOSSARY and anchor:
                linked.setdefault(anchor, where(match.start())[:2])
        first_number, first_line = run[0]
        if first_number <= after_tldr or HEADING.match(first_line) or SUMMARY.search(first_line):
            continue
        for start, end, anchor in term_uses(text, terms):
            if anchor not in seen:
                seen.add(anchor)
                number, column, width = where(start)
                unlinked.append((number, column, min(column + end - start, width), anchor, text[start:end]))
    return [use for use in unlinked if linked.get(use[3], (len(lines) + 1, 0)) > use[:2]]


def check_first_use(page: Path, lines: list[str], terms: Terms, report: Report) -> None:
    for number, _start, _end, anchor, words in first_uses_unlinked(page, lines, terms):
        report.warn(page, number, "glossary term not linked at first use",
                    f"first use of '{' '.join(words.split())}' needs a link to glossary.md#{anchor}")


# --------------------------------------------------------------------------- main

def pages_to_check() -> list[Path]:
    return sorted(p for p in FACTORY.rglob("*.md") if p not in EXCLUDED)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the factory blueprint pages.")
    parser.add_argument("--final", action="store_true",
                        help="all 64 sub-section pages must exist and every missing target is an error")
    parser.add_argument("-q", "--quiet", action="store_true", help="count warnings per kind instead of listing them")
    args = parser.parse_args()

    report = Report()
    index = read_index(report)
    index_pages = set(index.values())
    seen_ids: dict[str, Path] = {}
    flows: dict[str, tuple[Path, list[Flow]]] = {}
    terms = glossary_terms()

    for page in pages_to_check():
        lines = read_lines(page)
        kind = kind_of(page)
        sub_id = None
        if kind == "subsection":
            sub_id = check_subsection(page, lines, index, seen_ids, flows, report)
        elif kind == "section" and page.parent.name not in SECTION_FOLDERS:
            report.error(page, 0, f"unknown section folder '{page.parent.name}'")
        check_frame(page, lines, kind, index, sub_id, report)
        check_links(page, lines, index_pages, args.final, report)
        check_leftovers(page, lines, report)
        if page not in FIRST_USE_EXEMPT:
            check_first_use(page, lines, terms, report)
    check_flows(flows, report)
    check_interfaces_page(flows, report)
    check_build_sequence(index, report)
    check_overview(report)
    check_cited_in(report)

    if args.final:
        for sub_id in ALL_IDS:
            if sub_id in index and not index[sub_id].exists():
                report.error(index[sub_id], 0, f"{sub_id}: page missing (listed in the index)")

    report.print(args.quiet)
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
