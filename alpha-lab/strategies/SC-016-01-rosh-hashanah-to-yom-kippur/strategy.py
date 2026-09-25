"""SC-016-01, out of the market from Rosh Hashanah to Yom Kippur (build-plan.md): the five equity
funds in equal parts on every session but those after the last scheduled session before Rosh
Hashanah's first day and up to the last scheduled session before the day `days` calendar days after
it, the eve of Yom Kippur at 8, and nothing, cash, over those; Rosh Hashanah from the Hebrew
calendar's rules and sessions from the New York Stock Exchange's holiday rules, read from no price."""
from datetime import date

import numpy as np
import pandas as pd
from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday, Holiday, USLaborDay,
                                    USMartinLutherKingJr, USMemorialDay, USPresidentsDay,
                                    USThanksgivingDay, nearest_workday, sunday_to_monday)

HEBREW_EPOCH = -1373427                          # 1 Tishri of year 1, as a proleptic ordinal


def _elapsed(year: int) -> int:
    """Days from the epoch to the conjunction's day of Tishri of Hebrew `year`, postponed off
    Sunday, Wednesday and Friday and past a conjunction at or after noon (step 1)."""
    months = (235 * year - 234) // 19            # months elapsed, 7 leap years in 19
    parts = 12084 + 13753 * months               # parts (1,080 an hour) past the months' 29 days
    day = 29 * months + parts // 25920           # 25,920 parts a day
    return day + 1 if (3 * (day + 1)) % 7 < 3 else day


def _correction(year: int) -> int:
    """The postponement that keeps the year's length among the calendar's six (step 1)."""
    before, this, after = _elapsed(year - 1), _elapsed(year), _elapsed(year + 1)
    if after - this == 356:
        return 2
    if this - before == 382:
        return 1
    return 0


def rosh_hashanah(gregorian_year: int) -> pd.Timestamp:
    """Rosh Hashanah's first day, 1 Tishri, in the autumn of `gregorian_year` (step 1)."""
    year = gregorian_year + 3761
    return pd.Timestamp(date.fromordinal(HEBREW_EPOCH + _elapsed(year) + _correction(year)))


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
    """Weekdays from `first` to `last` less the scheduled holidays; read from no price (step 2)."""
    days = pd.bdate_range(first, last)
    holidays = ScheduledHolidays().holidays(start=days[0], end=days[-1])
    return days[~days.isin(holidays)]


def in_window(sessions: pd.DatetimeIndex, days: int) -> pd.Series:
    """For each scheduled session, whether it lies after the last scheduled session before Rosh
    Hashanah's first day and no later than the last before the day `days` days after it (step 3)."""
    window = np.zeros(len(sessions), dtype=bool)
    for year in range(sessions[0].year, sessions[-1].year + 1):
        new_year = rosh_hashanah(year)
        start = sessions.searchsorted(new_year)                  # first session on or after it
        end = sessions.searchsorted(new_year + pd.Timedelta(days=days))
        if start == 0 or end >= len(sessions):                   # the calendar does not hold it all
            continue
        window[start:end] = True                                 # after start - 1, through end - 1
    return pd.Series(window, index=sessions)


def positions(market, days):
    if days < 1:
        raise ValueError("days is 1 or more")
    index, tradable = market.prices.index, market.tradable
    # 2. the calendar of scheduled sessions, past the market's last session by two months
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    # 3. the window's scheduled sessions
    window = in_window(sessions, days)
    # 4. on each session of the market, whether the next scheduled session is held (not in the window)
    after = sessions.searchsorted(index, side="right")
    holding = pd.Series(~window.to_numpy()[after], index=index)
    trading = tradable.astype(float)
    count = trading.sum(axis=1)
    weights = trading.div(count.where(count > 0), axis=0).fillna(0.0).mul(holding.astype(float), axis=0)
    # a target only on the sessions on which the state changes, and on the first
    change = np.array(holding.ne(holding.shift()).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
