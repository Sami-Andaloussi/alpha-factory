"""The theory bank: every file keeps the format, judges nothing, and the index matches the files."""
import pytest

from lab import bank

GOOD = """---
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

Taxable investors sell their losing stocks before the end of the tax year to offset their gains.

## Prediction

Stocks that lost over the year fall into late December and recover in early January.

## What would refute it

No recovery of the year's losers in January, or the same pattern where no tax year ends.

## References

- Branch, B. (1977). A tax loss trading rule. Journal of Business, 50(2), 198-207.
"""


def bank_with(tmp_path, **files):
    for name, text in files.items():
        (tmp_path / name).write_text(text)
    return tmp_path


def test_a_file_that_keeps_the_format_passes_and_is_indexed(tmp_path):
    folder = bank_with(tmp_path, **{"SC-004-tax-loss-selling.md": GOOD})
    assert bank.problems(folder) == []
    index = bank.render(folder)
    assert "| [SC-004](SC-004-tax-loss-selling.md) | Tax-loss selling | flows, behavioural | stocks | weeks | untouched |" in index
    assert "## Seasonality and calendar effects (SC, 1)" in index


@pytest.mark.parametrize("change, message", [
    (("status: untouched\n", "status: untouched\npriority: high\n"), "fields must be exactly"),
    (("id: SC-004", "id: SC-4"), "is not a family code"),
    (("family: seasonality and calendar effects", "family: trend and momentum"), "does not match the id"),
    (("mechanism: [flows, behavioural]", "mechanism: [flows, luck]"), "mechanism must be"),
    (("asset_classes: [stocks]", "asset_classes: stocks"), "asset_classes must be"),
    (("horizon: [weeks]", "horizon: [quarters]"), "horizon must be"),
    (("status: untouched", "status: promising"), "status must be"),
    (("## What would refute it", "## Evidence"), "sections must be exactly"),
    (("No recovery of the year's losers in January, or the same pattern where no tax year ends.", ""),
     "a section is empty"),
    (("recover in early January.", "recover in early January, a strong candidate: testable with our data."),
     "a judgment before processing"),
    (("recover in early January.", "recover in early January. The evidence is weak."), "a judgment before processing"),
    (("recover in early January.", "recover in early January, a pattern well documented."), "a judgment before processing"),
    (("recover in early January.", "recover in early January; the literature is young."), "a judgment before processing"),
    (("recover in early January.", "recover in early January. This is a young literature."), "a judgment before processing"),
    (("recover in early January.", "recover in early January; the literature is still being built."),
     "a judgment before processing"),
    (("recover in early January.", "recover in early January, with strong empirical support."),
     "a judgment before processing"),
    (("recover in early January.", "recover in early January, a pattern formally documented."),
     "a judgment before processing"),
    (("recover in early January.", "recover in early January, observed robustly."), "a judgment before processing"),
    (("recover in early January.", "recover in early January, a robust anomaly."), "a judgment before processing"),
    (("recover in early January.", "recover in early January; identification is difficult."),
     "a judgment before processing"),
    (("recover in early January.", "recover in early January. It is hard to test."), "a judgment before processing"),
    (("recover in early January.", "recover in early January. High priority."), "a judgment before processing"),
    (("recover in early January.", "recover in early January, with an expected Sharpe ratio of 0.8."),
     "a judgment before processing"),
    (("recover in early January.", "recover in early January, suitable for a long-only universe of ETFs."),
     "a judgment before processing"),
    (("recover in early January.", "recover in early January, economically plausible."), "a judgment before processing"),
    (("---\n\n## Mechanism", "---\n\nA note before the sections.\n\n## Mechanism"), "sections must be exactly"),
    (("Taxable investors sell", "Les investisseurs vendent les titres perdants avant la fin de l'année pour "
      "compenser des plus-values, et la pression est plus forte sur les petites valeurs dans une année"),
     "text left in French"),
    (("Taxable investors sell", "Le signal de la tendance et le retard de la moyenne mobile. Taxable investors sell"),
     "text left in French"),
    (("- Branch, B. (1977).", "- Travaux sur la vente des titres perdants de fin d'année, cités dans les ouvrages du "
      "domaine.\n- Branch, B. (1977)."), "text left in French"),
])
def test_each_break_of_the_format_is_named(tmp_path, change, message):
    old, new = change
    assert old in GOOD
    folder = bank_with(tmp_path, **{"SC-004-tax-loss-selling.md": GOOD.replace(old, new, 1)})
    found = bank.problems(folder)
    assert any(message in line for line in found), found


@pytest.mark.parametrize("words", ["testable with daily data", "the strength of the evidence", "as in our data",
                                   "we recommend it", "[to verify]", "[à vérifier]", "Tier 2", "a priority for testing",
                                   "a promising lead"])
def test_each_judgment_pattern_refuses_its_own_words(tmp_path, words):
    folder = bank_with(tmp_path, **{"SC-004-tax-loss-selling.md": GOOD.replace(
        "recover in early January.", f"recover in early January ({words}).", 1)})
    assert any("a judgment before processing" in line for line in bank.problems(folder))


def test_two_theories_never_share_a_title(tmp_path):
    folder = bank_with(tmp_path, **{"SC-004-tax-loss-selling.md": GOOD,
                                    "SC-005-tax-selling.md": GOOD.replace("id: SC-004", "id: SC-005")})
    assert any("the title 'Tax-loss selling' is already SC-004-tax-loss-selling.md's" in line
               for line in bank.problems(folder))


def test_the_check_says_when_the_index_is_out_of_date(tmp_path, monkeypatch, capsys):
    folder = bank_with(tmp_path, **{"SC-004-tax-loss-selling.md": GOOD})
    monkeypatch.setattr(bank, "BANK", folder)
    monkeypatch.setattr(bank, "problems", lambda folder: [])
    (folder / bank.INDEX).write_text(bank.render(folder))
    assert bank.main(["check"]) == 0
    (folder / bank.INDEX).write_text("# stale\n")
    assert bank.main(["check"]) == 1 and "the index is out of date" in capsys.readouterr().err


def test_ids_are_unique_and_files_named_after_them(tmp_path):
    folder = bank_with(tmp_path, **{"SC-004-tax-loss-selling.md": GOOD, "SC-004-tax-selling.md": GOOD,
                                    "SC-004_Tax.md": GOOD})
    found = bank.problems(folder)
    assert sum("already used" in line for line in found) == 2
    assert any("SC-004_Tax.md: the file is not named" in line for line in found)


def test_the_bank_keeps_its_format_and_its_index_is_current():
    if not bank.files():
        pytest.skip("the bank holds no theory yet")
    assert bank.problems() == []
    assert (bank.BANK / bank.INDEX).read_text() == bank.render()
