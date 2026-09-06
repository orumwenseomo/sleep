# Mortgage interest analysis (as of Sep 6, 2026)

Source: lender app screenshot. Balance $489,899.43 (Aug 31, 2026), $1,193.54 bi-weekly,
3.69% fixed, matures Jun 05, 2028 (projected balance $465,873.01), 23 yrs 6 mths left.
Model: Canadian convention, 3.69% compounded semi-annually -> 0.14073% per bi-weekly period.
Calibration: model gives 23.6 yrs and $465,961 at maturity (app: 23.5 yrs / $465,873).

Reproduce with `python3 mortgage_analysis.py`.

## What you pay now

| | per payment | per year (26 pmts) |
|---|---|---|
| Payment | $1,193.54 | $31,032 |
| Interest (first payment) | $689.43 | ~$17,700 |
| Principal (first payment) | $504.11 | ~$13,300 |

57% of every payment is interest today. Year by year on the current plan:

| 12-month window | interest | principal | balance at end |
|---|---|---|---|
| Sep 2026 – Aug 2027 | $17,692 | $13,340 | $476,559 |
| Sep 2027 – Aug 2028 | $17,195 | $13,837 | $462,722 |
| Sep 2028 – Aug 2029 | $16,680 | $14,352 | $448,370 |
| Sep 2029 – Aug 2030 | $16,145 | $14,887 | $433,484 |

Lifetime interest if nothing changes (and 3.69% held): **$241,590** over 23.6 years.
Interest between now and the Jun 2028 renewal: **$30,964**.

## Scenarios (3.69% held for life, for comparability)

| Scenario | payoff (yrs) | total interest | interest saved | years cut |
|---|---|---|---|---|
| A. Do nothing | 23.6 | $241,590 | – | – |
| B. Accelerated bi-weekly ($1,293.89, +$100) | 20.8 | $210,337 | $31,253 | 2.7 |
| C. Payment +10% ($1,313) | 20.4 | $205,336 | $36,254 | 3.2 |
| D. Payment +20% ($1,432) | 18.0 | $178,764 | $62,826 | 5.6 |
| E. Round payment up to $1,500 | 16.8 | $166,592 | $74,997 | 6.7 |
| F. $5k lump sum every January | 18.8 | $187,549 | $54,041 | 4.8 |
| G. $10k lump sum every January | 15.6 | $153,430 | $88,159 | 8.0 |
| H. $20k lump sum every January | 11.7 | $112,477 | $129,113 | 11.9 |
| I. Payment +20% and $10k/yr lump | 13.1 | $125,698 | $115,892 | 10.5 |

## Timing of a lump sum

The same $10,000 paid on different dates (interest saved over the life of the loan):

| paid on | saved |
|---|---|
| Sep 14, 2026 (next payment) | $13,336 |
| Jan 1, 2027 | $13,078 |
| Sep 1, 2027 | $12,509 |
| Jun 5, 2028 (renewal) | $11,923 |

Every month of delay costs roughly $80 of future interest per $10,000. Earlier is always better,
but the difference between "now" and "next January" is small; the difference between
"now" and "never" is what matters.

## The renewal on Jun 5, 2028 is the biggest lever

Your rate is fixed only until then. About $466k renews at whatever the market rate is.

| renew at | new bi-weekly | change | interest after renewal |
|---|---|---|---|
| 2.99% | $1,117 | −$77 | $167,305 |
| 3.69% | $1,193 | $0 | $210,678 |
| 4.49% | $1,284 | +$90 | $262,078 |
| 4.99% | $1,342 | +$149 | $295,160 |
| 5.49% | $1,402 | +$208 | $328,951 |

Each 1% on the renewal rate is worth roughly $60k of interest over the remaining amortization.
Nothing you can do with prepayments this term is as large as the rate you sign at renewal.

## Recommended plan

1. Confirm your prepayment privileges in the app / mortgage document. Most Canadian lenders
   allow, per year and penalty-free: a payment increase of 10–20%, lump sums of 10–20% of the
   original principal, and "double-up" payments. Anything beyond that triggers a penalty
   (on a fixed rate: the greater of 3 months' interest or the IRD). Stay inside the privileges.
2. Raise the regular payment now, by the max allowed or to a round number you can sustain
   ($1,432 = +20%; $1,500 if allowed). This is the cheapest habit: it needs no discipline
   after the one call/click and saves $63k–$75k.
3. Put lump sums in as early in each year as you can, on a payment date so they apply
   immediately. Privileges usually reset on a calendar year or anniversary year: check
   which, because a lump in late Dec 2026 and another in early Jan 2027 can use two years'
   allowance in two weeks.
4. Before Jun 5, 2028: use the remaining allowance, then at renewal you can pay any amount
   with no penalty. That is also the one moment to shorten the amortization (e.g. to 20 yrs)
   and to switch lenders if another offers a better rate; you are not locked in.
5. At renewal, shop the rate 120 days out. Rate holds are free. The table above shows why
   this one number dominates everything else.
6. Keep the emergency fund and any higher-rate debt first: 3.69% is cheap money. Prepaying
   it beats a savings account earning less than ~3.7% after tax, but not a credit card,
   a car loan, or (usually) an unused TFSA/RRSP room if your marginal tax rate is high.

Not modelled: the payment/lump-sum caps of your specific lender, prepayment penalties,
property tax or insurance components (the app shows none), and the actual renewal rate.
