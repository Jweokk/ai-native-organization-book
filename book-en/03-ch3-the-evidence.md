# Chapter 3: The Evidence — What the Empirical Research Says

The first two chapters were about concepts and cases. This chapter looks only at evidence: what academic research and authoritative institutions' data actually say about AI-native organizations. To avoid "cherry-picking evidence that favors our argument," I will also list the limitations of every study.

## 3.1 HBS's *AI-Native Firms*: The Strongest Firm-Level Evidence

*AI-Native Firms* (HBS Working Paper 26-090, 2026)<sup><a href="12-appendix-a-sources.md#1-29">[1-29]</a></sup>, a working paper by Harvard Business School's Rembrand Koning and INSEAD's Hyunjin Kim and colleagues, is currently the hardest first-hand evidence at the firm level.

**Method**: All 2,891 YC startups from the W20–F24 cohorts (11 batches), plus 41,214 US VC-backed startups from PitchBook<sup><a href="12-appendix-a-sources.md#1-29">[1-29]</a></sup>, linked to micro-level labor data and compared against non-AI startups of the same industry and period.

**Core findings**:

| Dimension | AI-native firms vs. non-AI peers |
|------|--------------------------|
| Team size | **~25% smaller** (YC firms roughly half the size after three years) |
| Share of engineers | ~13 percentage points higher |
| Entry-level employees | ~15% fewer |
| Senior employees | ~20% more |
| Management layers | **Half a level flatter** |
| Managers | ~15% fewer |
| Funding / valuation | Comparable → ~20% more funding per capita, higher valuation per capita |

In one sentence: **AI-native companies are smaller, flatter, more engineer-dense, and more senior, with comparable valuations — and higher output per capita.**<sup><a href="12-appendix-a-sources.md#1-29">[1-29]</a></sup>

The paper's most important theoretical contribution is distinguishing two channels:

- **The process channel**: AI as an internal production tool that changes how employees do their work (agentic coding, AI customer service, automated sales) — this is where most existing research focuses;
- **The product channel**: AI capabilities embedded into the product, so customers generate deliverables directly inside the product — **knowledge work moves out of the internal organization and into the product**, scaling through compute rather than headcount.

**The decisive evidence: the process channel cannot predict smaller organizations.** AI startups are 2.6 times<sup><a href="12-appendix-a-sources.md#1-29">[1-29]</a></sup> more likely than non-AI peers to name ChatGPT/Copilot/Cursor in job postings — but that indicator cannot predict smaller teams. After controlling for the process channel, product-embedded AI remains significantly associated with fewer people and flatter structures.

**The largest differences appear in service businesses**: in service startups such as therapy, tutoring, and telemedicine, AI startups are about 70%<sup><a href="12-appendix-a-sources.md#1-29">[1-29]</a></sup> smaller than non-AI peers. Cases: Gamma (AI presentations; roughly 30 people reached $50 million in annual revenue within two years); FazeShift (an accounts-receivable AI agent; 10 people won dozens of enterprise clients, replacing the AR team at each client).

**A cautious conclusion about the labor market**: every AI-native company is smaller, but total employment need not fall — AI dramatically increases the number of startups (PitchBook's 2024 AI seed funding was about 8 times the 2020 average)<sup><a href="12-appendix-a-sources.md#1-29">[1-29]</a></sup>. Extrapolating from the firm level to the market level requires caution.

**Limitations**: the sample is YC/VC-backed startups, which may not generalize to mature large enterprises; the "AI-native" classification is the researchers' own definition; and the working paper has not been peer-reviewed.

## 3.2 The INSEAD/HBS Field Experiment: Rare Causal Evidence

The randomized controlled trial of 515 startups mentioned in the previous chapter (*Mapping AI into Production*, 2026)<sup><a href="12-appendix-a-sources.md#1-33">[1-33]</a></sup> is the scarcest kind of causal evidence in AI organization research: tools, skills, and budgets were fully equalized, and only the "organizational search space" was changed (the treatment group was shown how AI-native organizations restructure). The result: treatment-group use cases +44%, revenue 1.9x, external funding needs −39.5%.

**The "mapping problem"**: what limits AI gains is not the cost of technology or skills, but the cognitive bottleneck of "discovering where and how AI creates value in your own production process."

**Limitations**: a 10-week short-term experiment; a startup sample; the 1.9x revenue figure is a short-term relative increment with small absolute values (on the order of, say, $40,000).

## 3.3 WEF's *AI-First Operating Models*: A Systematic Framework for Operations

The World Economic Forum's (2026) core proposition: **layering AI on top of operating models designed for the pre-AI world (linear processes, static roles, incremental optimization) is a structural failure.** Global AI investment exceeded $250 billion in 2024, yet in most organizations "AI has not fundamentally changed the way they operate."

Three shifts:

1. **Work and teams: from process management to human–AI collaboration** — early AI-first organizations already have **human-to-AI ratios exceeding 10:1** (1 human : 10+ AI); delegation is a management skill that requires training and certification (the You.com CEO: adoption in mature organizations only really took off after a training-and-certification program was launched);
2. **Workflows: from linear processes to dynamic AI systems** — the Rubrik CEO's implementation path: **"go business line by business line; in each line, find 3–5 workflows that are purely manual or SaaS-plus-human, and define end-to-end AI-driven outcomes"**; the starting question determines everything (Lightspeed: "If we had unlimited intelligence, what would we build?");
3. **Metrics: from process optimization to dynamic value creation** — outcome-oriented, with reliability/accuracy/governance first to build trust.

Key judgment: **competitive advantage comes from orchestration, not experimentation.** Successful leaders treat capability, process, outcome, and business-model redesign as a single integrated evolution.

## 3.4 Tencent Research Institute's *AI-Native Work Report*: A Complete Framework from a Chinese Perspective

Tencent Research Institute (Chinese: 腾讯研究院) published a 40,000-character report in May 2026, with lead authors Si Xiao, Yuan Xiaohui, and Yu Yi (Chinese: 司晓、袁晓辉、余一). The most widely circulated part is its **competitiveness formula**:

> **Organizational competitiveness = talent density × AI leverage ÷ organizational friction**

If the numerator doubles but the denominator stays fixed, the net effect is discounted; **halving the denominator is equivalent to doubling the numerator** — reducing organizational friction (waiting/approvals/alignment/information decay) is usually easier to move than piling on talent.

The report defines four structural characteristics of the "Super-Individual" (all required):

1. **An AI-first workflow**: AI is the default starting point — "I let AI run first, then judge and correct on top of its output";
2. **An order-of-magnitude leap in capability boundaries**: 10x+ output; one person runs the full chain from idea to delivery;
3. **Extreme proactivity**: doesn't wait for organizational assignment; a natural boundary explorer;
4. **Influence spillover** (the key threshold for identifying Super-Individuals): **efficient individuals only make themselves faster; Super-Individuals make the team faster.**

It also outlines four emergence paths (bottom-up spontaneity / organizational selection and cultivation / atmosphere creation / founder-driven), three team forms (node-radiation / network collaboration / AI-hub), and one harsh judgment about the capability reshuffle: **AI is an accelerator of divergence, not an equalizer — only those who were already excellent become more excellent, and the gap widens.**

**We must emphasize the report's sample bias** (this is the knowledge base's systematic critique of the report): roughly 80% of its cases come from information-intensive, digital-native industries with fewer than 500 employees, with zero coverage of physical-world industries (manufacturing lines / medical clinical settings / logistics). The evidence in the report supports only this: **in information-intensive, small-team, digital-native industries, AI-native organizations can dramatically accelerate.** Before applying it to physical industries or large organizations, ask first: is this industry's bottleneck information processing, or the physical world?

## 3.5 Large-Sample Data from Authoritative Institutions

**McKinsey, *State of AI 2025* (November 2025)**: 88% of organizations regularly use AI<sup><a href="12-appendix-a-sources.md#1-03">[1-03]</a></sup> in at least **one business function** (78% last year); but about two-thirds are still in the experiment/pilot stage and only about one-third have begun scaling; only 39% attribute any degree of EBIT impact to AI, and most of them say the contribution is under 5%; "AI high performers" (EBIT impact ≥5%) account for only about 6%<sup><a href="12-appendix-a-sources.md#1-03">[1-03]</a></sup>. **Many companies use AI; very few make money from it.**

**BCG's *AI at Work* series**: a clear leadership–frontline gap — more than three-quarters of leaders use GenAI multiple times a week, while frequent frontline use stalled at 51%<sup><a href="12-appendix-a-sources.md#1-04">[1-04]</a></sup> in 2025 before jumping to 74%<sup><a href="12-appendix-a-sources.md#1-06">[1-06]</a></sup> in 2026 (+23 percentage points). Half of companies are moving from "Deploy" to "Reshape" (redesigning workflows).

**Microsoft's *Work Trend Index***: in 2024, 75% of knowledge workers already used AI<sup><a href="12-appendix-a-sources.md#1-13">[1-13]</a></sup>; in 2025 it introduced the "Frontier Firm" concept<sup><a href="12-appendix-a-sources.md#1-14">[1-14]</a></sup> (about 9.3% of surveyed leaders) — 71% of frontier-firm leaders say their company is "thriving," versus only 39% of employees globally; the most important finding of 2026: **organizational factors (culture, manager support, talent practices) contribute twice as much to AI impact as individual effort** (based on a permutation-importance analysis of 29 factors, R² ≈ 0.68–0.69).

**Stanford HAI's *AI Index 2025***: in 2024, 78% of organizations reported using AI<sup><a href="12-appendix-a-sources.md#1-16">[1-16]</a></sup> (55% in 2023).

**IMF**: AI will affect about 40% of jobs globally; roughly 60% in advanced economies, 40% in emerging markets, and 26%<sup><a href="12-appendix-a-sources.md#1-20">[1-20]</a></sup> in low-income countries — note that these are "exposure" estimates, not unemployment forecasts, and about half of exposed jobs may be augmented rather than replaced.

**WEF's *Future of Jobs 2025***: by 2030, job disruption will equal 22% of current jobs: 170 million created, 92 million eliminated, a net gain of 78 million<sup><a href="12-appendix-a-sources.md#1-27">[1-27]</a></sup>; 77% of employers plan to upskill their workforce, and 41% plan to reduce headcount because of AI automation — expectations, not facts.

## 3.6 A Warning on Data Use (This Book's Citation Discipline)

Putting all the numbers above together, there are five citation disciplines:

1. **Definitions come first**: the "95% failure rate" (MIT, zero organizational return), "30% abandoned" (Gartner, after PoC), and "88% adoption" (McKinsey, at least one function) are not contradictory — they are three different denominators;
2. **Report conclusions vs. media retelling**: media retelling often distorts (e.g., Fortune reported the MIT report's sample as 150 interviews/350 questionnaires, while the report actually covered 52 organizations/153 executives)<sup><a href="12-appendix-a-sources.md#1-02">[1-02]</a></sup>; this book always follows the original report;
3. **Forecasts vs. facts**: most of the Gartner/Forrester/WEF numbers are forward-looking forecasts or employer expectations, not events that have already happened;
4. **Sample bias**: McKinsey/WTI/BCG skew toward white-collar workers, large enterprises, and self-selected survey participants; every "global" claim must be checked against the original sampling scope;
5. **Conflicts of interest**: Microsoft, BCG, and McKinsey all sell AI products/consulting to enterprises — keep their positions in mind when citing their conclusions.

## 3.7 The Core Judgment of This Chapter

The evidence chain is complete: HBS shows AI-native companies are **smaller, flatter, and higher-output per capita**<sup><a href="12-appendix-a-sources.md#1-29">[1-29]</a></sup> (driven by the product channel, not the process channel); INSEAD/HBS shows that **organizational knowledge itself produces causal revenue differences**<sup><a href="12-appendix-a-sources.md#1-33">[1-33]</a></sup>; WEF shows that **operating models must be redesigned around AI**; Tencent shows that **competitiveness comes from talent density × AI leverage ÷ organizational friction**; McKinsey/BCG/Microsoft show that **a huge gap exists between tool adoption and organizational returns**.

**The evidence points exactly where Chapter 1 concluded: models are no longer scarce — what's scarce is organizations redesigned around AI.** In the next chapter, we look at what the inside of such an organization looks like.
