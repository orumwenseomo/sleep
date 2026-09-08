# The Next Nvidia: A Deep-Dive Search

*Research memo, September 8, 2026. All figures are as of the dates cited. This is research, not investment advice.*

---

## 0. Bottom line

**Primary pick: Credo Technology (CRDO).** It is the closest live match to what Nvidia looked like before its 2023 to 2026 run: a category creator with Nvidia-grade margins (68% gross, 48% operating, ~50% net), seven straight quarters of triple-digit growth, a fiscal-2027 guide of more than 85% growth, and a market cap of only about $32B after a 20% post-earnings drop that took its forward P/E down to roughly 22 to 27x. The market is pricing a slowdown that management's guidance does not contain. That gap between earnings trajectory and multiple is the single most reliable pre-blowup signature Nvidia showed.

**Runner-up: Lumentum (LITE).** The "bottleneck" pick. Lumentum controls 50 to 60% of the 200G-per-lane EML lasers every 1.6T optical link needs, its operating margin expanded roughly 2,100 basis points in a year, and Nvidia has started paying to lock up laser supply the same way it locked up memory. Bigger ($79B) and dearer than Credo, but the closest thing to "memory in 2025" that has not yet fully repriced.

**Third: Astera Labs (ALAB).** The "paradigm" pick. If custom accelerators (Broadcom's $230B fiscal-2028 AI revenue outlook, ASIC shipments tripling by 2027) become half the market, every non-Nvidia rack needs a scale-up fabric, and Astera's Scorpio X switch is the merchant answer. Fastest sequential growth of any name studied (Q3 guide +40% quarter on quarter) but at 120x forward earnings it needs everything to go right.

**What has already blown up and should not be called "next":** Micron (+225% YTD, ~$1T cap, quarterly revenue +346%), Sandisk (+536% YTD), SK hynix (76% operating margin), Dell (+306% YTD), Super Micro, Bloom Energy (9x since July 2025), Nebius (+454% revenue growth), Marvell (+179% YTD). These are the 2025 to 2026 blowups. Some may keep going, but the asymmetric setup is gone.

---

## 1. What "blowing up like Nvidia" actually was

Nvidia's run from the October 2022 low is roughly 20x in price and about 19x in market cap (sub-$300B to $5.56T on September 4, 2026). The important thing is *how*: earnings grew faster than the stock, so the multiple compressed while the price went vertical.

| Fiscal year (ends late Jan) | Revenue | YoY | Data center | GAAP gross margin | Net income |
|---|---|---|---|---|---|
| FY2023 | $26.97B | flat | $15.0B | ~57% (gaming inventory charges) | ~$4.4B |
| FY2024 | $60.9B | +126% | $47.5B | ~73% | ~$30B |
| FY2025 | $130.5B | +114% | $115.2B | ~75% | ~$73B |
| FY2026 | $215.9B | +65% | $197.3B | 71.1% | $120.1B |
| Q1 FY2027 | $81.6B | +85% | $75.2B | 74.9% | $58.3B |
| Q2 FY2027 (reported Aug 26, 2026) | $96.2B | +106% | $89.0B | 75.0% | not disclosed in excerpt (GAAP EPS $2.46) |

Sources: [SEC 8-K Q4 FY23](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000014/q4fy23pr.htm), [Nvidia Q4 FY24](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2024), [Nvidia Q4 FY25](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/), [Nvidia Q4 FY26](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026), [SEC 8-K Q1 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm), [SEC 8-K Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm). FY23 to FY25 margin and net income figures are from memory and unverified this session; FY26 onward are sourced.

**Market cap milestones:** $1T May 30, 2023; $2T Feb 23, 2024; $3T Jun 5, 2024; $4T Jul 9, 2025; $5T Oct 29, 2025; $5.56T on Sep 4, 2026 at about $230 per share ([CNBC](https://www.cnbc.com/2025/07/09/nvidia-4-trillion.html), [NBC](https://www.nbcnews.com/business/markets/nvidia-record-five-trillion-ai-bubble-rcna240447), [Capital.com](https://capital.com/en-int/markets/shares/nvidia-corp-share-price/market-cap)).

**Multiple compression while the price rose:** trailing P/E peaked near 248x in mid-2023 and sits near 32x in 2026; forward P/E was 52x in June 2023 and is now roughly 17 to 25x depending on the source ([TIKR](https://www.tikr.com/blog/nvidias-p-e-ratio-current-levels-historical-trends-and-outlook), [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/NVDA), [Motley Fool, Jul 11 2026](https://www.fool.com/investing/2026/07/11/nvidias-forward-pe-has-actually-fallen-as-its-stoc/)).

### The five signatures

Pulling the story apart, five things were visible in 2022 and early 2023 to anyone who looked:

1. **Sole supplier of the binding constraint.** Nvidia had roughly 98% of AI accelerators in 2023 with CUDA as the lock. When ChatGPT flipped demand in November 2022, there was one place to buy.
2. **Supply could not respond for two years.** CoWoS packaging and HBM, not demand, set Nvidia's revenue. Supply-constrained companies get pricing power, and pricing power shows up as gross margin: 57% to 75%.
3. **Customers' capex plans were public and rising.** Big-four hyperscaler capex went from about $410B in 2025 to about $725B planned for 2026, and Nvidia now expects more than $1T of hyperscaler data-center capex in 2027 ([Yahoo Finance](https://finance.yahoo.com/sectors/technology/article/meta-microsoft-amazon-and-alphabet-are-about-to-spend-a-shocking-amount-of-money-to-dominate-the-ai-era-115359575.html), [ValueAdd VC](https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race)).
4. **Consensus lagged for eight-plus quarters.** The May 2023 guide of $11B against roughly $7.2B expected was the first of many. Estimates chased results, which is why the multiple compressed.
5. **The starting base was small enough.** Sub-$300B allowed a 20x. A $2T company cannot do that.

Any "next Nvidia" candidate should be tested against all five, not just the first.

---

## 2. The September 2026 backdrop

**Nvidia's own blowup is still accelerating.** Q2 FY27 revenue of $96.2B was up 106% year over year. Q3 guidance is $108B. Management gave a preliminary fiscal-2028 growth guide of about 70% and called the outlook supply-constrained with demand "much higher" than it can deliver. Vera Rubin is about 20% of data-center revenue this quarter, and AWS has committed to 2 million Nvidia GPUs ([SEC 8-K Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm), [S&P Global preview](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/nvidia-earnings-preview-q2-2027)).

**The bottleneck has already migrated once, to memory.** Nvidia's own gross margin is guided to bottom at 71 to 72% in Q4 FY27 "partially due to memory prices," and its supply commitments more than doubled from $119B to $279B in one quarter, "primarily related to the procurement of memory." Jensen Huang's phrase: "Memory scarcity today is being driven in large part by the AI buildout itself." The S&P 500's top five year-to-date performers through September 4 are Sandisk (+536%), Moderna (+399%), Dell (+306%), Micron (+225%) and Seagate (+184%); three of five are memory or storage ([Investing.com](https://www.investing.com/analysis/the-sp-500-3-bestperforming-stocks-so-far-in-2026-200676716)).

Micron's fiscal Q3 2026 (reported June 24) shows what a completed blowup looks like: revenue $41.5B (+346%), gross margin 84.9%, guidance for $50B next quarter at an 86% margin, 16 strategic customer agreements worth about $100B of contracted minimum revenue, market cap through $1T ([SEC exhibit](https://www.sec.gov/Archives/edgar/data/723125/000072312526000013/a2026q3ex991-pressrelease.htm), [CNBC](https://www.cnbc.com/2026/06/24/micron-mu-earnings-report-q3-2026.html)). TrendForce expects DRAM to stay tight through 2027 with HBM contract prices potentially doubling in 2027, and SK hynix's chairman has said supply may run about 20% below demand through 2030 ([TrendForce, Jun 2 2026](https://www.trendforce.com/presscenter/news/20260602-13074.html), [TrendForce, Aug 4 2026](https://www.trendforce.com/presscenter/news/20260804-13166.html)). That is bullish for memory earnings, but the asymmetric *setup* is gone: consensus already models fiscal-2027 Micron EPS above $100, the CEO has sold more than $140M of stock since May, and Samsung is targeting HBM leadership by 2027.

**Capex is now externally financed.** Alphabet raised $84.75B of equity in June 2026 and hyperscalers are tapping debt as capex outruns free cash flow ([FactSet](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow)). 2027 capex estimates sit between $935B and $1.01T for the big four. This is the main systemic risk for every name below.

**The private giants are arriving.** SpaceX (with xAI) listed June 12, 2026 at about $1.8T and trades near its IPO price; Cerebras listed May 14 at $56B fully diluted and is now near $50B; Anthropic filed confidentially on June 1 at a reported $965B valuation; OpenAI is pre-filing at about $852B. These absorb capital that used to chase public "next Nvidia" proxies ([CNBC](https://www.cnbc.com/2026/06/11/spacex-raises-75-billion-in-record-setting-ipo-ahead-of-nasdaq-debut.html), [CNBC](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html), [Futurum](https://futurumgroup.com/insights/anthropic-files-for-ipo-looking-to-beat-openai-to-the-punch/)).

---

## 3. Screening framework

Each candidate is scored 0 to 5 on six criteria derived from the five signatures plus a valuation check. A 30 is a perfect Nvidia-2022 analogue.

| # | Criterion | What earns a 5 |
|---|---|---|
| A | Bottleneck ownership | Sole or clearly dominant supplier of something the AI buildout cannot proceed without |
| B | Demand visibility | Multi-year backlog, long-term agreements, or "supply-constrained" language from management |
| C | Margin trajectory | Gross margin above 60% *and* operating margin still expanding |
| D | Growth | Revenue growth above 80% with guidance that holds it |
| E | Headroom | Market cap under $50B (a 10x is arithmetically plausible); 0 above $1T |
| F | Multiple vs growth | Forward P/E below growth rate; the market is not yet believing the guide |

---

## 4. The candidate universe, by layer of the stack

### 4a. Compute (GPU, custom ASIC, foundry)

| Ticker | Latest quarter | Growth | AI line | Margin | Market cap | Valuation | Verdict |
|---|---|---|---|---|---|---|---|
| AVGO | $29.6B (Q3 FY26, Sep 2) | +86% | AI semis $16.7B, +221%; FY26 $58B, FY27 $115B, FY28 $230B outlook | ~68% op (non-GAAP) | ~$2.0T | ~18x CY27 | Compounder. A 2x is credible, a 5x is not from $2T. Q4 guide missed and BofA flagged margin dilution and Anthropic/OpenAI concentration. |
| AMD | $11.5B (Q2, Aug 4) | DC +107% | Data center $6.7B; OpenAI 6 GW, Anthropic 2 GW Helios, Azure | 56% GM, flat | ~$800B | ~21x 2027 EPS ($15.45 consensus) | The only merchant second source at rack scale. Margins not expanding, warrant dilution up to 10%. 2 to 3x case, not 10x. |
| TSM | $40.2B (Q2, Jul 16) | +36% | HPC 66% of revenue; FY26 growth "slightly above 40%" | 67.7% GM, 60% op | ~$2.2T | ~33% consensus upside | Everyone's supplier, best business in the group, no headroom. Motley Fool's explicit "next Nvidia by 2030" pick, which tells you it is consensus. |
| MRVL | $2.74B (Q2 FY27, Aug 27) | +37% | DC $2.17B +46%; Google warrant deal up to $120B over 6.5 years; FY27 ~$12B | 58.9% GM | ~$190 to 200B | ~50x fwd | Already tripled in 2026; custom ramp lumpy; fell 7% on guide. |
| CBRS (Cerebras) | Q1 +92% | +92% | Wafer-scale inference; only public non-Nvidia accelerator with real revenue | Net loss narrowing | ~$50B | n/a | Fell 14% on its second print; Q2 figures conflict across sources. High-variance option on inference, not a scored pick until numbers are clean. |

Sources: [CNBC AVGO](https://www.cnbc.com/2026/09/02/broadcom-avgo-q3-earnings-report-2026.html), [Seeking Alpha AVGO outlook](https://seekingalpha.com/news/4639799-broadcom-forecasts-58b-fiscal-2026-ai-revenue-and-outlines-115b-in-2027-230b-in-2028), [AMD newsroom](https://newsroom.amd.com/news/amd-2q-2026-earnings/), [AMD/OpenAI](https://www.amd.com/en/newsroom/press-releases/2025-10-6-amd-and-openai-announce-strategic-partnership-to-d.html), [TSMC 6-K](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm), [Marvell IR](https://investor.marvell.com/news-events/press-releases/detail/1031/marvell-technology-inc-reports-second-quarter-of-fiscal-year-2027-financial-results), [CNBC CBRS](https://www.cnbc.com/2026/08/12/cerebras-cbrs-q2-earnings-report-2026.html).

### 4b. Memory and storage (the 2026 blowup)

| Ticker | Latest quarter | Growth | Margin | Market cap | Valuation | Verdict |
|---|---|---|---|---|---|---|
| MU | $41.5B (FQ3, Jun 24) | +346% | 84.9% GM | ~$1T | ~9 to 10x FY27 EPS | Already the Nvidia of 2026. Cheap on paper, but the cheapness is the market pricing a cycle peak. Insider selling heavy. |
| SNDK | $8.97B (FQ4, Aug 5) | +51% QoQ, two-thirds from price | n/a | n/a | n/a | +536% YTD. Guide $10.3 to 10.8B. Pure pricing beta. |
| SK hynix | KRW 79.3T (Q2) | +257% | 76% op margin | n/a | n/a | Fell 9% on a record print. The market is already fading the cycle. |
| Samsung | KRW 171.5T (Q2) | +130% | op profit +1,814% | n/a | n/a | HBM4 sales tripling in Q3; the share-taker that threatens MU. |

Sources: [Micron SEC exhibit](https://www.sec.gov/Archives/edgar/data/723125/000072312526000013/a2026q3ex991-pressrelease.htm), [Sandisk IR](https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-fourth-quarter-2026-financial-results), [SK hynix](https://news.skhynix.com/en/q2-2026-business-results/), [Samsung](https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results).

### 4c. Interconnect and optics (where the setup still exists)

| Ticker | Latest quarter | Growth | Gross / op margin | Next-quarter guide | Market cap | Fwd P/E | Consensus PT vs price |
|---|---|---|---|---|---|---|---|
| CRDO | $479M (FQ1 27, early Sep) | +115% | 68.0% / 48.2% | $525 to 535M; FY27 >+85% | ~$32B | 22 to 27x | $281 vs $171 (+65%) |
| ALAB | $392M (Q2, Aug 4) | +104% | 73.7% / 39.1% | $540 to 560M (+40% QoQ); op margin ~43% | $54 to 72B (sources conflict) | ~120x | $392 vs $304 (+29%) |
| LITE | $1.01B (FQ4 26, Aug 11) | +109% | 50.4% / 36.6% | $1.225 to 1.275B; op margin 39.5 to 40.5% | ~$79B | n/a (trailing ~146x) | $1,148 vs $1,053 (+9%) |
| COHR | $2.05B (FQ4 26, Aug 12) | +34% (+42% pro forma) | 40.2% / n/a | $2.2 to 2.4B | ~$55B | ~29x | $398 vs $282 (+41%) |
| ANET | $3.04B (Q2, Aug 4) | +38% | 63.4% / 49.9% | ~$3.3B; FY26 $12.6B | not retrieved (>$200B likely) | ~37x | $242 vs $194 (+25%) |
| CIEN | $1.67B (FQ3, Sep 3) | +37% | 46.4% / 22.5% | FY27 >+30%; backlog $8.5B | n/a | n/a | n/a |
| AAOI | $192M (Q2, Aug 6) | +86% | n/a | 800G ~5x in Q3; capacity to ~650k units/month | small cap | n/a | Wildcard if the FCC ban on Chinese transceivers proceeds |

Sources: [Credo IR](https://investors.credosemi.com/news-events/news/news-details/2026/Credo-Technology-Group-Holding-Ltd-Reports-First-Quarter-of-Fiscal-Year-2027-Financial-Results/), [Astera IR](https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-second-quarter-2026-financial-results), [Astera 10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000035/alab-20260630.htm), [Lumentum IR](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx), [Coherent](https://www.coherent.com/news/press-releases/fourth-quarter-and-fiscal-year-2026-results), [Arista](https://www.arista.com/en/company/news/press-release/24401-pr-20260804), [Ciena](https://www.nasdaq.com/press-release/ciena-reports-fiscal-third-quarter-2026-financial-results-2026-09-03), [AAOI](https://investors.ao-inc.com/news-releases/news-release-details/applied-optoelectronics-reports-second-quarter-2026-results).

Demand proxy: Nvidia's own data-center networking revenue grew 138% year over year in Q2 FY27, with Spectrum-X up 2.6x. Dell'Oro sees cumulative AI back-end switch spend approaching $1T over 2026 to 2030 and LightCounting sees a path to $100B of AI-cluster optics by 2030 ([Dell'Oro](https://www.delloro.com/news/ai-back-end-switch-sales-to-approach-1-trillion-over-the-next-five-years/), [LightCounting](https://www.lightcounting.com/newsletter/en/march-2026-ethernet-optics-382)).

### 4d. Servers, racks and physical infrastructure

| Ticker | Latest quarter | Growth | Margin | Market cap | Verdict |
|---|---|---|---|---|---|
| DELL | $47.0B (FQ2 27, Sep 1) | +58%; AI orders $60.9B, AI backlog $95B; FY27 ~$192B | low | large cap | +306% YTD; already ran. FY27 AI server revenue ~$74B. |
| SMCI | $11.1B (FQ4, Aug) | +93% | 17.5% GM | mid cap | FY27 guide $65 to 72B. Ran, then margins matter. |
| CLS | $4.70B (Q2, Jul 27) | +62% | 8.2% op | $36 to 49B (sources conflict) | 63% of revenue from three customers; an 8% margin business at 38x. |
| VRT | $3.27B (Q2, Jul 29) | +24% | 22.6% op | ~$99B | Backlog >$15B; 800V DC with Nvidia. A compounder at 38x, not a 10x. |
| APH | $8.8B (Q2, Jul 29) | +55% | 29.5% op | large cap | AI run-rate $10.5 to 11B. Too diversified to be a "next Nvidia." |
| MPWR | $981M (Q2, Jul 30) | +48% | n/a | n/a | Enterprise data +164%; FY segment growth raised to 130%. Interesting, not dominant. |

Sources: [Dell slides](https://www.investing.com/news/company-news/dell-q2-fy27-slides-ai-server-backlog-hits-95b-revenue-up-58-93CH-4884718), [SMCI 8-K](https://www.sec.gov/Archives/edgar/data/0001375365/000137536526000021/exhibit991_20260630.htm), [Celestica](https://corporate.celestica.com/news-releases/news-release-details/celestica-announces-second-quarter-2026-financial-results), [Vertiv 8-K](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026050323/q22026exhibit991vrt07292026.htm), [Amphenol](https://finance.yahoo.com/markets/stocks/articles/amphenol-reports-record-second-quarter-120000607.html), [MPWR 8-K](https://www.sec.gov/Archives/edgar/data/0001280452/000162828026051029/mpwr-20260630xexx991.htm).

### 4e. Power and neoclouds

| Ticker | Latest quarter | Growth | Backlog / contracts | Economics | Verdict |
|---|---|---|---|---|---|
| GEV | Q2 (Jul) | Orders $24.2B, +88% | Backlog $176B; gas turbine backlog and slot reservations 116 GW, target 125 GW by year-end | FY26 FCF $11.5 to 12.5B | Duopoly with Siemens Energy (69 GW backlog). Growth is capped by factory throughput, not demand. Already re-rated; a compounder. |
| BE | $1.07B (Q2, Jul 28) | +166% | FY26 revenue $3.9 to 4.2B (~+100%) | GM 33.4%, non-GAAP op income $800 to 900M | 9x since July 2025. Behind-the-meter fuel cells are the fastest power to deploy. The Motley Fool asked "Is Bloom the next Nvidia?" in July, which is usually a late signal. |
| VST / CEG / TLN | Q2 | EBITDA +30 to 34% | Meta 2.6 GW 20-year PPAs with Vistra; Microsoft 835 MW with Constellation; Amazon 1.92 GW with Talen | Self-funding, high FCF | Scarcity pricing on baseload, but merchant softness already showing (Vistra revenue miss, NRG -15%). Mid-teens growers. |
| OKLO / SMR / LEU | Q2 | Pre-revenue (Oklo $1.2M; NuScale $75K) | Oklo Aurora targets 2028; NuScale still has no definitive PPA; Centrus backlog $4.5B | Cash burn | Binary, years away. No US commercial SMR generates power in 2026. |
| CRWV | $2.6B (Q2, Aug 11) | +112% | Backlog $104.2B plus $25B new in early Q3 | FY26 revenue $12.4 to 13.2B against capex $35 to 39B | Growth is Nvidia-like; economics are the opposite (levered lessor of depreciating GPUs to five customers). |
| NBIS | $582M (Q2, Aug 12) | +454% | Meta up to $27B; ARR $3B | Adj EBITDA margin 41%; capex $20 to 25B vs ~$3B revenue | Best neocloud margin trajectory. Funding need is the risk. Watch-list only. |
| ORCL | FQ4 (Jun 10) | OCI +93% | RPO $638B | FCF -$23.7B; $20B equity ATM | Mega-cap; no path to 5x. |
| WULF / APLD / CIFR / IREN | Q2 | transitional | TeraWulf: $19B 20-year Anthropic lease vs $3 to 4B capex; Applied Digital: $36B of 15-year leases; Cipher: $8.5B AWS and Google-backed leases; IREN: $9.7B Microsoft | Heavy losses, warrants, secured debt | Highest lease-to-equity leverage in the market. A 5x is arithmetically possible for TeraWulf, but with one customer and Google dilution of ~14%. |

Sources: [GE Vernova Q2](https://www.gevernova.com/news/articles/ge-vernova-releases-second-quarter-2026-financial-results), [Utility Dive on 116 GW](https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/), [Bloom Q2](https://investor.bloomenergy.com/press-releases/press-release-details/2026/Bloom-Energy-Reports-Record-Second-Quarter-2026-Financial-Results-and-Raises-Full-Year-2026-Guidance/default.aspx), [Vistra/Meta](https://investor.vistracorp.com/2026-01-09-Vistra-and-Meta-Announce-Agreements-to-Support-Nuclear-Plants-in-PJM-and-Add-New-Nuclear-Generation-to-the-Grid), [CNBC CoreWeave](https://www.cnbc.com/2026/08/11/coreweave-crwv-q2-earnings-report-2026.html), [Nebius Q2](https://nebius.com/newsroom/nebius-reports-second-quarter-2026-financial-results), [Oracle FQ4](https://www.oracle.com/news/announcement/q4fy26-earnings-release-2026-06-10/), [TeraWulf/Anthropic](https://www.terawulf.com/resources/terawulf-signs-19-billion-lease-with-anthropic-for-ai-infrastructure-campus), [Applied Digital](https://ir.applieddigital.com/news-events/press-releases/detail/159/applied-digital-reports-fiscal-fourth-quarter-and-full-year), [NuScale Q2](https://www.nuscalepower.com/press-releases/2026/nuscale-power-reports-second-quarter-2026-results), [Oklo Q2](https://www.investing.com/news/company-news/oklo-q2-2026-slides-first-criticality-achieved-3b-liquidity-93CH-4846923).

Grid context: Goldman projects US data-center power demand of 41 GW in 2026 and 66 GW in 2027; PJM's December 2025 capacity auction cleared 6.6 GW short of its reliability target at a record price, and summer 2027 is projected to be the first season with insufficient capacity ([Goldman](https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027), [PJM](https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/), [Utility Dive](https://www.utilitydive.com/news/pjm-board-backstop-capacity-auction-data-center-curtailment/826347/)). Power is a genuine bottleneck, but its winners are either already priced (GEV, BE) or pre-revenue (SMRs).


### 4f. Next-paradigm plays (physical AI, agents, quantum, space)

| Ticker | Latest quarter | Growth | Market cap | Valuation | Verdict |
|---|---|---|---|---|---|
| PLTR | $1.94B (Q2, Aug 2) | +93%; US commercial +149%; Rule of 40 = 155 | ~$380 to 430B | ~50x TTM sales | The best *financial* analogue (62% adj op margin, 63% FCF margin) but the multiple already assumes it. 40% off its high before the print. |
| TSLA | $28.2B (Q2, Jul 22) | +26%; op income -57% | ~$1.4T | ~190x fwd | Optimus lines being installed, robotaxi in 7 metros, no FSD licensing deal. Optionality is priced; margins are collapsing. |
| SPCX | first public quarter not retrieved | n/a | ~$1.8T | Morningstar FV ~55% below | Largest IPO ever, trades near issue. No headroom. |
| RKLB | $234M (Q2, Aug 10) | +62%; backlog $2.36B | ~$38B | ~40x sales | Neutron to pad Q4 2026 is a binary. Not an AI-bottleneck story. |
| IONQ | $80M (Q2) | +287% (organic +132%); RPO $485M | $13 to 16B | ~50x fwd sales | Best quantum fundamentals; the group is ~100x forward sales and all four names fell 30% in a month. |
| QNT (Quantinuum) | $8M (Q2) | +279% | ~$13B | n/a | IPO'd June 4 at $60, now ~$49. Pre-revenue at scale. |
| SYM | $721M (FQ3) | +22%; backlog $22.5B | ~$5.6B | n/a | Real, GAAP profitable, Walmart-concentrated, 22% gross margin. |
| Cambricon | RMB 6.0B (H1) | +108% | ~$102B | n/a | China's Nvidia substitute; run already happened, inventory exceeds H1 revenue. |

Sources: [Palantir SEC exhibit](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000039/a2026q2ex991pressrelease.htm), [CNBC TSLA](https://www.cnbc.com/2026/07/22/tesla-tsla-q2-2026-earnings-report.html), [CNBC SPCX](https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html), [Rocket Lab IR](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-second-quarter-2026-financial-results-posts), [IonQ IR](https://investors.ionq.com/news/news-details/2026/IonQ-Announces-Record-Second-Quarter-2026-Revenues-Growing-287-YoY/default.aspx), [Quantum Insider](https://thequantuminsider.com/2026/08/12/quantinuum-revenue-jumps-279-in-first-earnings-report-since-ipo/), [Symbotic IR](https://ir.symbotic.com/news-releases/news-release-details/symbotic-reports-third-quarter-fiscal-year-2026-results), [Tom's Hardware Cambricon](https://www.tomshardware.com/tech-industry/semiconductors/cambricon-targets-500000-ai-chips-in-2026-as-china-accelerates-domestic-hardware-push).

---

## 5. Scorecard

Scores are judgment calls applied to the sourced data above. A = bottleneck ownership, B = demand visibility, C = margin trajectory, D = growth, E = headroom, F = multiple versus growth.

| Rank | Ticker | A | B | C | D | E | F | Total | One-line read |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **CRDO** | 4 | 4 | 4 | 5 | 5 | 5 | **27** | Nvidia-grade margins, 115% growth, $32B cap, ~25x forward after a 20% drop |
| 2 | **LITE** | 5 | 4 | 5 | 5 | 3 | 2 | **24** | Owns the constrained laser; margins expanding fastest; $79B and expensive |
| 3 | **ALAB** | 4 | 4 | 4 | 5 | 3 | 1 | **21** | Fastest sequential growth; scale-up fabric for the ASIC world; 120x forward |
| 4 | AMD | 3 | 4 | 2 | 4 | 1 | 4 | 18 | Rack-scale second source; margins flat; $800B |
| 5 | NBIS | 2 | 4 | 3 | 5 | 3 | 1 | 18 | Growth and margin trajectory real; capex seven times revenue |
| 6 | COHR | 4 | 4 | 3 | 3 | 3 | 4 | 21 (note) | Nvidia's $2B laser partner; 40% gross margin caps the upside; scores well but Lumentum is the purer version |
| 7 | AVGO | 5 | 5 | 3 | 4 | 0 | 4 | 21 (note) | The best custom-silicon franchise; $2T cap removes the "blowup" possibility |
| 8 | MU | 4 | 5 | 5 | 5 | 0 | 5 | 24 (note) | Perfect fundamentals, zero headroom: the 2026 blowup, not the next one |
| 9 | CBRS | 3 | 2 | 1 | 4 | 3 | 1 | 14 | Real inference alternative; unclean numbers |
| 10 | BE | 3 | 4 | 3 | 5 | 2 | 2 | 19 | Already 9x |
| 11 | WULF | 1 | 5 | 1 | 2 | 5 | 2 | 16 | $19B lease vs $3 to 4B capex; one customer |
| 12 | PLTR | 3 | 3 | 5 | 5 | 0 | 0 | 16 | Best financial analogue, fully priced |
| 13 | GEV | 5 | 5 | 3 | 2 | 1 | 3 | 19 | Turbine duopoly; capped by factories; large cap |
| 14 | TSM | 5 | 5 | 4 | 2 | 0 | 3 | 19 | Consensus pick, no headroom |

Names scoring high on fundamentals but zero on headroom (MU, AVGO, TSM, PLTR) are excellent businesses that cannot produce a 10x from here. The ranking is about the *blowup* setup, not business quality.

---

## 6. Deep dive: Credo Technology (CRDO)

### What it is

Credo sells the high-speed connectivity inside AI racks: active electrical cables (AECs, copper cables with retimer chips that replace optical links at 800G and 1.6T inside and between racks), optical DSPs, silicon-photonics PICs, and its "ZeroFlap" optical transceivers. Its core IP is SerDes design, licensed to hyperscalers and embedded in its own products. It invented the AEC category and still leads it.

### The numbers

| Item | Value | Source |
|---|---|---|
| FQ1 2027 revenue (quarter ended Aug 1, 2026) | $479.0M, +114.7% YoY, +9.6% QoQ; seventh straight triple-digit quarter | [Credo IR](https://investors.credosemi.com/news-events/news/news-details/2026/Credo-Technology-Group-Holding-Ltd-Reports-First-Quarter-of-Fiscal-Year-2027-Financial-Results/) |
| Non-GAAP gross margin | 68.0% (GAAP 64.5%) | same |
| Non-GAAP operating margin | 48.2% ($230.6M) | same |
| Non-GAAP net margin | 49.3%; EPS $1.20 (GAAP $0.67) | same |
| FQ2 2027 guide | Revenue $525 to 535M; non-GAAP GM 67 to 69% | same |
| FY2027 outlook | Revenue growth above 85%; non-GAAP net margin ~50%; optical revenue above $600M with optical DSPs, silicon-photonics PICs and ZeroFlap each above $100M | [Yahoo call highlights](https://finance.yahoo.com/markets/stocks/articles/credo-technology-group-q1-earnings-230226578.html) |
| FY2026 revenue | $1.34B, +205.7% | [StockAnalysis](https://stockanalysis.com/stocks/crdo/) |
| Share price / market cap | $170.57 / $32.1B (Sep 7, 2026) | [StockAnalysis](https://stockanalysis.com/stocks/crdo/statistics/) |
| Forward P/E | 22.5x (StockAnalysis) to 26.8x (GuruFocus, Sep 4) | [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/CRDO) |
| Trailing P/E, P/S | 58x, 20x | StockAnalysis |
| Post-earnings reaction | About -20% despite the beat | StockAnalysis (magnitude unverified) |
| Consensus target | $281 average (19 analysts, range $185 to 350); Evercore initiated Outperform at $325 | [StockAnalysis forecast](https://stockanalysis.com/stocks/crdo/), [MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/CRDO/forecast/) |
| Customer concentration | Amazon was 67% of FY2025 revenue; by FQ3 2026 the top three were 39%, 32% and 17%; Microsoft and xAI ramping; a fifth hyperscaler signed | [Substack analysis](https://spheniscidae007.substack.com/p/credo-technology-group-holding-ltd), [Yahoo](https://finance.yahoo.com/news/analysts-highlight-credo-hyperscaler-partnerships-191746184.html) (secondary sources) |

### Why it matches the Nvidia pattern

1. **Margin structure says pricing power.** A 68% gross margin and a 48% operating margin at under $2B of annual revenue is a Nvidia-like profile. Nvidia's FY2024 operating margin was about 54% at $61B of revenue. Nobody gets 48% operating margins on cables unless the IP is the product.
2. **Growth is guided, not hoped.** Seven triple-digit quarters, then a guide of more than 85% for FY2027 with a back-half-weighted optical ramp. Nvidia's tell in 2023 was guidance that outran consensus; Credo's guidance is above where the stock trades.
3. **The multiple has already compressed.** At roughly 22 to 27x forward earnings against 85%-plus growth, the PEG is about 0.3. That is the Nvidia-2023 configuration where the price looked expensive on trailing numbers and cheap on forward ones. The 20% post-print drop on a beat is expectations resetting, not fundamentals.
4. **Headroom exists.** $32B is the smallest cap of any name in the top tier. A 10x is $320B, which needs roughly $12 to 15B of revenue at Credo's margins. Credo's own framing is a "$10B-plus" addressable market; Dell'Oro's cumulative $1T of AI back-end switching through 2030 and LightCounting's $100B optics path make that a share question, not a market-size question ([Benzinga](https://www.benzinga.com/trading-ideas/movers/26/06/60023965/credo-wires-agentic-ai-with-10-billion-plus-market-in-sight)).
5. **The customer base is diversifying at the right moment.** Amazon concentration has fallen from 67% to under 40%, Microsoft and xAI are ramping, and a fifth hyperscaler signed. Nvidia's 2023 to 2024 move coincided with its customer list widening from Microsoft to everyone.
6. **The demand proxy is screaming.** Nvidia's own data-center networking revenue grew 138% in the latest quarter and Spectrum-X 2.6x. Every rack Nvidia and its custom-ASIC rivals ship needs more copper and optical links per accelerator, not fewer.

### The path to 5 to 10x

| Milestone | What has to happen | Rough timing |
|---|---|---|
| Revenue $2.5B (FY2027) | Deliver the 85%-plus guide | Mid-2027 |
| Revenue $4 to 5B | Optics becomes a second engine equal to AECs; four-plus hyperscalers at scale; 1.6T AEC attach on Rubin Ultra and custom XPU racks | FY2028 to FY2029 |
| Net margin holds near 45 to 50% | Mix shift to optical modules does not crush gross margin below 60% | Continuous |
| Multiple re-rates to 35 to 45x | Market accepts a multi-year growth runway | Whenever consensus catches up |

$4.5B of revenue at a 45% net margin is about $2B of net income; at 40x that is $80B, a 2.5x. A 10x requires the $12 to 15B revenue case, which means Credo becomes the default interconnect supplier for the non-Nvidia half of the market. That is possible but not the base case. **Base case: 2.5 to 4x over three years. Bull case: 10x.**

### What breaks it

- **Marvell and Amphenol enter AECs with DSP silicon.** Marvell has the SerDes and the hyperscaler relationships; Amphenol has the cable plant. Credo's share and its 68% gross margin are both at risk if AECs commoditize.
- **CPO and LPO leapfrog retimed architectures.** Co-packaged optics remove the DSP from the transceiver. Credo is entering optical DSPs at exactly the moment the industry debates removing them. Celestica already won a 1.6T CPO switch program for 2027.
- **Customer concentration reverses.** Two customers are still 70% of revenue. One design loss at Amazon or Microsoft is a 20 to 30% revenue hole.
- **The AI capex cycle turns.** Neoclouds and hyperscalers are now externally financed. Credo sells into the most discretionary part of the rack.
- **Beta.** The stock's beta is about 3.2. It fell 20% on a beat. A 50% drawdown in a risk-off tape is normal for this name, and it has to be sized accordingly.

### Signposts for the next 12 months

- FQ2 2027 print (December 2026): does revenue clear $535M and does the optical mix show up?
- Any new 10%-customer disclosure in the 10-Q (a fourth or fifth hyperscaler above 10% de-risks the thesis).
- Marvell's AEC product announcements and any Amphenol cable partnership pricing.
- Nvidia's Rubin Ultra rack reference designs: copper versus optical attach counts.
- Whether Credo's ZeroFlap optics win a hyperscaler slot in 2027.

---

## 7. Deep dive: Lumentum (LITE), the bottleneck pick

### Why it is the "memory of optics"

The AI cluster moves from 800G to 1.6T links in 2026 and 2027. A 1.6T link needs 200G-per-lane EML lasers, and Lumentum holds 50 to 60% share of that laser, built on indium-phosphide capacity that takes years to add. That is the same shape as HBM in 2025: a component nobody thought about, a two-year supply lag, and a customer who cannot ship without it. Nvidia's $2B equity investment in Coherent, plus a multi-year CPO supply agreement through the end of the decade, is Nvidia locking up laser supply the way it locked up memory with $279B of purchase commitments. Lumentum is the purer public expression of the same shortage.

| Item | Value | Source |
|---|---|---|
| FQ4 2026 revenue (reported Aug 11) | $1.01B, +109% YoY; first $1B quarter | [Lumentum IR](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx) |
| Non-GAAP gross / operating margin | 50.4% / 36.6% | same |
| Non-GAAP EPS | $3.23 | same |
| FQ1 2027 guide | Revenue $1.225 to 1.275B; op margin 39.5 to 40.5% (more than 2,100 bp of YoY expansion at midpoint); EPS $4.05 to 4.35 | same |
| Optical circuit switch revenue | Doubled QoQ to above $100M per quarter; management targets above $400M in the second half | [PhotonCap](https://photoncap.net/p/lumentums-first-1b-quarter-fq4-2026) |
| Market cap / price | ~$79B / ~$1,053 (Sep 4) | [StockAnalysis](https://stockanalysis.com/stocks/lite/market-cap/) |
| Valuation | Trailing ~146x; forward P/E not retrieved. On the FQ1 EPS guide annualized (~$17), roughly 60x | derived |
| Consensus target | $1,148 average, 24 analysts (range $820 to 1,400) | [Investing.com](https://www.investing.com/equities/lumentum-holdings-inc-consensus-estimates) |

**The bull case:** operating margin from 15% to 40% in a year is the fastest margin expansion of any company studied, including Nvidia's 2023. If revenue doubles again in FY2027 to about $4.5B at 40% operating margins, EPS approaches $17 to 18 on a full-year basis and the stock is at ~60x, still expensive. A 5x from $79B is $400B, which needs $10B-plus of revenue: plausible only if 1.6T and CPO adoption run ahead of forecasts and Chinese EML makers stay two generations behind.

**What breaks it:** Chinese 200G EML catch-up (a two- to four-year risk per Anand Capital); an optics glut in 2028 as capacity arrives (the industry did this in 2001); the June 2026 "optics valuation reckoning" drawdown shows how fast the multiple can compress; PEG near 1 leaves no margin of safety ([Anand Capital](https://anandcapital.substack.com/p/lumentum-holdings-inc-lite-investment), [24/7 Wall St](https://247wallst.com/investing/2026/06/23/applied-optoelectronics-plunges-13-coherent-drops-9-lumentum-falls-8-has-an-optics-valuation-reckoning-begun/)).

**Versus Coherent:** Coherent has the Nvidia anchor and trades at 29x forward, but its 40% gross margin and heavier balance sheet cap the upside. Lumentum's higher margin and the OCS second engine make it the better "blowup" candidate; Coherent is the safer way to own the same shortage.

---

## 8. Deep dive: Astera Labs (ALAB), the paradigm pick

### The thesis

Nvidia's NVLink is the scale-up fabric for Nvidia racks. Everyone else (AWS Trainium, Google TPU, Meta MTIA, the OpenAI and Anthropic chips Broadcom is building) needs a merchant scale-up fabric. Astera's Scorpio X-Series switch entered volume production in Q2 2026 and will be its largest product line in Q3. If Broadcom's fiscal-2028 AI revenue outlook of $230B is even half right, and TrendForce's forecast that ASIC shipments grow 45% versus 16% for merchant GPUs holds, the non-Nvidia half of the market is where the fastest interconnect growth will be, and Astera is the pure play on it.

| Item | Value | Source |
|---|---|---|
| Q2 2026 revenue (reported Aug 4) | $392.4M, +104% YoY, +27% QoQ | [Astera IR](https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-second-quarter-2026-financial-results) |
| Non-GAAP gross / operating margin | 73.7% / 39.1% (+290 bp QoQ) | same |
| Non-GAAP EPS | $0.80 | same |
| Q3 2026 guide | Revenue $540 to 560M (+40% QoQ at midpoint); op margin ~43%; EPS $1.16 to 1.21 | [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q2-2026-eps-forecast-shares-swing-93CH-4836051) |
| Customer concentration (Q2 10-Q) | Five customers each at or above 10%: 29%, 25%, 15%, 13%, 10%+; Amazon holds purchase-linked warrants | [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000035/alab-20260630.htm) |
| Market cap | $54B (CNN) to $72B (StockAnalysis), sources conflict | [StockAnalysis](https://stockanalysis.com/stocks/alab/statistics/) |
| Forward P/E, P/S | ~120x, 46x | same |
| Returns | YTD +92%, 1-year +227% | same |
| Consensus target | $392 (26 analysts, range $190 to 500); Citi $430; Jefferies $450 | [StockAnalysis forecast](https://stockanalysis.com/stocks/alab/forecast/) |

**Why it ranks third, not first:** at 120x forward earnings the market already believes the paradigm. Nvidia at $1T in mid-2023 was about 50x forward; Astera is more than twice that. The thesis also has a specific structural threat: Nvidia is licensing NVLink (NVLink Fusion) to custom-silicon builders, and Amazon, Astera's biggest customer, co-adopted it for Trainium4. If NVLink Fusion becomes the default scale-up fabric for ASICs too, Scorpio X is fighting the incumbent on its own turf. Astera was also left out of the ESUN open scale-up architecture backed by Meta, AMD, Broadcom and Marvell ([Yahoo/Benzinga](https://finance.yahoo.com/news/astera-labs-battles-nvidia-broadcom-182512569.html), [The Register](https://www.theregister.com/systems/2026/08/31/nvidia-is-building-an-ip-licensing-empire-on-the-back-of-nvlink/5293530)).

**What would move it to first:** a second consecutive quarter of 30%-plus sequential growth with operating margin above 45%, and a disclosed design win on a Broadcom-built XPU rack (OpenAI or Anthropic). That combination would make it the merchant scale-up standard and justify the multiple.

---

## 9. Why not the obvious names

- **AMD.** The strongest fundamental story outside Nvidia: data center +107%, OpenAI 6 GW, Anthropic 2 GW, Azure Helios, 2027 EPS consensus rising from $12.96 to $15.45 in ninety days. But gross margin is stuck at 56% while data center doubles, capex is rising, the OpenAI warrant can dilute up to 10%, and the CEO sold $80M of stock in August. From $800B a 2 to 3x is the ceiling. It is a very good stock, not a blowup.
- **Broadcom.** FY2028 AI revenue of $230B would be a 4x from FY2026, and the customer list (Google, Meta, OpenAI, Anthropic, Apple) is the best in the industry. At $2T the stock can double; it cannot 10x. The Q4 guide miss and the margin dilution from hardware-heavy XPU racks are the near-term issues.
- **Micron and the memory complex.** Perfect fundamentals, cheapest multiple, zero setup: the stock is up 7x in a year, insiders are selling, Samsung is coming, and the market is already fading record prints (SK hynix -9% on a record quarter). The next leg is earnings-driven, not multiple-driven, and the cycle risk is real for 2028.
- **TSMC.** The consensus "next Nvidia" pick, which disqualifies it. No headroom at $2.2T.
- **Palantir.** Growth of 93% at a 62% operating margin is the closest *financial* analogue to Nvidia in the whole market. At 50x sales and roughly $400B, it needs to become a $1T software company just to justify the current price.
- **CoreWeave and the neoclouds.** Nvidia-like growth (CoreWeave +112%, Nebius +454%) with the opposite economics. Nvidia earned 75% gross margins on negligible capex and no customer credit risk. Neoclouds spend three to seven times revenue on GPUs that depreciate in four years and lease them to five customers. Nebius is the one to watch if it can fund $20 to 25B of capex without crushing equity holders.
- **Cerebras.** The only public inference-specific chip company with real revenue, down 14% on its second print, with Q2 numbers that conflict across sources. Worth a small speculative position once a clean 10-Q exists, not a scored pick today.
- **Power (GE Vernova, Bloom, Vistra).** The bottleneck is real and multi-decade. GE Vernova is capped by factory throughput, Bloom has already gone 9x, and the merchant generators are seeing power prices soften. The SMR names are pre-revenue with 2028 to 2030 timelines.
- **SpaceX, Tesla, quantum.** SpaceX at $1.8T trades near its IPO price with Morningstar's fair value 55% lower. Tesla's operating income fell 57% while the stock trades at 190x forward. The quantum group is about 100x forward sales and fell 30% in a month.

---

## 10. Risks common to every candidate

1. **The capex cycle.** Big-four capex of $725B in 2026 and roughly $1T in 2027 is now funded by equity raises (Alphabet $84.75B in June) and debt. Any pause resets every name here by 40 to 60%; the interconnect names have betas near 3.
2. **Circular financing.** Nvidia invests in Coherent, CoreWeave and Nebius; AMD pays OpenAI in warrants; Google backstops TeraWulf and Cipher; Oracle counts $75B of customer-prepaid hardware in RPO. Demand and financing are entangled in a way they were not in 2023.
3. **Nvidia's own gravity.** Nvidia is now the number-one data-center Ethernet vendor (IDC, 1Q26), is licensing NVLink, bought Groq's team for $20B and acquired Hugging Face. Any merchant supplier of a rack component competes with its biggest customer's ambitions.
4. **China.** Nvidia assumes zero China data-center compute revenue. Cambricon and Huawei will supply about 90% of China's accelerators in 2026. For optics, Chinese vendors hold about 60% of 800G volume; a US ban would help Lumentum, Coherent and AAOI, and a thaw would hurt them.
5. **The IPO supply wave.** Anthropic (about $965B), OpenAI (about $852B) and Databricks ($190B) listing within 12 months will pull capital out of public AI proxies.

---

## 11. Twelve-month signposts

| Date | Event | What it decides |
|---|---|---|
| Sep 10, 2026 | Oracle FQ1 2027 | Whether RPO keeps growing while FCF stays negative |
| Late Sep 2026 | Micron FQ4 2026 | Whether the $50B guide holds and HBM4 share moves |
| Oct to Nov 2026 | Hyperscaler Q3 prints | 2027 capex guides: the single most important number for every name here |
| Nov 2026 | Nvidia Q3 FY27 | Gross margin trajectory toward the 71 to 72% trough; Rubin mix; networking growth |
| Dec 2026 | Credo FQ2 2027; Astera Q3 | Whether the top two picks deliver $535M and $550M |
| Q4 2026 | Rocket Lab Neutron to pad; Anthropic IPO window | Capital rotation into new listings |
| H1 2027 | AMD Helios first GW for OpenAI; Anthropic MI450 start; Rubin Ultra reference designs | Copper versus optical attach counts, NVLink Fusion versus UALink adoption |
| 2027 | HBM contract prices (TrendForce sees a potential doubling); CoWoS supply gap closing to ~10% | Whether memory stays the bottleneck or the bottleneck moves again, to optics and power |

---

## 12. Data caveats

This memo was assembled on September 8, 2026 from search-engine excerpts of the cited pages. Direct fetches of primary sources were blocked by the research environment's network policy, and the search budget was exhausted before every figure could be cross-checked. Specific gaps:

- Consensus 2026 and 2027 revenue and EPS estimates were not retrieved for most names; company guidance is used instead.
- Market caps for Astera Labs, Celestica and Vertiv conflict across sources by 20 to 35%; the ranges are shown.
- Nvidia's FY2023 to FY2025 gross margin and net income are from memory and flagged as such.
- Credo's post-earnings drop is reported as "about 20%" by one aggregator and not independently confirmed.
- Cerebras Q2 2026 figures conflict across sources and are excluded from scoring.
- Power and neocloud share prices, market caps and multiples were not retrieved at all; those names are scored on fundamentals and backlog only.

Underlying agent research files with full source lists are preserved in the session scratchpad and summarized in the source links above.

