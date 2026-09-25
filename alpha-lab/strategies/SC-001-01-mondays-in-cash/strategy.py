"""SC-001-01, the equity funds out of the market over each week's first session (build-plan.md): the
five equity funds in equal parts over the sessions that are in, cash over those that are out, on the
New York Stock Exchange's calendar of scheduled sessions derived from its holiday rules alone. With
`day` first, the first `count` scheduled sessions of each calendar week are out; with `day` last, only
the last `count` are in."""
import numpy as np
import pandas as pd
from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday, Holiday, USLaborDay,
                                    USMartinLutherKingJr, USMemorialDay, USPresidentsDay,
                                    USThanksgivingDay, nearest_workday, sunday_to_monday)

DAYS = ("first", "last")


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
    """Weekdays from `first` to `last` less the scheduled holidays; read from no price."""
    days = pd.bdate_range(first, last)
    holidays = ScheduledHolidays().holidays(start=days[0], end=days[-1])
    return days[~days.isin(holidays)]


def in_sessions(sessions: pd.DatetimeIndex, day: str, count: int) -> pd.Series:
    """For each scheduled session, whether the portfolio holds equities over it: with `day` first,
    unless it is among the first `count` sessions of its calendar week; with `day` last, only if it
    is among the last `count`."""
    weeks = pd.Series(sessions.to_period("W-SUN"), index=sessions)           # Monday to Sunday
    if day == "first":
        return weeks.groupby(weeks).cumcount() + 1 > count                    # 1 for the first
    return weeks.groupby(weeks).cumcount(ascending=False) + 1 <= count        # 1 for the last


def positions(market, day, count):
    if day not in DAYS:
        raise ValueError(f"day is one of {', '.join(DAYS)}, not {day!r}")
    if count < 1:
        raise ValueError("count is 1 or more")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by a few weeks
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=14), index[-1] + pd.Timedelta(days=21))
    held = in_sessions(sessions, day, count)
    # 2. on each session of the market, whether the next scheduled session is in
    after = sessions.searchsorted(index, side="right")
    holding = pd.Series(held.to_numpy()[after], index=index)
    # 3. the weights: the funds that trade, in equal parts, while holding; nothing otherwise
    trading = tradable.astype(float)
    number = trading.sum(axis=1)
    weights = trading.div(number.where(number > 0), axis=0).fillna(0.0).mul(holding.astype(float), axis=0)
    # 4. a target only on the sessions on which the state changes, and on the first
    change = np.array(holding.ne(holding.shift()).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
