#!/usr/bin/env python3
"""
Replicates and stress-tests the "buy last year's best S&P 500 stock" experiment
from the Instagram reel (Ricky, the Steady Investor, episode 8).

Rules of the experiment (from the reel's transcript):
  * For each purchase year 2006..2025, pick the S&P 500 company with the highest
    total return in the previous calendar year.
  * On the first trading day of the purchase year invest $1,000 in that stock and
    $1,000 in the S&P 500. Reinvest dividends. Hold everything through Aug 2026.

Data: Yahoo Finance daily adjusted closes (split + dividend adjusted, so the ratio
of two adjusted closes is a total return with dividends reinvested), extracted in
yahoo_prices.txt. Three picks were delisted before Aug 2026 and are modelled from
documented deal terms (see DELISTED below).
"""
import json, sys
from collections import defaultdict

# ---------------------------------------------------------------- load data
first = defaultdict(dict)   # ticker -> year -> (date, close, adjclose) on first trading day
yend  = defaultdict(dict)   # ticker -> year -> adjclose on last trading day
end   = {}                  # ticker -> (date, close, adjclose) on 2026-08-31
for line in open("yahoo_prices.txt"):
    kind, t, *rest = line.split()
    if kind == "F":
        for item in rest:
            y, d, c, a = item.split(":"); first[t][int(y)] = (d, float(c), float(a))
    elif kind == "Y":
        for item in rest:
            y, a = item.split(":"); yend[t][int(y)] = float(a)
    elif kind == "E":
        d, c, a = rest[0].split(":"); end[t] = (d, float(c), float(a))

SPX = "^SP500TR"   # S&P 500 total-return index (dividends reinvested)
END_DATE = end[SPX][0]

# ------------------------------------------------ the reel's picks, by purchase year
# (winner of the previous calendar year). Verified against the constituent scan in
# scan_result.txt where Yahoo still has data; see README for the three delisted names.
PICKS = {
    2006: ("AAPL", "Apple"),
    2007: ("ATI",  "Allegheny Technologies"),
    2008: ("NOV",  "National Oilwell Varco"),
    2009: ("FDO",  "Family Dollar"),
    2010: ("XL",   "XL Capital"),
    2011: ("NFLX", "Netflix"),
    2012: ("COG",  "Cabot Oil & Gas (later Coterra)"),
    2013: ("PHM",  "PulteGroup"),
    2014: ("NFLX", "Netflix"),
    2015: ("LUV",  "Southwest Airlines"),
    2016: ("NFLX", "Netflix"),
    2017: ("NVDA", "Nvidia"),
    2018: ("ALGN", "Align Technology"),
    2019: ("AMD",  "AMD"),
    2020: ("AMD",  "AMD"),
    2021: ("TSLA", "Tesla"),
    2022: ("DVN",  "Devon Energy"),
    2023: ("OXY",  "Occidental Petroleum"),
    2024: ("NVDA", "Nvidia"),
    2025: ("PLTR", "Palantir"),
}

# What the reel itself reported, for comparison ($, rounded as spoken).
REEL = {
    2006: (141700, 9000), 2008: (400, None), 2010: (3600, 9200), 2011: (31800, None),
    2014: (15600, None), 2016: (7400, None), 2017: (88000, None), 2019: (25000, None),
    2020: (9600, None), 2021: (1500, 2300),
}
REEL_TOTAL = (357000, 105000)

# ------------------------------------------------------------- delisted picks
# Modelled from documented deal terms. Start prices are the prior year-end closes
# (first-trading-day closes were not available for delisted tickers), dividends are
# approximate per-share totals from the companies' dividend histories. Cash received
# in a takeover is assumed to sit idle (no reinvestment), which matches the reel's
# XL figure; "reinvest" variants put takeover cash into the S&P 500 TR index instead.
def spx_growth(y0, y1=None):
    """Growth of $1 in the S&P 500 TR from first trading day of y0 to END_DATE (or to a
    given (year, adjclose) point)."""
    return end[SPX][2] / first[SPX][y0][2]

def spx_from_level(level):
    return end[SPX][2] / level

# S&P 500 TR index level on the takeover dates (from the daily series; approximated by
# interpolation between year-start levels is NOT good enough, so these were read from
# the Yahoo daily series: 2015-07-06 and 2018-09-12).
SPX_2015_07_06 = 3922.0   # approx S&P 500 TR close 6 Jul 2015
SPX_2018_09_12 = 5876.0   # approx S&P 500 TR close 12 Sep 2018

def value_FDO(reinvest=False):
    # Family Dollar: bought at $26.07 (31 Dec 2008 close). Dividends 2009-H1 2015 ~ $5.60/sh.
    # 6 Jul 2015: $59.60 cash + 0.2484 Dollar Tree (DLTR) shares per FDO share. DLTR pays no dividend.
    sh = 1000 / 26.07
    dltr = sh * 0.2484 * end["DLTR"][2]
    cash = sh * (59.60 + 5.60)
    if reinvest: cash = sh * 59.60 * spx_from_level(SPX_2015_07_06) + sh * 5.60
    return cash + dltr

def value_XL(reinvest=False):
    # XL Capital / XL Group: bought at $18.33 (31 Dec 2009 close). Dividends 2010-Q3 2018 ~ $5.54/sh.
    # 12 Sep 2018: acquired by AXA for $57.60 cash per share.
    sh = 1000 / 18.33
    cash = sh * (57.60 + 5.54)
    if reinvest: cash = sh * 57.60 * spx_from_level(SPX_2018_09_12) + sh * 5.54
    return cash

# Cabot Oil & Gas -> Coterra (2021) -> merged into Devon Energy on 7 May 2026 at 0.70 DVN
# per share. Stooq keeps the split- and dividend-adjusted series under CTRA: 15.4923 on
# 3 Jan 2012 (first trading day) and 32.56 on 6 May 2026 (its last session). From there the
# position is 0.70 Devon shares per Coterra share, valued at Devon's 31 Aug 2026 close.
CTRA_STOOQ_2012_01_03 = 15.4923
CTRA_STOOQ_2026_05_06 = 32.56

def value_COG():
    growth_to_merger = CTRA_STOOQ_2026_05_06 / CTRA_STOOQ_2012_01_03
    dvn_after = 0.70 * end["DVN"][2] / CTRA_STOOQ_2026_05_06
    return 1000 * growth_to_merger * dvn_after

DELISTED = {"FDO": value_FDO, "XL": value_XL, "COG": value_COG}

# Corrected picks: where Yahoo total-return data shows a different winner than the reel used.
#   2005: Valero +128.5% beat Apple +123.3%   -> the 2006 purchase should be VLO
#   2017: NRG Energy +133.7% beat Align +131.1% -> the 2018 purchase should be NRG
CORRECTED = dict(PICKS); CORRECTED[2006] = ("VLO", "Valero Energy"); CORRECTED[2018] = ("NRG", "NRG Energy")

# Runner-up strategy: buy the SECOND-best stock of the prior year (among names Yahoo still
# carries; where the true #1 was delisted the survivor #1 stands in). Tests whether "#1"
# is special or whether any extreme prior-year winner would have done.
RUNNER_UP = {
    2006: ("AAPL", "Apple"), 2007: ("TEX", "Terex"), 2008: ("AMZN", "Amazon"),
    2009: ("HRB", "H&R Block"), 2010: ("THC", "Tenet Healthcare"), 2011: ("FFIV", "F5 Networks"),
    2012: ("ISRG", "Intuitive Surgical"), 2013: ("WHR", "Whirlpool"), 2014: ("BBY", "Best Buy"),
    2015: ("EW", "Edwards Lifesciences"), 2016: ("AMZN", "Amazon"), 2017: ("OKE", "ONEOK"),
    2018: ("ALGN", "Align Technology"), 2019: ("FTNT", "Fortinet"), 2020: ("LRCX", "Lam Research"),
    2021: ("ETSY", "Etsy"), 2022: ("MRNA", "Moderna"), 2023: ("XOM", "Exxon Mobil"),
    2024: ("META", "Meta Platforms"), 2025: ("VST", "Vistra"),
}

# ----------------------------------------------------------------- main run
def run(picks=PICKS, verbose=True):
    rows = []
    for y, (t, name) in sorted(picks.items()):
        spx_val = 1000 * end[SPX][2] / first[SPX][y][2]
        if t in DELISTED:
            val = DELISTED[t](); approx = True
        else:
            val = 1000 * end[t][2] / first[t][y][2]; approx = False
        # forward returns of the pick vs the index over the purchase year only
        if t in DELISTED:
            fwd1 = None
        else:
            fwd1 = yend[t][y] / first[t][y][2] - 1
        spx1 = yend[SPX][y] / first[SPX][y][2] - 1
        rows.append(dict(year=y, ticker=t, name=name, value=val, spx=spx_val, approx=approx,
                         fwd1=fwd1, spx1=spx1, prev=None))
    return rows

def fmt(v): return f"${v:,.0f}"

if __name__ == "__main__":
    rows = run()
    tot = sum(r["value"] for r in rows); tot_spx = sum(r["spx"] for r in rows)
    wins = sum(r["value"] > r["spx"] for r in rows)
    print(f"Hold-to-{END_DATE} results, $1,000 per year, dividends reinvested\n")
    print(f"{'Buy':>4} {'Pick':<6} {'Pick value':>12} {'S&P 500':>10} {'Beat?':>5} {'Reel said':>18}   {'Yr-1 pick':>9} {'Yr-1 S&P':>9}")
    for r in rows:
        reel = REEL.get(r["year"]); rs = ""
        if reel: rs = f"{fmt(reel[0])}" + (f" / {fmt(reel[1])}" if reel[1] else "")
        f1 = f"{r['fwd1']*100:+.0f}%" if r["fwd1"] is not None else "n/a"
        print(f"{r['year']:>4} {r['ticker']:<6} {fmt(r['value']):>12}{'~' if r['approx'] else ' '}{fmt(r['spx']):>10} {'yes' if r['value']>r['spx'] else 'no':>5} {rs:>18}   {f1:>9} {r['spx1']*100:+8.0f}%")
    print(f"\nTOTAL  picks {fmt(tot)}  vs S&P {fmt(tot_spx)}   (reel: {fmt(REEL_TOTAL[0])} vs {fmt(REEL_TOTAL[1])})")
    print(f"Picks beat the index in {wins} of {len(rows)} years (reel: 11 of 20)")
    top2 = sorted(rows, key=lambda r: -r["value"])[:2]
    print(f"Top two picks: " + ", ".join(f"{r['year']} {r['ticker']} {fmt(r['value'])}" for r in top2) + f" = {fmt(sum(r['value'] for r in top2))}")
    rest = [r for r in rows if r not in top2]
    print(f"Without them: picks {fmt(sum(r['value'] for r in rest))} vs S&P {fmt(sum(r['spx'] for r in rest))}")
    import statistics
    ratios = [r["value"]/r["spx"] for r in rows]
    print(f"Median pick/S&P ratio: {statistics.median(ratios):.2f}x ; mean {statistics.mean(ratios):.2f}x")
    f1 = [r for r in rows if r["fwd1"] is not None]
    print(f"\nNext-year only (buy Jan, sell Dec of purchase year): pick beat S&P in {sum(r['fwd1']>r['spx1'] for r in f1)} of {len(f1)} years with data")
    print(f"  median pick next-year return {statistics.median(r['fwd1'] for r in f1)*100:+.1f}%  vs S&P {statistics.median(r['spx1'] for r in f1)*100:+.1f}%")
    print(f"  mean   pick next-year return {statistics.mean(r['fwd1'] for r in f1)*100:+.1f}%  vs S&P {statistics.mean(r['spx1'] for r in f1)*100:+.1f}%")
    def summarize(label, rs):
        t=sum(r["value"] for r in rs); ts=sum(r["spx"] for r in rs); w=sum(r["value"]>r["spx"] for r in rs)
        f=[r for r in rs if r["fwd1"] is not None]
        print(f"\n== {label}: picks {fmt(t)} vs S&P {fmt(ts)} ({t/ts:.2f}x); beat index {w}/{len(rs)} years; "
              f"median ratio {statistics.median(r['value']/r['spx'] for r in rs):.2f}x; "
              f"next-year wins {sum(r['fwd1']>r['spx1'] for r in f)}/{len(f)}, median next-year {statistics.median(r['fwd1'] for r in f)*100:+.1f}% vs S&P {statistics.median(r['spx1'] for r in f)*100:+.1f}%")
        big=max(rs,key=lambda r:r["value"]); print(f"   biggest: {big['year']} {big['ticker']} {fmt(big['value'])} = {big['value']/t*100:.0f}% of total")
        return rs
    corrected = summarize("Corrected picks (VLO 2006, NRG 2018)", run(CORRECTED))
    for r in corrected:
        if r["ticker"] in ("VLO","NRG"): print(f"   {r['year']} {r['ticker']}: {fmt(r['value'])} vs S&P {fmt(r['spx'])}, next-year {r['fwd1']*100:+.0f}% vs {r['spx1']*100:+.0f}%")
    runner = summarize("Runner-up picks (#2 of prior year)", run(RUNNER_UP))
    # sensitivity: takeover cash reinvested in the index instead of idle
    alt = dict(FDO=value_FDO(True), XL=value_XL(True))
    print(f"\nIf takeover cash had been reinvested in the S&P 500: FDO {fmt(alt['FDO'])}, XL {fmt(alt['XL'])}")
    json.dump({"end_date": END_DATE, "reel": rows, "corrected": corrected, "runner_up": runner,
               "reel_claimed": {"total": REEL_TOTAL, "by_year": REEL}}, open("results.json", "w"), indent=1)
