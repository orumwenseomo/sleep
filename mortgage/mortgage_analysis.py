#!/usr/bin/env python3
"""
Mortgage interest analysis.

Facts taken from the lender app screenshot (Sep 6, 2026):
  balance        $489,899.43 as of Aug 31, 2026
  payment        $1,193.54 bi-weekly, next due Sep 14, 2026
  rate           3.69% fixed (Canadian convention: compounded semi-annually)
  maturity       Jun 05, 2028, projected balance $465,873.01
  amortization   23 yrs 6 mths remaining

Everything else is derived. Run:  python3 mortgage_analysis.py
"""
from datetime import date, timedelta

BALANCE = 489_899.43
PAYMENT = 1_193.54
RATE = 0.0369
START = date(2026, 8, 31)
FIRST_PAYMENT = date(2026, 9, 14)
MATURITY = date(2028, 6, 5)
PERIOD = timedelta(days=14)
PERIODS_PER_YEAR = 26

# Canadian fixed mortgages: nominal rate compounded semi-annually.
BIWEEKLY_RATE = (1 + RATE / 2) ** (2 / PERIODS_PER_YEAR) - 1
MONTHLY_RATE = (1 + RATE / 2) ** (2 / 12) - 1


def simulate(payment=PAYMENT, extra_per_period=0.0, lump_sums=None,
             balance=BALANCE, stop=None):
    """Run the schedule payment by payment.

    lump_sums: {date: amount} applied on the first payment date on/after that date.
    stop: stop at this date (e.g. MATURITY) or run to payoff.
    Returns dict with totals and a per-payment list.
    """
    lump_sums = dict(lump_sums or {})
    bal = balance
    d = FIRST_PAYMENT
    rows = []
    total_int = total_prin = total_lump = 0.0
    n = 0
    while bal > 0.005:
        if stop and d > stop:
            break
        interest = bal * BIWEEKLY_RATE
        pay = min(payment + extra_per_period, bal + interest)
        principal = pay - interest
        bal -= principal
        # lump sums due on or before this payment date
        lump = 0.0
        for ld in sorted(lump_sums):
            if ld <= d:
                lump += lump_sums.pop(ld)
        lump = min(lump, bal)
        bal -= lump
        n += 1
        total_int += interest
        total_prin += principal
        total_lump += lump
        rows.append((d, pay, interest, principal, lump, bal))
        d += PERIOD
    return dict(n=n, interest=total_int, principal=total_prin, lump=total_lump,
                end_balance=bal, end_date=rows[-1][0] if rows else START,
                rows=rows)


def years(n):
    return n / PERIODS_PER_YEAR


def fmt(x):
    return f"${x:,.0f}"


if __name__ == "__main__":
    print(f"bi-weekly rate {BIWEEKLY_RATE*100:.5f}%  monthly-equiv rate {MONTHLY_RATE*100:.5f}%")
    base = simulate()
    to_mat = simulate(stop=MATURITY)
    print("\n== Calibration against the app ==")
    print(f"remaining amortization: model {years(base['n']):.2f} yrs  (app: 23.5 yrs)")
    print(f"balance at maturity   : model {fmt(to_mat['end_balance'])}  (app: $465,873)")
    print(f"payments to maturity  : {to_mat['n']}  last on {to_mat['end_date']}")

    print("\n== Year-by-year, current plan (12-month windows from first payment) ==")
    print(f"{'window':<28}{'paid':>10}{'interest':>11}{'principal':>11}{'end balance':>14}")
    rows = base["rows"]
    for y in range(0, 4):
        chunk = rows[y * 26:(y + 1) * 26]
        if not chunk:
            break
        paid = sum(r[1] for r in chunk); i = sum(r[2] for r in chunk); p = sum(r[3] for r in chunk)
        print(f"{chunk[0][0]} .. {chunk[-1][0]}  {fmt(paid):>10}{fmt(i):>11}{fmt(p):>11}{fmt(chunk[-1][5]):>14}")
    print(f"\nFirst payment split: interest {rows[0][2]:.2f}  principal {rows[0][3]:.2f}")
    print(f"Interest if you never change anything: {fmt(base['interest'])} over {years(base['n']):.1f} yrs")
    print(f"Interest between now and maturity (Jun 2028) : {fmt(to_mat['interest'])}")

    # Monthly-equivalent payment and accelerated bi-weekly
    n_months = base["n"] * 12 / 26
    monthly = BALANCE * MONTHLY_RATE / (1 - (1 + MONTHLY_RATE) ** (-n_months))
    accel = monthly / 2
    print(f"\nMonthly-equivalent payment {monthly:.2f}; accelerated bi-weekly would be {accel:.2f} (+{accel-PAYMENT:.2f})")

    print("\n== Scenarios: run to payoff (assumes 3.69% held for life for comparability) ==")
    scenarios = {
        "A. Do nothing": dict(),
        "B. Accelerated bi-weekly (+$103/pmt)": dict(payment=accel),
        "C. +10% payment ($1,313)": dict(payment=PAYMENT * 1.10),
        "D. +20% payment ($1,432)": dict(payment=PAYMENT * 1.20),
        "E. Round up to $1,500": dict(payment=1500),
        "F. $5k lump each Jan": dict(lump_sums={date(y, 1, 1): 5000 for y in range(2027, 2060)}),
        "G. $10k lump each Jan": dict(lump_sums={date(y, 1, 1): 10000 for y in range(2027, 2060)}),
        "H. $20k lump each Jan": dict(lump_sums={date(y, 1, 1): 20000 for y in range(2027, 2060)}),
        "I. +20% pmt AND $10k/yr": dict(payment=PAYMENT * 1.20,
                                        lump_sums={date(y, 1, 1): 10000 for y in range(2027, 2060)}),
    }
    print(f"{'scenario':<40}{'payoff':>8}{'total int':>12}{'saved':>11}{'yrs cut':>9}")
    for name, kw in scenarios.items():
        r = simulate(**kw)
        print(f"{name:<40}{years(r['n']):>8.1f}{fmt(r['interest']):>12}"
              f"{fmt(base['interest']-r['interest']):>11}{years(base['n'])-years(r['n']):>9.1f}")

    print("\n== Timing: the same $10,000 lump sum, paid on different dates (interest to payoff) ==")
    for when in [date(2026, 9, 14), date(2027, 1, 1), date(2027, 9, 1), date(2028, 6, 5)]:
        r = simulate(lump_sums={when: 10000})
        print(f"  paid {when}: total interest {fmt(r['interest'])}  saved {fmt(base['interest']-r['interest'])}")

    print("\n== Before the Jun 2028 renewal: what you owe, by scenario (this is what gets repriced) ==")
    for name, kw in scenarios.items():
        r = simulate(stop=MATURITY, **kw)
        print(f"  {name:<40} balance at renewal {fmt(r['end_balance'])}   interest paid to then {fmt(r['interest'])}")

    print("\n== Renewal-rate sensitivity: balance $465,873 renewed for the remaining ~21.7 yrs ==")
    for rr in [0.0299, 0.0369, 0.0449, 0.0499, 0.0549]:
        i_bw = (1 + rr / 2) ** (2 / 26) - 1
        n_left = base["n"] - to_mat["n"]
        pmt = to_mat["end_balance"] * i_bw / (1 - (1 + i_bw) ** (-n_left))
        tot_int = pmt * n_left - to_mat["end_balance"]
        print(f"  renew at {rr*100:.2f}%: bi-weekly {pmt:,.2f}  ({pmt-PAYMENT:+,.0f}/pmt)  interest after renewal {fmt(tot_int)}")
