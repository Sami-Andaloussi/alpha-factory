"""SC-006-01, the year's winning sectors over December's last sessions (build-plan.md): over each
year's window, from the close of December's `entry` session to the close of its `exit` session,
counted back from its last, the `winners` sector funds nearest their year's high on the ranking
session, in equal parts; the funds in equal parts otherwise, set back to equal parts on the market's
first session of each month; on the New York Stock Exchange's calendar of scheduled sessions derived
from its holiday rules alone."""
import numpy as np
import pandas as pd
from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday, Holiday, USLaborDay,
                                    USMartinLutherKingJr, USMemorialDay, USPresidentsDay,
                                    USThanksgivingDay, nearest_workday, sunday_to_monday)

RANK = -12          # December's twelfth-last scheduled session: the winners are ranked on or before it


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


def ranked(closes, tradable, first, day):
    """Each fund's drop from its highest close since the year's `first` session to `day`, for the
    funds that traded on `first` and on `day`: zero at the high, negative below it."""
    live = tradable.loc[first] & tradable.loc[day]
    span = closes.loc[first:day, live[live].index]
    return (span.loc[day] / span.max() - 1).dropna()


def positions(market, winners, entry, exit):
    if winners < 1 or not RANK < entry < exit <= -1:
        raise ValueError("winners is 1 or more; entry and exit are sessions of December counted back, "
                         "after the ranking session, entry before exit")
    index, closes, tradable = market.prices.index, market.signal_prices, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=62), index[-1] + pd.Timedelta(days=62))
    after = sessions.searchsorted(index, side="right")
    following = pd.Series(sessions[np.minimum(after, len(sessions) - 1)], index=index)  # next scheduled
    # 2. outside the windows, the funds that trade in equal parts
    trading = tradable.astype(float)
    number = trading.sum(axis=1)
    weights = trading.div(number.where(number > 0), axis=0).fillna(0.0)
    in_window = pd.Series(False, index=index)
    for year in sorted(set(index.year)):
        december = sessions[(sessions.year == year) & (sessions.month == 12)]
        this_year = index[index.year == year]
        on_or_before = this_year[this_year <= december[RANK]] if len(december) >= -RANK else []
        if not len(on_or_before):
            continue
        # 3. the ranking: on the market's last session on or before the twelfth-last scheduled one,
        #    the funds that traded on the year's first session, by their drop from the year's high
        drop = ranked(closes, tradable, this_year[0], on_or_before[-1])
        if drop.empty:
            continue
        cut = drop.sort_values(ascending=False).iloc[:winners].min()
        chosen = drop.index[drop >= cut]                                   # ties at the cut included
        # 4. the window: the sessions whose next scheduled session is after entry, up to exit
        held = (following > december[entry]) & (following <= december[exit])
        rows = held[held].index
        if not len(rows):
            continue
        live = tradable.loc[rows, chosen].astype(float)
        weights.loc[rows] = 0.0
        weights.loc[rows, chosen] = live.div(live.sum(axis=1).where(live.sum(axis=1) > 0), axis=0).fillna(0.0)
        in_window |= held
    # 5. a target where the state changes, on the first session of each month outside the windows,
    #    and on the first session
    month = pd.Series(index.to_period("M"), index=index)
    first_of_month = month.ne(month.shift()).to_numpy()
    change = in_window.ne(in_window.shift()).to_numpy() | (first_of_month & ~in_window.to_numpy())
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
