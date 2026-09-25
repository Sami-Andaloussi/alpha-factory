"""SC-026-01, out of the US sector funds on the session after each change of the clocks
(build-plan.md): the sector funds in equal parts on every session but the `sessions` first scheduled
sessions after each of the United States' changes of the clocks, cash in those, on the New York Stock
Exchange's calendar of scheduled sessions derived from its holiday rules alone (SC-025-01's calendar,
copied)."""
import datetime as dt

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


def nth_sunday(year, month, n) -> dt.date:
    """The `n`th Sunday of the month, or its last when `n` is -1."""
    if n > 0:
        first = dt.date(year, month, 1)
        return first + dt.timedelta(days=(6 - first.weekday()) % 7 + 7 * (n - 1))
    last = dt.date(year + (month == 12), month % 12 + 1, 1) - dt.timedelta(days=1)
    return last - dt.timedelta(days=(last.weekday() + 1) % 7)


def clock_changes(year) -> list:
    """The United States' two changes of the clocks in `year`, by the rule in force (step 2)."""
    if year >= 2007:
        return [nth_sunday(year, 3, 2), nth_sunday(year, 11, 1)]
    return [nth_sunday(year, 4, 1), nth_sunday(year, 10, -1)]


def positions(market, sessions):
    if not 1 <= sessions <= 5:
        raise ValueError("sessions is from 1 to 5")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    calendar = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    # 2. the sessions out: the `sessions` first scheduled sessions after each change's Sunday
    out = set()
    for year in range(calendar[0].year, calendar[-1].year + 1):
        for sunday in clock_changes(year):
            after = calendar[calendar.searchsorted(pd.Timestamp(sunday), side="right"):][:sessions]
            out.update(after)
    # 3. on each session of the market, whether the next scheduled session is not out
    following = calendar[calendar.searchsorted(index, side="right")]
    holding = pd.Series([day not in out for day in following], index=index)
    # 4. the weights: the funds that trade, in equal parts, while holding; nothing otherwise; a
    #    target only on the first session and on the sessions on which it changes
    trading = tradable.astype(float)
    count = trading.sum(axis=1)
    weights = trading.div(count.where(count > 0), axis=0).fillna(0.0)
    weights = weights.mul(holding.astype(float), axis=0)
    change = np.array(weights.ne(weights.shift()).any(axis=1).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
