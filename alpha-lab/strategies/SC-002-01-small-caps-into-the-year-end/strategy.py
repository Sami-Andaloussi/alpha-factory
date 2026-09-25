"""SC-002-01, the small caps for the S&P 500 from mid-December (build-plan.md): over each year's
window, from the first scheduled session on or after day `start` of December to December's `end`
session, SPY's part moved to IWM; the five equity funds in equal parts otherwise, set back to equal
parts on the first scheduled session of each month; on the New York Stock Exchange's calendar of
scheduled sessions derived from its holiday rules alone."""
import numpy as np
import pandas as pd
from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday, Holiday, USLaborDay,
                                    USMartinLutherKingJr, USMemorialDay, USPresidentsDay,
                                    USThanksgivingDay, nearest_workday, sunday_to_monday)

SMALL, LARGE = "IWM", "SPY"


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


def in_window(sessions: pd.DatetimeIndex, start: int, end: int) -> pd.Series:
    """For each scheduled session, whether it is in a year's window: after the first scheduled
    session on or after day `start` of December, up to and including December's `end` session,
    counted back from its last, -1 the last."""
    held = pd.Series(False, index=sessions)
    for year in range(sessions[0].year, sessions[-1].year + 1):
        december = sessions[(sessions.year == year) & (sessions.month == 12)]
        opening = december[december.day >= start]
        if not len(opening) or len(december) < -end:
            continue                                  # a December the calendar does not cover
        held[(sessions > opening[0]) & (sessions <= december[end])] = True
    return held


def positions(market, start, end):
    if not 1 <= start <= 31 or end > -1:
        raise ValueError("start is a day of December, end a session of December counted back, -1 or less")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=62), index[-1] + pd.Timedelta(days=62))
    window = in_window(sessions, start, end)
    # 2. on each session of the market, whether the next scheduled session is in a window
    after = sessions.searchsorted(index, side="right")
    tilted = pd.Series(window.to_numpy()[after], index=index)
    # 3. the weights: the funds that trade in equal parts; in a window, SPY's part moved to IWM
    trading = tradable.astype(float)
    number = trading.sum(axis=1)
    equal = trading.div(number.where(number > 0), axis=0).fillna(0.0)
    tilt = equal.copy()
    if SMALL in tilt.columns and LARGE in tilt.columns:
        moved = tilt[LARGE].where(tradable[SMALL], 0.0)
        tilt[SMALL] = tilt[SMALL] + moved
        tilt[LARGE] = tilt[LARGE] - moved
    weights = tilt.where(tilted, equal, axis=0)
    # 4. a target where the state changes, on the first scheduled session of each month outside the
    #    windows (the equal parts set back), and on the first session
    month = pd.Series(index.to_period("M"), index=index)
    first_of_month = month.ne(month.shift()).to_numpy()
    change = np.array(tilted.ne(tilted.shift()).to_numpy(), dtype=bool) | (first_of_month & ~tilted.to_numpy())
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
