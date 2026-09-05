# Which selection rule wins more often?

Follow-up to the replication in the parent folder. The reel's rule (buy last year's single
best S&P 500 stock) beat the index in about half of the years. This study asks whether any
simple, mechanical rule built from the same information (prior returns and volatility of
S&P 500 constituents) beats the index more consistently.

## Setup

* Universe: stocks in the S&P 500 at the previous year-end (constituent history from
  github.com/fja05680/sp500), restricted to tickers Yahoo Finance still serves: 279 names in
  2006 rising to 485 in 2025. Prices are monthly split- and dividend-adjusted closes.
* Selection at the start of each year 2006 to 2025 uses only data through the prior December.
  Baskets are equal-weight.
* Two evaluations: (1) hold one year, compare the basket's total return with the S&P 500
  total-return index, count the years the basket wins, and compound the annual returns;
  (2) the reel's framing, $1,000 per year held to 31 Aug 2026.
* Null distribution: 800 random equal-weight baskets of 1, 3 and 10 stocks drawn from the same
  universe each year. A random 3-stock basket beats the index in 9.5 of 20 years on average
  (sd 2.2); 14 or more wins happens 3.4% of the time, 15 or more 1%.

Files: `strat.py` (rules and evaluation), `fetch_monthly.py` (data download; needs a
network path to Yahoo Finance), `strat_results.json` (all results), `report.html` (write-up).

## Headline results (1-year hold, 20 purchase years)

| Rule | Years beat index | Median excess | CAGR (index 11.0%) | Hold-to-2026 wins |
|---|---|---|---|---|
| Reel: #1 of prior year | 10 | -1.3% | 19.4% | 12 |
| Top 3 of prior year, equal-weight | **14** | +12.5% | 20.6% | 15 |
| Top 3 by 12-1 momentum | **14** | +10.1% | 17.2% | 14 |
| #3 of prior year (single stock) | 13 | +19.0% | 23.3% | 13 |
| 3-year momentum #1 | 13 | +26.0% | 20.9% | 12 |
| Top 10 of prior year | 12 | +3.7% | 10.2% | 16 |
| Middle 50 / ranks 101-200 | 12 | +1.2% | ~11% | 7 / 2 |
| Beat index last year, lowest-vol 25 | 11 | +1.8% | 11.2% | 5 |
| Lowest-vol 10 | 10 | 0.0% | 9.0% | 3 |
| Bottom 10 | 9 | -4.7% | 7.7% | 12 |
| Worst 1 | 9 | -18.8% | -23.7% | 5 |
| All constituents equal-weight | 9 | -0.2% | 10.9% | 11 |

Full table for all 41 rules in `strat_results.json`.

## What it says

1. **No rule wins reliably.** The best hit rate is 14 of 20, and two closely related rules
   share it. With 41 rules tried, a 14 by luck alone was more likely than not.
2. **A small basket of prior-year winners is the most consistent thing here.** Going from the
   #1 stock to the top 3 to the top 10 moves the hit rate from 10 to 14 to 12, the median
   excess from -1% to +12% to +4%, and the hold-to-2026 wins from 12 to 15 to 16. The top-3
   basket compounded at 20.6% a year against 11.0% for the index.
3. **The edge is regime-dependent.** The top-3 basket beat the index in 4 of 9 years from 2006
   to 2014 and 10 of 11 from 2015 to 2025. Its bad years are bad: -56% in 2008, 36 points
   behind the index in 2009, 35 behind in 2011.
4. **Single-rank picks are noise.** #1, #2, #3, #5 and #10 of the prior year won 10, 7, 13, 6
   and 7 years; #3's record rests on Nvidia in 2016 (+215 points of excess).
5. **Defensive filters raise the hit rate only to about 11 and give up the upside.** Low-vol and
   "beat the index but low-vol" baskets win in down years (2008, 2011, 2022) and lose in up
   years; on a hold-to-2026 basis they beat the index twin in 1 to 5 years out of 20.
6. **Contrarian rules are coin flips with fat tails.** The worst stock of the prior year won 9
   years yet compounded at -24% a year. Survivorship bias flatters these rules most: the names
   that went to zero (Lehman, Washington Mutual, Circuit City) are missing from the data.
7. **The base rate is falling.** The share of constituents beating the cap-weighted index was
   about 50% through 2022 and 28 to 31% in 2023 to 2025, when a handful of mega-caps drove the
   index. Any equal-weight rule starts each recent year at a disadvantage.

## Caveats

Survivorship (about 270 delisted tickers missing), 41 rules tested on 20 years, no
transaction costs or taxes (annual turnover is 100% for most rules), equal-weight baskets,
and rules chosen with hindsight of what the 2010s rewarded. Treat every number as descriptive
of 2006 to 2026, not predictive.
