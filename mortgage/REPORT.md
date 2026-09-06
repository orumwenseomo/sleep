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

## Your 2025 statement (from the app's "Summary of 2025")

| 2025 | amount |
|---|---|
| Interest | $9,929.83 |
| Principal (regular payments) | $6,416.85 |
| Additional principal (your lump sum) | $3,000.00 |
| Taxes / insurance | $0.00 |

Fitting these three numbers to the current balance pins the mortgage down: funded about
June 9, 2025 (3-year term to Jun 5, 2028), original principal about **$508,170**, first
regular payment Jul 7, 2025, with 13 payments plus an interest-adjustment charge in 2025.
The model reproduces the statement to within ~$100 (day-count rounding).

Only 39% of your 2025 regular payments went to principal. Annualised, 2025 interest was
about $18,500, which is why the year-one figure above (~$17,700) is already lower: the
balance is falling.

What the $3,000 did:

| | with the $3,000 | without |
|---|---|---|
| Balance today | $489,899 | $493,024 |
| Balance at Jun 2028 renewal | $465,961 | $469,294 |
| Lifetime interest | $241,590 | $245,901 |
| Payoff | 23.6 yrs | 23.8 yrs |

So $3,000 saves **$4,311** of interest and about 3 months, i.e. every prepaid dollar returns
$1.44 of avoided interest at 3.69% (before any renewal-rate rise, which only makes it better).
Against your ~$50.8k annual room you used 0.6% of it in 2025; the 2026 allowance is untouched.

The app reports "additional principal" per calendar year, which is consistent with CIBC
tracking the 10% allowance per calendar year, but confirm on the prepayment screen.

## CIBC's rules (Fixed Rate Closed mortgage, from cibc.com, checked Sep 2026)

| Privilege | CIBC term |
|---|---|
| Lump sum, no charge | up to **10% of the original principal per year** (some products 15–20%; the app shows yours) |
| Payment increase, no charge | up to **100% of the original regular payment**, any time in the term |
| Lump-sum application | applied straight to principal "if there's no interest owing" (so pay on a payment date) |
| Over the limit | charge = greater of 3 months' interest or the IRD; CIBC uses posted-rate IRD and adds back your original discount, which makes the IRD large |
| Early renewal | as early as **150 days before maturity** (from ~Jan 6, 2028); renewal offer mailed ~30 days out |
| How | CIBC Online Banking / app: "Manage mortgage payments" lets you change the payment and make prepayments yourself |

Whether the 10% resets on the calendar year or on your mortgage anniversary is not stated
publicly and forum reports conflict. The app's prepayment screen shows "available this year";
that number is authoritative.

Original principal is not on the screen. Backing it out (25-yr amortization, ~37 payments made)
gives roughly $508k, so the 10% cap is about **$50,800 per year** and the payment could go as
high as ~$2,387 bi-weekly. Neither cap is binding; cash flow is.

| CIBC-sized scenario | payoff (yrs) | total interest | saved | balance at Jun 2028 renewal |
|---|---|---|---|---|
| J. Payment +50% ($1,790) | 13.3 | $129,165 | $112,425 | $437,622 |
| K. One max lump ($50.8k) Sep 2026 | 20.0 | $179,976 | $61,613 | $411,835 |
| L. Max lump Sep 2026 and Jan 2028 | 16.9 | $135,912 | $105,677 | $360,237 |
| M. Max lump every year | 6.4 | $61,387 | $180,203 | $360,843 |

Market context (Sep 2026): 3-yr fixed ~3.91%, best 5-yr fixed ~4.04%, CIBC prime 4.45%.
Renewing at ~3.9–4.0% costs $14k–$22k more than 3.69% over the remaining amortization
(+$24 to +$39 per payment); the sensitivity table above covers the range.

## Recommended plan

1. Raise the regular payment now in the app. CIBC allows up to double; pick the most you can
   sustain. +20% ($1,432) saves ~$63k; +50% ($1,790) saves ~$112k. A payment increase is
   penalty-free and, unlike a lump sum, needs no discipline after the one change.
2. Lump sums: up to ~$50k per year without charge. Make them on a payment date so they hit
   principal immediately. Earliest is best, but the timing loss is small (~$80 per $10k per
   month of delay); the real loss is not making them.
3. Two windows before renewal: one lump now (2026 allowance), one in early January 2028
   (a fresh allowance if CIBC resets on the calendar year; confirm in the app). That alone
   takes the renewal balance from $466k to $360k.
4. Never exceed the 10% in a term year. The posted-rate IRD at CIBC is punitive; if you have
   more than the cap, hold it until Jun 5, 2028, when you can pay any amount with no charge.
5. From Jan 6, 2028 (150 days out) you can renew early. Get a rate hold from CIBC and two
   competing quotes; at renewal you can also shorten the amortization and switch lenders
   for free. Each 1% on the renewal rate is worth ~$60k.
6. Keep the emergency fund and pay any higher-rate debt first: 3.69% is cheap money. Prepaying
   it beats a savings account earning less than ~3.7% after tax, but not a credit card,
   a car loan, or (usually) unused TFSA/RRSP room if your marginal tax rate is high.

Not modelled: the exact lump-sum tier and reset date of your specific CIBC product (check the
app), property tax or insurance components (the app shows none), and the actual renewal rate.

Sources: cibc.com prepayment, pay-your-mortgage-faster, fixed-rate-closed, FAQ and renewal
pages; ratehub.ca CIBC penalty article; mortgagerenewalhub.ca early-renewal; ratehub.ca
best-mortgage-rates (Sep 2026).
