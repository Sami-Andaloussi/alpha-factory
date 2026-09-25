"""SC-018-01, equities from November to April (build-plan.md): the five equity funds in equal parts
in every calendar month but the `months` from the month named `first`, cash in those, the first
`late` sessions of the first month out and the last `early` of the last still held, on the New York
Stock Exchange's calendar of scheduled sessions derived from its holiday rules alone (SC-017-01's
code, copied)."""
import numpy as np
import pandas as pd
from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday, Holiday, USLaborDay,
                                    USMartinLutherKingJr, USMemorialDay, USPresidentsDay,
                                    USThanksgivingDay, nearest_workday, sunday_to_monday)

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]


class ScheduledHolidays(AbstractHolidayCalendar):
    """The exchange's scheduled holidays by rule: New Year's Day moves to Monday from a Sunday and
    is not observed from a Saturday; Juneteenth (from 2022), Independence Day and Christmas move to
    the nearest weekday."""
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


def held_sessions(sessions: pd.DatetimeIndex, out: list[int], late: int, early: int) -> np.ndarray:
    """For each scheduled session, whether equities are held over it: its month is not out, or it
    is among the first `late` sessions of the first month out, or among the last `early` of the
    last."""
    months = pd.Series(sessions.month, index=sessions)
    period = pd.Series(sessions.to_period("M"), index=sessions)
    forward = period.groupby(period).cumcount() + 1                          # +1, +2, ...
    backward = period.groupby(period).cumcount(ascending=False) + 1          # 1 for the last
    held = ~months.isin(out)
    held |= (months == out[0]) & (forward <= late)
    held |= (months == out[-1]) & (backward <= early)
    return held.to_numpy()


def positions(market, first, months, late, early):
    if first not in MONTHS or not 1 <= months <= 11 or late < 0 or early < 0:
        raise ValueError("first is an English month name, months from 1 to 11, late and early "
                         "0 or more")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=45),
                                  index[-1] + pd.Timedelta(days=62))
    # 2. the months out, in order from `first`, and the scheduled sessions held
    start = MONTHS.index(first)
    out = [(start + k) % 12 + 1 for k in range(months)]
    held = held_sessions(sessions, out, late, early)
    # 3. on each session of the market, whether the next scheduled session is held
    after = sessions.searchsorted(index, side="right")
    holding = pd.Series(held[after], index=index)
    # 4. the weights: the funds that trade, in equal parts, while holding; nothing otherwise; a
    #    target only on the sessions on which the state changes, and on the first
    trading = tradable.astype(float)
    count = trading.sum(axis=1)
    weights = trading.div(count.where(count > 0), axis=0).fillna(0.0)
    weights = weights.mul(holding.astype(float), axis=0)
    change = np.array(holding.ne(holding.shift()).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
