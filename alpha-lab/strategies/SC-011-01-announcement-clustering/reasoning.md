# SC-011-01 — Macroeconomic announcement clustering: reasoning, not testable

## The theory, and the form its sources give it

SC-011 holds that some calendar effects within the month are not effects of the calendar: important
scheduled macroeconomic releases fall at recurring points of the month, and if prices move on them,
a monthly cycle of news makes a monthly cycle of returns. The turn-of-the-month and intramonth
patterns would then be, in part, the premium for bearing the risk of scheduled announcements, not a
mispricing. Its test is a control: the patterns should shrink or vanish once the announcement days
are accounted for, and should move when the release calendar moves.

Its source, Nikkinen, Sahlström and Äijö (*Journal of Futures Markets*, 2007; the lab read the
abstract only), finds both the turn-of-the-month and the intramonth effects in the returns of the
S&P 100, and finds them gone once the important US macroeconomic announcements are taken into
account. It also proposes a measure of the change in the expected risk premium around announcements,
from option-implied volatilities, which it finds captures the announcements' effects only
incompletely: a secondary check, not the control. A companion paper of 2007 asks the same question
of European stock markets and US announcements. A later study of a Finnish market, by the same
authors with a fourth (Nikkinen, Sahlström, Takko and Äijö, 2009), runs the control following the
2007 papers: announcement-day dummies first, then the residual returns regressed on day-of-month
dummies — dates alone. Its own set of announcements, over 2001–2007, has ten US releases, which the
lab could not verify are the 2007 paper's: the two ISM surveys, the employment report, retail sales,
producer prices, import and export prices, consumer prices, consumer confidence, GDP and the
employment cost index. The theory explains other calendar effects, SC-008's turn of the month among
them; its test is the difference the announcements make to them.

## Why the lab cannot test it

The test needs the dates of the releases, and the lab's data does not hold them. The snapshot holds
daily prices of twenty-two funds and bitcoin, the bill rate and two exchange rates of the Swiss
franc, and nothing else. Nor can the dates be read from prices: choosing days by their large moves
and then finding large moves on them is circular.

**What was considered, and why it does not rescue the test:**

- **Placing the releases by rule.** Some can be: the ISM manufacturing survey comes out on the first
  business day of the month and the services survey on the third, almost without exception; the
  employment report follows the Bureau of Labor Statistics' rule, the third Friday after the week
  that includes the 12th, which places most months, with exceptions — a Thursday release before the
  4 July holiday, and delays by government shutdowns (the September 2013 report, due on 4 October,
  came out on 22 October; the September 2025 report on 20 November, inside the holdout). The others
  — consumer and producer prices, retail sales, GDP, the employment cost index, consumer confidence
  — come out on dates set each year, which no rule gives. And the releases a rule places well cannot
  do the work: a release on a fixed business day coincides with a calendar day, so controlling for
  the ISM surveys is controlling for days +1 and +3 of the month, and cannot tell an announcement
  from the calendar. Only releases whose dates move can separate the two — the theory's third
  refutation — and of those only the employment report follows a rule: one release of ten, on dates
  partly guessed, in a split of about 216 months by where the report falls, too weak to separate
  anything.
- **Testing only the claim that returns are high on announcement days**, as a trade: a rule holding
  equities on those days alone would be a one-day position, and gate 6's check of a day's delay,
  which must keep 70% of the Sharpe ratio, fails such a rule by construction — a failure built in,
  on which the campaign's decisions refuse to spend a trial. It would also be a different claim from
  the control the source runs.
- **Dates copied by hand into a card's parameters**, which a card could carry as a list: data with
  no hash, entered by hand, which the rule of a frozen snapshot exists to prevent.
- **Adding a release calendar to the lab's data**: public calendars exist (the Bureau of Labor
  Statistics' schedules, the release dates of economic series in public archives), but the runbook
  allows an asset or a rate to join the snapshot only before the first card, and the lab's own scope
  provides for theory-specific price data — a stock universe, for the theories that need one — not
  for a calendar of releases. A new kind of data is a decision for the lab's framing, not for a
  card. Recorded here as what would make the theory testable.
- **Reading the question through SC-008**: the turn-of-the-month effect can be tested on prices, and
  SC-008 will be; but whether announcements explain it is SC-011's claim, and needs the dates.

## Status

SC-011 is recorded `not-testable`: its test controls calendar effects for the days of scheduled
macroeconomic announcements, and the lab holds no release calendar; the releases a rule can place
fall on fixed days and cannot separate announcements from the calendar. No card is drawn, and no
trial is spent. It would become testable with a calendar of the major scheduled US releases — for
instance the ten of the 2009 follow-up — added to the lab's data.
