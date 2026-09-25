"""SC-009-01, the dash-for-cash week (build-plan.md): the five equity funds in equal parts on every
session but a window of `length` scheduled sessions ending `end` sessions before each month's last,
counted with 1 the last, and cash over the window, on the New York Stock Exchange's calendar of
scheduled sessions derived from its holiday rules alone."""
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
    """Weekdays from `first` to `last` less the scheduled holidays; read from no price."""
    days = pd.bdate_range(first, last)
    holidays = ScheduledHolidays().holidays(start=days[0], end=days[-1])
    return days[~days.isin(holidays)]


def in_window(sessions: pd.DatetimeIndex, end: int, length: int) -> pd.Series:
    """For each scheduled session, whether it lies from -(end + length - 1) to -end of its month, -1
    being the month's last scheduled session."""
    months = pd.Series(sessions.to_period("M"), index=sessions)
    backward = months.groupby(months).cumcount(ascending=False) + 1           # 1 for the last: -1
    return (backward >= end) & (backward <= end + length - 1)


def positions(market, end, length):
    if end < 1 or length < 1:
        raise ValueError("end and length are 1 or more")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    window = in_window(sessions, end, length)
    # 2. on each session of the market, whether the next scheduled session is outside the window
    after = sessions.searchsorted(index, side="right")
    holding = pd.Series(~window.to_numpy()[after], index=index)
    # 3. the weights: the funds that trade, in equal parts, while holding; nothing otherwise
    trading = tradable.astype(float)
    count = trading.sum(axis=1)
    weights = trading.div(count.where(count > 0), axis=0).fillna(0.0).mul(holding.astype(float), axis=0)
    # 4. a target only on the sessions on which the state changes, and on the first
    change = np.array(holding.ne(holding.shift()).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
