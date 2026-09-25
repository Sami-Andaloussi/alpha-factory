"""The universe, fixed before any hypothesis card, so that no result depends on a choice made after
seeing it.

Every asset carries its cluster, which gate 6 leaves out one at a time, the first session on which
the lab can trade it (the start of the sample or the asset's own start, whichever is later, unless
its first months traded too thinly for the lab's costs) and the reason it is here. Bitcoin's signals
are lagged one day, since Yahoo's bitcoin close comes about four hours after the US close. The
Treasury funds were added before the first card, so that trend and allocation rules have a defensive
asset; they were frozen in a snapshot of their own.
"""
from dataclasses import dataclass

START, END = "2005-01-01", "2025-12-31"
RISK_FREE = "^IRX"  # 13-week Treasury bill, annual yield in per cent
TRADING_DAYS = 252  # sessions a year: annualisation, and the daily bill rate


@dataclass(frozen=True)
class Asset:
    ticker: str
    cluster: str
    first_session: str
    why: str
    lagged: bool = False


UNIVERSE = (
    Asset("XLB", "sectors", "2005-01-03", "Materials: chemicals, metals and mining, construction materials."),
    Asset("XLC", "sectors", "2018-06-19", "Communication services: telecoms, media and online platforms."),
    Asset("XLE", "sectors", "2005-01-03", "Energy: oil, gas and their equipment, the equity side of the energy cycle."),
    Asset("XLF", "sectors", "2005-01-03", "Financials: banks, insurers and capital markets."),
    Asset("XLI", "sectors", "2005-01-03", "Industrials: machinery, aerospace and transport."),
    Asset("XLK", "sectors", "2005-01-03", "Information technology, the largest sector and the one that grew most."),
    Asset("XLP", "sectors", "2005-01-03", "Consumer staples, the defensive sector."),
    Asset("XLRE", "sectors", "2016-09-19", "Real estate, a sector apart from financials since 2016; traded "
          "from 2016-09-19, before which the fund traded a few thousand shares a day."),
    Asset("XLU", "sectors", "2005-01-03", "Utilities, defensive and sensitive to interest rates."),
    Asset("XLV", "sectors", "2005-01-03", "Health care, defensive, with a cycle of its own: drug approvals and policy."),
    Asset("XLY", "sectors", "2005-01-03", "Consumer discretionary, the cyclical consumer."),
    Asset("SPY", "broad", "2005-01-03", "US large caps (S&P 500): the market most theories are stated on."),
    Asset("QQQ", "broad", "2005-01-03", "US large-cap growth (Nasdaq-100)."),
    Asset("IWM", "broad", "2005-01-03", "US small caps (Russell 2000), for effects of size."),
    Asset("EFA", "broad", "2005-01-03", "Developed markets outside North America (MSCI EAFE)."),
    Asset("EEM", "broad", "2005-01-03", "Emerging markets (MSCI Emerging Markets)."),
    Asset("GLD", "metals", "2005-01-03", "Gold, a store of value and a hedge in crises."),
    Asset("SLV", "metals", "2006-04-28", "Silver, a precious metal with an industrial side."),
    Asset("DBC", "commodities", "2006-02-06", "A commodity basket: energy, metals and agriculture futures."),
    Asset("BTC-USD", "crypto", "2014-09-17", "Bitcoin, traded every day and on its own cycle.", lagged=True),
    Asset("SHY", "bonds", "2005-01-03", "US Treasuries of one to three years, close to cash."),
    Asset("IEF", "bonds", "2005-01-03", "US Treasuries of seven to ten years."),
    Asset("TLT", "bonds", "2005-01-03", "US Treasuries of twenty years and more, the longest duration."),
)
TICKERS = tuple(asset.ticker for asset in UNIVERSE)
CLUSTERS = tuple(dict.fromkeys(asset.cluster for asset in UNIVERSE))
LAGGED = tuple(asset.ticker for asset in UNIVERSE if asset.lagged)
# Francs per dollar and per euro, which a campaign run in francs needs: not assets, never traded.
CHF_RATES = ("USDCHF=X", "EURCHF=X")


def cluster_of(ticker: str) -> str:
    for asset in UNIVERSE:
        if asset.ticker == ticker:
            return asset.cluster
    raise KeyError(f"{ticker} is not in the universe")
