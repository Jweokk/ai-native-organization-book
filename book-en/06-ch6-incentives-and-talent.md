# Chapter 6 Incentives and Talent: The Hardest Variable to Rebuild

Technical problems all have answers; people problems don't. This chapter examines the hardest variable in an AI-native organization: how to evaluate performance, how to incentivize, and how to develop people.

## 6.1 Transn's "Energy Gold": Turning Adoption from an Administrative Order into Market Behavior

Transn (Chinese: 传神), a translation company, runs an "Energy Gold" mechanism that is the Chinese benchmark for AI-native incentive design:

> Every time a colleague genuinely uses an AI application and is satisfied with the result, the development team earns Energy Gold — a colleague-validated incentive credit. The more it is used and the higher the satisfaction, the greater the reward. **Judgment rights go to the users; decision rights go to the data.**

The supporting mechanisms are an AI Native decision committee (organized by business line — AI is not the technology department's business, it is each business line's own business) and the DEMO rule (every AI project must have a runnable DEMO and clearly explain which business problem it solves; no DEMO, no meeting — this kills 90% of PPT projects).

The elegance of "Energy Gold" is that it turns adoption from an "administrative order" into "market behavior": colleagues vote with their feet, creating a positive reinforcement loop of "the more it is used, the better it gets; the better it gets, the more it is used."

## 6.2 Evaluation: From Input to Output

The third of the three lightweight principles for small and mid-sized teams is the most counterintuitive and the most important: **evaluation criteria must change.**

Traditional evaluation looks at hours worked, volume of output, and process KPIs — which is effectively forcing employees to fake using AI. Someone who genuinely knows how to use AI produces more in 3 hours than a non-user does in 10. Evaluation must shift **from input to output, from process to results**.

> If you don't touch evaluation, AI adoption is empty talk — you are touching the root of the entire management system.

International samples are changing evaluation too: Shopify includes AI usage in performance reviews, and its CEO memo requires employees to "first prove AI can't do this job" before applying for additional headcount<sup><a href="12-appendix-a-sources.md#7-19">[7-19]</a></sup>; Duolingo's AI-first memo likewise included using AI to evaluate employee performance<sup><a href="12-appendix-a-sources.md#7-52">[7-52]</a></sup> (though it later sparked controversy).

## 6.3 Tencent Research Institute: Reviews Give Way to Calibration and Four Dimensions of Incentives

The Tencent Research Institute report takes a more radical position: **"reviews" largely retire inside Super-Teams; management action shrinks from "control" to "calibration."**

> When information is transparent enough and individuals are strong enough, management action contracts from control to calibration — the rest is left to people and agents to run on their own.

Super-Individuals do not lack capability; what is scarce is "why invest time here." The four incentive dimensions (all indispensable — an imbalance in any one leads to attrition or downgrade):

| Dimension | Mechanism | Case |
|------|------|------|
| Autonomy (most cited) | You decide what to do and how | Block's DRI system — for 90 days you are the CEO of this problem. "Power incentives first, money incentives second" |
| Growth environment | High-density peers + sense of mission | Kimi: all 300 people see themselves as AGI builders; no OKRs, no KPIs, no clocking in |
| Economic return | How output is fairly priced (the hardest) | Three explorations: Anker Innovations, Tenex, Pure Global |
| Freedom to exit | Retain people by being worth staying for, not by lock-in | Netflix: options vest immediately with no lock-up period |

**Economic return is the dimension the report admits it cannot solve**: "How can a 10–100x efficiency gap be reflected in a compensation system? No company has yet given a replicable answer." Traditional pay is tied to rank and role, but once AI flattens execution capability, the value of judgment and creativity rises sharply. "10x output rewarded with only 1.2x pay" → either leave and start a company, or reduce your effort — either way, the organization loses.

One reverse warning (ColaOS): **"organizations that make efficiency gains their core metric end up laying people off; organizations that make revenue growth their core metric end up expanding"** — the best incentive for a Super-Individual is "your high-output work opened up new business space, and you get to share in that growth."

## 6.4 Super-Individuals and the Competitiveness Formula

The Tencent Research Institute gives four structural characteristics of Super-Individuals (see Chapter 3): an AI-first work pattern, order-of-magnitude jumps in capability boundaries, strong proactivity, and influence spillover — **an efficient individual only makes themselves faster; a Super-Individual makes the team faster.**

The competitiveness formula: **organizational competitiveness = talent density × AI leverage ÷ organizational friction.**

The corollary for talent strategy: shrink the denominator (organizational friction) first, then multiply the numerator (talent density × AI leverage); halving the denominator is equivalent to doubling the numerator. Hiring structure follows the HBS evidence: a higher share of engineers, fewer entry-level roles, half the management layers — **invest the budget in senior all-rounders.**

The reshuffling of capability rankings: AI amplifies underlying capabilities (logic, rapid learning, problem decomposition, systems thinking) — only people who were already excellent become more excellent, and the gap widens. What is actually being repriced is the layer beneath skills: **judgment, learning speed, problem decomposition, taste** — while the existing talent system measures almost entirely the layer that is depreciating.

## 6.5 The Skills Gap: The More AI Is Used, the More "Hollowed-Out" Organizational Capability May Become

This is the most hidden long-term risk of the AI-native organization.

**Anthropic's internal research (December 2025) offers two-sided evidence<sup><a href="12-appendix-a-sources.md#8-40">[8-40]</a></sup>**: engineers become "full-stack" and learn and iterate faster because of AI, **but at the same time worry about deep skills atrophy** — "when output is so easy and fast, actually taking the time to learn something becomes harder and harder"; 27% of AI-assisted work is exploratory work they would not otherwise have done (the good news), yet employees also worry that "one day AI will automate me out of a job."

**WEF 2026**: up to 75% of entry-level jobs in East Asia are disrupted by AI; up to 60% of entry-level tasks can already be taken over by AI<sup><a href="12-appendix-a-sources.md#8-38">[8-38]</a></sup>, and newcomers to the workforce lose their "practice ground" — cutting only entry-level roles severs the pipeline for talent development and innovation.

The essence of the skills gap is a choice between "treating AI as a crutch or as a trainer":

- Let AI fully take over (employees lose practice opportunities) → skills gap;
- Use AI to accelerate learning (AI as sparring partner, explainer, boundary-expander) → organizational capability compounds.

Anthropic has already made "how to prevent skill atrophy" a formal research topic. **The psychological cost of AI-native work is real** — internal employee communications mention "about 5 months without hand-writing code" and "feeling meaningless when everything is automated." Organizations need institutionalized "learning preservation" design.

Overseas research has now quantified the "crutch or trainer" question. The *Widening Gap* study cited by JetBrains frame-by-frame analyzed novice programming behavior: novices who leaned heavily on AI assistance "skipped crucial planning stages" and finished with an "illusion of competence" rather than true understanding; the best-performing novices were those who heavily limited or outright ignored AI assistance — they developed "negative expertise": the ability to identify and ignore incorrect or unhelpful AI suggestions. A University of Pennsylvania 2025 study of 1,000 students found that students learning math with an LLM performed 17% worse than students with only a textbook — while believing they were excelling; in the same study, a "GPT Tutor" group that used the model as a Socratic sparring partner (attempting problems first, asking for help when stuck) performed 127% better<sup><a href="12-appendix-a-sources.md#8-79">[8-79]</a></sup> in practice sessions — **friction itself is a necessary condition for forming expertise**. Anthropic's 2026 study on how AI assistance affects coding skill formation reaches the same conclusion: "Cognitive effort — and even getting painfully stuck — is likely important for fostering mastery."

The other face of the skills gap is the **right to refuse**. An employee at an Australian sports organization resigned<sup><a href="12-appendix-a-sources.md#8-78">[8-78]</a></sup> after her request to opt out of Copilot was denied in writing ("you are not entitled to ask that your work not be accessed by our AI systems"); surveys show roughly 35% of employees are uncomfortable with AI adoption, and an individual's exit neither stops the AI nor stops "employees training the AI that replaces them." An organization that designs only "how everyone uses AI" but not "who has the right to refuse, and what refusal costs" will see hollowing-out take another form: talent voting with their feet.

## 6.6 Innovation Density: The Organization Wins

DeepSeek: 160 people vs OpenAI: 3,500 / Anthropic: 3,000 / DeepMind: 8,100; Moonshot delivered a trillion-parameter model with 300 people and 1% of the industry's compute.

> **In the AI era, more people does not mean stronger — innovation density is the ultimate competitiveness, and innovation density is not built by stacking people; it is engineered through organization.**

This fully corroborates the Tencent formula: high talent density × high AI leverage ÷ low organizational friction = 160 people beating 3,500.

## 6.7 Enable vs Replace: A Debate Already Settled by the Data

On the relationship between AI and people, there are two strategies:

- **Replacement automation**: positioning AI as a tool to "cut headcount, cut costs, boost efficiency" — breeds employee resistance, collapsing trust, tacit knowledge loss, and stalled innovation; it looks like saving money in the short term but destroys core organizational capability in the long term;
- **Augmentative collaboration**: AI handles the transactional layer while humans focus on judgment, creation, and relationships.

The data has already settled the debate:

- 2026 Gallup and PwC research: an **"enable employees" strategy can raise retention by about 32%**, with innovation capability and performance significantly ahead;
- Asana (2025): 64% of employees consider AI agents unreliable<sup><a href="12-appendix-a-sources.md#8-34">[8-34]</a></sup> and call for more training, clarity, and guardrails — nearly half of employees are anxious about job loss (Accenture);
- Microsoft WTI 2026: **organizational factors (culture, manager support, talent practices) contribute 2x as much to AI impact as individual effort<sup><a href="12-appendix-a-sources.md#7-71">[7-71]</a></sup>** — employees are not the bottleneck; the organization is;
- Business Week (2026): 55% of companies that laid people off because of AI regret it (Orgvue survey).

## 6.8 Role Fusion: Those Who Own Results Should Not Be Boxed in by Job Titles

The biggest obstacle to enterprise AI adoption is not technology but organizational inertia<sup><a href="12-appendix-a-sources.md#8-73">[8-73]</a></sup>. Traditional organizations function on two premises: work can be fully divided into standardized nodes, and employees only need to be responsible for their process node while the organization backs the final result. AI changes exactly these premises — when document work, design, and parts of coding can be done by AI at lower cost and higher stability, the value of many roles is revalued and role boundaries blur: a product manager builds a demo with AI, a designer generates front-end pages directly, a developer joins product judgment with AI's help.

This is not one role replacing another — it is **Role Fusion**: the people who will be more valuable are no longer responsible for a single process node but can go from a user problem to full implementation and own the final result. The disruption follows: one person can span steps that previously required handoffs and produce something much closer to the outcome, yet the organization still manages people by job title, breaks tasks down by process, and accepts deliverables by node — "the people who actually get things done take on more responsibility but are still evaluated inside their old job boxes."

Role Fusion must be paired with results-oriented incentives, changing three dimensions at once: **authority** — give fused roles decision rights that span steps; **reward** — allocate by final results and user value rather than job level; **growth** — provide career paths that cross traditional functional boundaries. Otherwise the people who truly achieve Role Fusion will quickly feel the unfairness, and most will leave for teams that can recognize this kind of capability.

The hiring market already shows the corresponding gap: enterprises do not want people who can call APIs and write agent loops; they want people who can turn model capability into **stable services** — monitoring, evaluation, iteration, cost, latency, stability, and human review after launch each require engineering discipline; the real bar is turning a demo into a low-latency, observable, maintainable service that can enter enterprise processes. That is why the hybrid roles in demand are the **product engineer and the business-minded technical consultant** — they may not only know models, but they know how to turn a vague requirement into model inputs and outputs, translating back and forth between business and engineering.

## 6.9 The Core Judgment of This Chapter

The direction for restructuring incentives and talent is clear: **evaluation from input to output, incentives from position to results, management from control to calibration, talent from quantity to density, AI from replacement to enablement.** No single dimension can be solved by "just paying more" — but for every dimension, a set of organizations has provided reference answers. In Chapter 9 we will see: organizations that do not address the people problem are doomed to fail their transformation.
