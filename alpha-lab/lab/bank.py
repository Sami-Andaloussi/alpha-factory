"""The theory bank: one file per theory, described without judgment, and its generated index.

A theory file opens with its fields, then four sections, in this order:

    ---
    id: SC-004
    title: Tax-loss selling
    family: seasonality and calendar effects
    mechanism: [flows, behavioural]
    asset_classes: [stocks]
    horizon: [weeks]
    data: [daily prices, market capitalisation]
    status: untouched
    ---

    ## Mechanism
    ## Prediction
    ## What would refute it
    ## References

The file is named after its id and a short slug: `SC-004-tax-loss-selling.md`. The fields take
their values from the lists below; `data` is free, a list of short names. Nothing in a file judges
the theory before it is processed: whether it can be tested here, how strong its evidence is, how
urgent it is. Those judgments belong to the strategy folders, after the fact.

    python -m lab.bank              # checks every file and writes bank/README.md, the index
    python -m lab.bank check        # checks every file, and that the index is current; writes nothing
    python -m lab.bank check SC     # checks the files whose name starts with SC; writes nothing
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from lab.status import LAB, STATUSES, front_matter

BANK = LAB / "bank"
INDEX = "README.md"
FAMILIES = {
    "TM": "trend and momentum",
    "MR": "mean reversion and relative value",
    "SC": "seasonality and calendar effects",
    "LL": "lead-lag and information diffusion",
    "CA": "cross-asset relative value",
    "FP": "flows and positioning",
    "EF": "earnings and fundamentals",
    "AS": "asset-specific mechanisms",
}
MECHANISMS = {
    "risk premium": "compensation for bearing a risk that others avoid",
    "behavioural": "investors' biases: under- or over-reaction, attention, sentiment",
    "flows": "trades forced by rules, mandates, calendars or taxes, whatever the price",
    "information": "news that reaches prices slowly, or reaches some assets before others",
    "microstructure": "how trading works: liquidity provision, inventory, spreads, price impact",
    "limits to arbitrage": "costs, funding and constraints that keep a mispricing open",
    "structural": "how an asset or market is built: supply schedules, contract design, index rules",
    "macroeconomic": "returns that follow the state of the economy or of policy",
}
ASSET_CLASSES = ("stocks", "equity indices", "sectors", "bonds", "credit", "commodities", "currencies",
                 "crypto", "volatility", "real estate")
HORIZONS = ("intraday", "days", "weeks", "months", "years")
FIELDS = ("id", "title", "family", "mechanism", "asset_classes", "horizon", "data", "status")
SECTIONS = ("Mechanism", "Prediction", "What would refute it", "References")
ID = re.compile(rf"^({'|'.join(FAMILIES)})-\d{{3}}$")
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
JUDGMENT = re.compile(r"testable with|strength of (the )?evidence|\bour (data|setup|universe|lab|means|scope)\b"
                      r"|\bwe (recommend|should|could test)\b|to verify\]|à vérifier|\btier [1-4]\b"
                      r"|\bpriority (for|of) (testing|research)\b|\b(high|low|top) priority\b|\bpromising\b"
                      # the strength of the evidence, in the words the former texts used
                      r"|\b(weak|strong|limited|thin|partial|less developed|solid)( empirical)? (evidence|support)\b"
                      r"|\bevidence\b[^.]{0,20}\b(less developed|weak|thin|limited|scarce)\b"
                      r"|\bliterature is (young|thin|limited|scarce)\b|\byoung literature\b"
                      r"|\bliterature (is )?still (being built|under construction)\b|\bwell[- ]documented\b|\bformally documented\b"
                      r"|\bobserved robustly\b|\brobust anomal|\b(economically|structurally) plausible\b"
                      # whether it can be tested, or suits a scope
                      r"|\bhard to (test|tell|isolate|distinguish)\b|\bidentification is difficult\b"
                      r"|\bsuitable for\b|\bexpected sharpe\b", re.I)
FRENCH = re.compile(r"\b(les|des|une|est|dans|avec|pour|sont|qui|aux|du|cette|ces|le|la|de|un)\b")
MAX_FRENCH = 2                  # French function words tolerated outside the references (a name, a title)
MAX_FRENCH_REFERENCES = 3       # and in the references, where a French title may be quoted


def files(bank: Path = BANK) -> list[Path]:
    return sorted(p for p in bank.glob("*.md") if p.name != INDEX)


def sections(text: str) -> list[tuple[str, str]]:
    """The `## ` sections after the fields, with their text; any text before the first section is
    returned under an empty title."""
    body = text[text.index("\n---", 4) + 4:]
    parts = re.split(r"^## +(.+?)\s*$", body, flags=re.M)
    before = [("", parts[0].strip())] if parts[0].strip() else []
    return before + [(parts[k].strip(), parts[k + 1].strip()) for k in range(1, len(parts) - 1, 2)]


def problems(bank: Path = BANK) -> list[str]:
    """Everything wrong in the bank, one line each; none when every file keeps the format."""
    found, seen, titles = [], {}, {}
    for path in files(bank):
        name, text = path.name, path.read_text()
        try:
            meta = front_matter(path)
        except Exception as error:                      # a broken YAML block
            found.append(f"{name}: fields unreadable ({error})")
            continue
        if list(meta) != list(FIELDS):
            found.append(f"{name}: fields must be exactly {', '.join(FIELDS)}, in this order")
            continue
        ident = str(meta["id"])
        if not ID.match(ident):
            found.append(f"{name}: id {ident!r} is not a family code and three digits")
        elif ident in seen:
            found.append(f"{name}: id {ident} already used by {seen[ident]}")
        seen.setdefault(ident, name)
        slug = name[len(ident) + 1:-3] if name.startswith(f"{ident}-") else ""
        if not SLUG.match(slug):
            found.append(f"{name}: the file is not named <id>-<slug>.md")
        if ID.match(ident) and meta["family"] != FAMILIES[ident[:2]]:
            found.append(f"{name}: family {meta['family']!r} does not match the id")
        title = str(meta["title"] or "").strip()
        if not title:
            found.append(f"{name}: no title")
        elif title.lower() in titles:
            found.append(f"{name}: the title {title!r} is already {titles[title.lower()]}'s")
        titles.setdefault(title.lower(), name)
        for field, allowed in (("mechanism", MECHANISMS), ("asset_classes", ASSET_CLASSES), ("horizon", HORIZONS)):
            values = meta[field]
            if not isinstance(values, list) or not values or any(v not in allowed for v in values):
                found.append(f"{name}: {field} must be a list of {', '.join(allowed)}")
        if not isinstance(meta["data"], list) or not meta["data"] or not all(isinstance(d, str) for d in meta["data"]):
            found.append(f"{name}: data must be a list of short names")
        if meta["status"] not in STATUSES:
            found.append(f"{name}: status must be one of {', '.join(STATUSES)}")
        body = sections(text)
        if [title for title, _ in body] != list(SECTIONS):
            found.append(f"{name}: sections must be exactly {', '.join(SECTIONS)}, in this order")
        elif any(not content for _, content in body):
            found.append(f"{name}: a section is empty")
        judged = JUDGMENT.search(text)
        if judged:
            found.append(f"{name}: a judgment before processing ({judged.group(0)!r})")
        described = "\n".join(content for title, content in body if title != "References")
        cited = "\n".join(content for title, content in body if title == "References")
        if len(FRENCH.findall(described)) > MAX_FRENCH or len(FRENCH.findall(cited)) > MAX_FRENCH_REFERENCES:
            found.append(f"{name}: text left in French")
    return found


def render(bank: Path = BANK) -> str:
    """The index: every theory, family by family, with its fields and its status."""
    rows: dict[str, list[str]] = {code: [] for code in FAMILIES}
    for path in files(bank):
        meta = front_matter(path)
        code = str(meta.get("id", ""))[:2]
        if code in rows:
            rows[code].append(f"| [{meta['id']}]({path.name}) | {meta['title']} | {', '.join(meta['mechanism'])} "
                              f"| {', '.join(meta['asset_classes'])} | {', '.join(meta['horizon'])} | {meta['status']} |")
    total = sum(len(r) for r in rows.values())
    out = ["# The theory bank", "",
           f"{total} theories, one file each, described without judgment: the mechanism, the prediction, what",
           "would refute it, and the references. A theory's status changes as the lab processes it; the",
           "judgments come after, in the strategy folders. Generated by `python -m lab.bank` from the files.", "",
           "Mechanism types: " + "; ".join(f"**{k}**, {v}" for k, v in MECHANISMS.items()) + ".", ""]
    for code, family in FAMILIES.items():
        if rows[code]:
            out += [f"## {family[0].upper()}{family[1:]} ({code}, {len(rows[code])})", "",
                    "| Id | Theory | Mechanism | Asset classes | Horizon | Status |", "|---|---|---|---|---|---|",
                    *rows[code], ""]
    return "\n".join(out).rstrip("\n") + "\n"


def write(bank: Path = BANK) -> Path:
    index = bank / INDEX
    index.write_text(render(bank))
    return index


def main(args: list[str]) -> int:
    checking = args[:1] == ["check"]
    found = [line for line in problems(BANK) if line.startswith(args[1] if checking and len(args) > 1 else "")]
    if checking and len(args) == 1 and not found and (BANK / INDEX).read_text() != render(BANK):
        found.append(f"{INDEX}: the index is out of date; python -m lab.bank writes it again")
    for line in found:
        print(line, file=sys.stderr)
    if checking:
        print(f"{len(found)} problems", file=sys.stderr)
        return 1 if found else 0
    if found:
        print(f"{len(found)} problems; the index is not written", file=sys.stderr)
        return 1
    print(write(), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
