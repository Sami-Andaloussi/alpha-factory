"""SC-007-01, the Santa Claus window (build-plan.md): the five equity funds in equal parts over the
last `december` scheduled sessions of each December and the first `january` of each January, cash
otherwise, on the New York Stock Exchange's calendar of scheduled sessions derived from its holiday
rules alone."""
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


def in_window(sessions: pd.DatetimeIndex, december: int, january: int) -> pd.Series:
    """For each scheduled session, whether it is among the last `december` sessions of a December or
    the first `january` sessions of a January."""
    months = pd.Series(sessions.to_period("M"), index=sessions)
    forward = months.groupby(months).cumcount() + 1                           # 1 for the first
    backward = months.groupby(months).cumcount(ascending=False) + 1           # 1 for the last
    return ((sessions.month == 12) & (backward <= december)) | ((sessions.month == 1) & (forward <= january))


def positions(market, december, january):
    if december < 1 or january < 1:
        raise ValueError("december and january are 1 or more")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    window = in_window(sessions, december, january)
    # 2. on each session of the market, whether the next scheduled session is in the window
    after = sessions.searchsorted(index, side="right")
    holding = pd.Series(window.to_numpy()[after], index=index)
    # 3. the weights: the funds that trade, in equal parts, while holding; nothing otherwise
    trading = tradable.astype(float)
    count = trading.sum(axis=1)
    weights = trading.div(count.where(count > 0), axis=0).fillna(0.0).mul(holding.astype(float), axis=0)
    # 4. a target only on the sessions on which the state changes, and on the first
    change = np.array(holding.ne(holding.shift()).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
