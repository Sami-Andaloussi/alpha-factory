"""SC-023-01, the same calendar month across assets (build-plan.md): at the close of the last
session before each calendar month m, placed on the New York Stock Exchange's calendar of scheduled
sessions derived from its holiday rules alone, hold in equal parts the `top` assets whose mean
residual return in month m over the previous `years` years, beyond their beta to the universe's
equal-weighted average estimated over months m - 12 * years to m - 2, is highest."""
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


def monthly_returns(prices) -> pd.DataFrame:
    """Each calendar month's return, from the close on the market's last session of the month before
    to the close on its last session of the month; NaN where either close is missing (step 2)."""
    month = prices.index.to_period("M")
    last = prices.groupby(month).tail(1)
    last.index = last.index.to_period("M")
    if len(last) > 1 and not (np.diff(last.index.asi8) == 1).all():
        raise ValueError("a calendar month without a session")
    return last / last.shift(1) - 1.0


def positions(market, years, top):
    if years < 1 or top < 1:
        raise ValueError("years and top are 1 at least")
    prices, tradable = market.prices, market.tradable
    index = prices.index
    # 1. the decision sessions: the next scheduled session falls in a new calendar month m
    sessions = scheduled_sessions(index[0] - pd.Timedelta(days=45), index[-1] + pd.Timedelta(days=62))
    following = sessions[sessions.searchsorted(index, side="right")]
    decide = (following.year * 12 + following.month) != (index.year * 12 + index.month)
    # 2. the monthly returns, raw, and the average's: the mean of those known in each month
    returns = monthly_returns(prices)
    average = returns.mean(axis=1)
    weights = pd.DataFrame(np.nan, index=index, columns=prices.columns)
    for day, target in zip(index[decide], following[decide]):
        m = pd.Period(target, freq="M")
        # 3. the window: months m - 12 * years to m - 2, the month in progress left out
        window = pd.period_range(m - 12 * years, m - 2, freq="M")
        block = returns.reindex(window)
        market_month = average.reindex(window)
        # 4. the ranking: the assets that trade and whose returns in every month of the window are known
        ranked = tradable.loc[day] & block.notna().all() & market_month.notna().all()
        row = pd.Series(0.0, index=prices.columns)
        if ranked.any():
            y = block.loc[:, ranked]
            x = market_month - market_month.mean()
            beta = (y - y.mean()).mul(x, axis=0).sum() / (x * x).sum()
            residual = y - np.outer(market_month.to_numpy(), beta.to_numpy())
            signal = residual.loc[window.month == m.month].mean()
            # 5. the targets: the `top` highest in equal parts, ties broken by the universe's order
            chosen = signal.sort_values(ascending=False, kind="stable").index[:top]
            row[chosen] = 1.0 / len(chosen)
        weights.loc[day] = row
    return weights
