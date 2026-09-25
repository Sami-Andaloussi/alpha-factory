"""SC-019-01, the January barometer (build-plan.md): each of the five equity funds holds a fifth of
the portfolio over January; from February, a fund whose return over the year's first `months`
calendar months was positive keeps its fifth for the rest of the year, and one whose return was zero
or negative leaves its fifth in cash; the funds are bought back on the session before the next
year's first scheduled session, placed on the New York Stock Exchange's calendar of scheduled
sessions derived from its holiday rules alone."""
import numpy as np
import pandas as pd
from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday, Holiday, USLaborDay,
                                    USMartinLutherKingJr, USMemorialDay, USPresidentsDay,
                                    USThanksgivingDay, nearest_workday, sunday_to_monday)


class ScheduledHolidays(AbstractHolidayCalendar):
    """The exchange's scheduled holidays by rule: New Year's Day moves to Monday from a Sunday and is
    not observed from a Saturday; Juneteenth (from 2022), Independence Day and Christmas move to the
    nearest weekday."""
    rules = [
        Holiday("New Year's Day", month=1, day=1, observance=sunday_to_monday),
        USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay,
        Holiday("Juneteenth", month=6, day=19, start_date="2022-01-01", observance=nearest_workday),
        Holiday("Independence Day", month=7, day=4, observance=nearest_workday),
        USLaborDay, USThanksgivingDay,
        Holiday("Christmas", month=12, day=25, observance=nearest_workday),
    ]


def scheduled_sessions(first, last) -> pd.DatetimeIndex:
    """Weekdays from `first` to `last` less the scheduled holidays; read from no price (step 1)."""
    days = pd.bdate_range(first, last)
    holidays = ScheduledHolidays().holidays(start=days[0], end=days[-1])
    return days[~days.isin(holidays)]


def positions(market, months):
    if not 1 <= months <= 11:
        raise ValueError("months is from 1 to 11")
    prices, tradable = market.prices, market.tradable
    index = prices.index
    # 1. the sessions whose next scheduled session falls in the next year
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    after = sessions.searchsorted(index, side="right")
    next_year = pd.Series(sessions[after].year > index.year, index=index)
    # 2. the signal: each fund's return over the year's first `months` months, read the next month
    seen = prices.shift(1)                                     # the closes up to the session before
    weights = pd.DataFrame(np.nan, index=index, columns=prices.columns)
    equal = tradable.astype(float)
    equal = equal.div(equal.sum(axis=1).where(lambda n: n > 0), axis=0).fillna(0.0)
    # 3. the targets: the five in equal parts on the first session and before each new year
    buy_back = next_year.to_numpy().copy()
    buy_back[0] = True
    weights.loc[buy_back] = equal.loc[buy_back]
    for year in sorted(set(index.year)):
        decide = index[(index.year == year) & (index.month == months + 1)]
        if len(decide) == 0:
            continue
        day = decide[0]                                        # the first session of the next month
        before = seen.loc[:day]
        start = before.index[before.index.year < year]
        first = prices.loc[prices.index.year == year]
        base = (prices.loc[start[-1]] if len(start) else first.apply(lambda s: s.dropna().iloc[0]
                                                                     if s.notna().any() else np.nan))
        end = seen.loc[day]                                    # the last close of the signal's months
        rose = (end / base - 1.0) > 0
        held = tradable.loc[day] & rose.fillna(False)
        count = tradable.loc[day].sum()
        weights.loc[day] = held.astype(float) / count if count > 0 else 0.0
    return weights
