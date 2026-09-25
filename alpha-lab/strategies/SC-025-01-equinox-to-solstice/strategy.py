"""SC-025-01, out of the northern equity funds from the equinox to the solstice (build-plan.md): the
four funds in equal parts on every session but those of the window from 22 September for `days`
days, cash in those, on the New York Stock Exchange's calendar of scheduled sessions derived from its
holiday rules alone (SC-017-01's calendar, copied)."""
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


def in_window(date, days) -> bool:
    """Whether `date` falls on 22 September of its own year or of the year before, or on one of the
    `days` - 1 days after it (step 2)."""
    for year in (date.year, date.year - 1):
        if 0 <= (date - dt.date(year, 9, 22)).days < days:
            return True
    return False


def positions(market, days):
    if not 1 <= days <= 365:
        raise ValueError("days is from 1 to 365")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    # 2-3. on each session of the market, whether the next scheduled session is outside the window
    after = sessions[sessions.searchsorted(index, side="right")]
    holding = pd.Series([not in_window(d.date(), days) for d in after], index=index)
    # 4. the weights: the funds that trade, in equal parts, while holding; nothing otherwise; a
    #    target only on the sessions on which the state changes, and on the first
    trading = tradable.astype(float)
    count = trading.sum(axis=1)
    weights = trading.div(count.where(count > 0), axis=0).fillna(0.0)
    weights = weights.mul(holding.astype(float), axis=0)
    change = np.array(holding.ne(holding.shift()).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
