# Does last year's best S&P 500 stock keep winning?

A replication and stress test of the experiment in an Instagram reel by "Ricky, the
Steady Investor" (episode 8): every year from 2006 to 2025, put $1,000 into the S&P 500
company with the highest total return in the previous calendar year, and $1,000 into the
S&P 500 itself. Hold everything through August 2026 with dividends reinvested.

The reel reported $357,000 for the picks vs $105,000 for the index, with the pick beating
the index in 11 of 20 years.

## Results

| Variant | Picks | S&P 500 | Years pick won |
|---|---|---|---|
| Reel's own picks, replicated | $352,300 | $104,600 | 10 of 20 |
| Corrected picks (Valero for 2006, NRG for 2018) | $227,600 | $104,600 | 11 of 20 |
| Runner-up picks (#2 of the prior year) | $272,100 | $104,600 | 6 of 20 |

* **The reel's arithmetic is right.** Every figure it quotes reproduces within rounding
  (Apple $141,723 vs "$141,700", Nvidia $87,992 vs "$88,000", Netflix $31,801 vs "$31,800",
  and so on). The total is $352k vs its $357k; the gap is the three delisted names, which
  are approximated here (see caveats).
* **Two of its picks are wrong under its own rule.** By total return, Valero (+128.5%)
  beat Apple (+123.3%) in 2005, and NRG Energy (+133.7%) beat Align (+131.1%) in 2017.
  Swapping them cuts the picks' total from $352k to $228k. It still beats the index.
* **The result is a story about two stocks.** Apple 2006 and Nvidia 2017 are 65% of the
  reel's total. With the corrected picks, Nvidia alone is 39%. The median pick ended up
  worth 0.98x its matching index investment (1.31x corrected), so the *typical* pick did
  not beat the index; a few enormous winners carried the sum.
* **Momentum did not persist over the following year.** Over the purchase year alone the
  pick beat the index in 8 of 17 years with data and had a lower median return (+12.6% vs
  +14.7%). The outperformance comes from multi-year compounding of a handful of names, not
  from prior-year winners continuing to win the next year.
* **Being #1 was not special.** Buying the second-best stock of the prior year instead
  produced $272k, more than the corrected #1 strategy, mostly because Apple then becomes
  the 2006 pick. The whole class of "extreme prior-year winners" happened to contain the
  great tech compounders of 2006 to 2026.

## Follow-up

`strategies/` tests 41 mechanical selection rules (top-N baskets, rank buckets, longer
momentum, volatility and consistency filters, contrarian) on the same universe and scores
them by how often they beat the index. See `strategies/README.md`.

## Method

* `yahoo_prices.txt`: Yahoo Finance daily data (split- and dividend-adjusted closes), first
  trading day of each year and the 31 Aug 2026 close, pulled 4 Sep 2026. The ratio of two
  adjusted closes is a total return with dividends reinvested. The S&P 500 benchmark is the
  total-return index `^SP500TR`.
* `scan_result.txt`: calendar-year total returns for every stock that was in the S&P 500 at
  a year-end 2004 to 2025 (constituent lists from github.com/fja05680/sp500), top 8 per
  year, using Yahoo monthly data. 265 of 956 historical tickers are no longer on Yahoo, so
  this only checks winners among survivors. Six tickers (UVN, CBE, PBG, TIE, MEE, GR, EP)
  now point at unrelated or junk series and were ignored.
* `analysis.py`: the replication and the variants. `results.json` is its output.
* `report.html`: the published write-up.

## Caveats

* Three picks were delisted before Aug 2026 and are modelled from deal terms, not price
  feeds: Family Dollar (acquired by Dollar Tree, 6 Jul 2015, $59.60 cash + 0.2484 DLTR
  shares), XL Group (acquired by AXA, 12 Sep 2018, $57.60 cash) and Cabot Oil & Gas /
  Coterra (merged into Devon Energy, 7 May 2026, 0.70 DVN per share; its adjusted price
  path comes from Stooq). Takeover cash is assumed to sit idle, which matches the reel's XL
  figure. Start prices for FDO and XL are prior year-end closes and their dividends are
  approximate. Together these three positions are under 3% of the total.
* Winners are verified only among stocks Yahoo still carries. A delisted company could
  have been the true winner in some year (2006 and 2007 are the least certain).
* Nvidia's 2017 figure and Apple's 2006 figure use Yahoo's adjusted closes; the reel's
  identical numbers suggest it used the same source.
