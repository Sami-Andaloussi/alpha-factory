"""SC-027-01, the equity funds held in the fortnight around the new moon (build-plan.md): the five
equity funds in equal parts on the sessions within `days` days of the nearest mean new moon, by the
formula Kaufman gives (Meeus's), cash on the others, on the New York Stock Exchange's calendar of
scheduled sessions derived from its holiday rules alone (SC-026-01's calendar, copied)."""
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


def new_moons(first, last) -> list:
    """The dates of the moon's mean new moons from `first` to `last`, each JDE taken as universal time
    on the date of floor(JDE + 0.5) (step 2)."""
    dates = []
    k0 = int(np.floor((first.toordinal() - dt.date(2000, 1, 6).toordinal()) / 29.530588853)) - 1
    k = k0
    while True:
        t = k / 1236.85
        jde = (2451550.09765 + 29.530588853 * k + 0.0001337 * t ** 2 - 0.000000150 * t ** 3
               + 0.00000000073 * t ** 4)
        day = dt.date(2000, 1, 1) + dt.timedelta(days=int(np.floor(jde + 0.5)) - 2451545)
        if day > last:
            return dates
        if day >= first:
            dates.append(day)
        k += 1


assert new_moons(dt.date(2000, 1, 1), dt.date(2000, 1, 31)) == [dt.date(2000, 1, 6)]


def in_fortnight(dates, moons, days) -> np.ndarray:
    """Whether each date lies within `days` days of the nearest new moon's date (step 3)."""
    ords = np.array([d.toordinal() for d in dates])
    moon = np.array([m.toordinal() for m in moons])
    at = np.clip(np.searchsorted(moon, ords), 1, len(moon) - 1)
    nearest = np.minimum(np.abs(ords - moon[at - 1]), np.abs(moon[at] - ords))
    return nearest <= days


def positions(market, days):
    if not 1 <= days <= 14:
        raise ValueError("days is from 1 to 14")
    index, tradable = market.prices.index, market.tradable
    # 1. the calendar of scheduled sessions, past the market's last session by two months
    calendar = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    # 2. the mean new moons, forty days beyond the calendar on each side
    moons = new_moons(calendar[0].date() - dt.timedelta(days=40), calendar[-1].date() + dt.timedelta(days=40))
    # 3. on each session of the market, whether the next scheduled session is in the new moon's fortnight
    following = calendar[calendar.searchsorted(index, side="right")]
    holding = pd.Series(in_fortnight([d.date() for d in following], moons, days), index=index)
    # 4. the weights: the funds that trade, in equal parts, while holding; nothing otherwise; a
    #    target only on the first session and on the sessions on which it changes
    trading = tradable.astype(float)
    count = trading.sum(axis=1)
    weights = trading.div(count.where(count > 0), axis=0).fillna(0.0)
    weights = weights.mul(holding.astype(float), axis=0)
    change = np.array(weights.ne(weights.shift()).any(axis=1).to_numpy(), dtype=bool)
    change[0] = True
    return weights.where(pd.Series(change, index=index), axis=0)
