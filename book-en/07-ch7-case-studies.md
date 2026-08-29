# Chapter 7: Case Studies — AI-Native Organizations in China and Around the World

This chapter is the factual foundation of the book. Every case covers organizational form, on-the-ground practices, quantified results, and controversies and dissenting voices. **Official claims and third-party verified reporting are labeled separately** — because in the AI-native narrative, the tension between the promotional surface and the factual surface is itself the most important research material.

## 7.1 Chinese Cases

### Transn (Chinese: 传神) — "Rather Than Wait for Employees to Become AI Experts, Grow AI Capability into the Organization"

Translation company Transn's AI-native practice is the most complete Chinese model available today. It runs on several key mechanisms:

- An AI Native decision committee organized by business line (Language Intelligence Group / Industry Intelligence Group / Brand & Sales Group), each with a clear lead and clear progress goals — AI is not the technology department's business; it is each business line's own business;
- A "DEMO rule": every AI project must have a runnable DEMO and clearly state which business problem it solves — this one rule killed 90% of PPT projects;
- An "AI joint fleet": 20+ cross-departmental business teams build their own AI applications, so that AI applications grow inside business scenarios from day one;
- Backed by the "Energy Gold" incentive mechanism — a colleague-validated incentive credit (detailed in Chapter 6).

Founder He Enpei's judgment: **"Rather than wait for employees to become AI experts, it is better to grow AI capability into the organization."** Individuals come and go; organizational capability stays.

### Huawei / Alibaba / Feishu — Three Common Traits of Organizational AI-ification

- **Huawei**: AI embedded across the entire data lifecycle, with intelligent analysis becoming the default capability of the data platform ("You don't go looking for it; the system delivers it to you");
- **Feishu (Lark internationally)**: a collaboration suite connecting IM, documents, and business flow, with AI intervening in project milestones in real time rather than summarizing afterward;
- **Alibaba**: AI-informed decisions replacing experience-based decisions — as data flows through, AI automatically analyzes, warns, and pushes decision recommendations.

### DeepSeek — The Ultimate Example of Innovation Density

160 people built a trillion-parameter model. Compare with the scale of peers: OpenAI 3,500 people, Anthropic 3,000, DeepMind 8,100. Organizational design (rather than stacking headcount) determines innovation density — this is the strongest case for the "innovation density" thesis of Chapter 6.

### Jingzhunxue (Chinese: 精准学) (Yang Renbin) — The Organizational Brain

Injecting the highest cognition into the front line: AI Chief of Staff + decision model index + context engineering. AI coding is only 0% or 100% (engineers are not allowed to modify code themselves; humans only provide feedback); anti-documentation, anti-group-chat; Context is Everything. (See Chapter 4 for details.)

### MarsWave (Chinese: 火星电波) — Completing an AI-Native Transformation in 5 Weeks

The OPC model (human judgment / AI code / manager macro-decisions) + Soul Team (personality and emotional output) + a unified repository as the AI's context + a rhythm of front-load thinking and back-load review. (See Chapter 4 for details.)

### Mininglamp Technology (Chinese: 明略科技) — Six Patterns of Enterprise Multi-Agent Collaboration

Mininglamp was one of the first Chinese vendors to productize "multi-agent collaboration," and its architecture guide published in 2026 offers the most complete enterprise-level multi-agent collaboration design framework to date, mutually corroborating Anthropic's multi-agent research in Chinese and English.

**Three-layer infrastructure**: a unified identity registry (every agent has a unique identity and permissions), a shared context mechanism (converging unstructured discussions in IM into structured knowledge: brief / timeline / deliverables / rejection records / acceptance status), and a task orchestration engine (split / serialize / parallel / compete).

**Information topology controls visibility** — "see each other when they should, stay blind when they should": a payroll agent should not broadcast its intermediate results to a weekly report agent. Group-chat-style information architectures can only achieve "everyone sees everything"; they cannot deliver programmable visibility boundaries.

**Six collaboration patterns** (nestable and combinable): Solo (working alone); Roundtable (mutual visibility — all agents share context); Critic (generate-review, with the reviewer holding veto power); Pipeline (strict serial — upstream output is downstream input); Split (divide-and-conquer in parallel — subtasks stay blind to each other and merge after each delivers); Swarm (competition selects the best — multiple candidates produce in parallel, redundancy traded for quality).

Implication for organizations: multi-agent is not "opening a few more windows" — you first decide the information topology and collaboration patterns, and only then talk about model capability. This aligns with the conclusion of the Anthropic multi-agent experiments in Chapter 9: **coordination does not naturally emerge from stronger intelligence.**

New data from mid-2026 continues to confirm this direction: IDC reports that 68% of leading enterprises put autonomous agents on their IT procurement priority list, yet more than 60% of pilots remain stuck at the production stage; a CAICT (信通院) survey of 358 enterprises found 67% reporting "coordination costs higher than expected." In July 2026, Beijing issued the first provincial-level agent policy, setting three bottom lines — "traceable, auditable, controllable" — with up to CNY 100 million in industry support. Organization-level multi-agent collaboration is moving from vendor practice to a regulatory topic.

### More Chinese Practice

Jimo (Chinese: 极摩) (AI-native organizational architecture), Moka (AI-native HR: 3 AI colleagues), Atlassian's China practice (AI-native PM) — case details in Chapter 4 and the appendices.

## 7.2 International Cases

### Klarna — The Most Complete Control Group for AI-Native Transformation

Klarna's AI transformation is the most important retrospective sample in the industry today.

**Organizational form**: full-time headcount fell from 5,527 in December 2022 to 3,422 in December 2024 (−38%) — the path was a hiring freeze plus natural attrition since 2023 (natural attrition of 15–20% per year), not a one-off mass layoff [IPO prospectus data].

**On-the-ground practices**: externally — an AI customer service built on OpenAI technology launched in February 2024, handling 2.3 million conversations in its first month, about two-thirds of total customer service chat volume; internally — AI assistant Kiki has answered more than 250,000 employee questions, used by 85% of employees, and the legal department drafts contracts with ChatGPT Enterprise in about 10 minutes instead of about 1 hour [official claims].

**Quantified results**: the two yardsticks must be placed side by side. Officially, Klarna claimed the AI customer service would bring $40 million in profit improvement in 2024, and by Q3 2025 upgraded the claim to the equivalent of 853 full-time employees and $60 million in cumulative savings, with revenue per employee of $1.24 million (3.6 times the 2022 figure); third-party comparisons show that even counting the $60 million in savings, Q3 2025 customer service and operations costs of $50 million were still higher than the $42 million a year earlier — "AI cost reduction" and "rising customer service costs" coexisting.

The controversy and reversal deserve the closest attention: after loudly publicizing "AI replacing 700 customer service agents" in 2024, Bloomberg reported in May 2025 that Klarna was **switching back to human agents** — the CEO admitted that going all-in on AI had degraded service quality, and planned to rehire human agents under "Uber-style" flexible employment. CSAT on complex interactions declined markedly and repeat contact rates rose; the overall averages masked a collapse in quality in retention-critical scenarios.

Lesson: AI-native does not equal a one-off mass layoff; purely cost-driven AI replacement has limits; "over-rotation" requires correction. 55% of companies that laid off employees due to AI regret it (Orgvue 2025).

### Shopify — Layoffs First, Then AI-Powered Growth

Shopify's layoffs and AI-ification are two separate things, and order matters: 14% layoffs in July 2022, 20% in May 2023 (about 2,000 people; officially attributed to selling the logistics business and slowing growth — **not AI replacement; AI-ification came after the layoffs**). Headcount then stayed flat for multiple consecutive quarters: about 8,300 at the end of 2023 → about 7,600 in 2025, with revenue per employee rising from $1.1 million to $1.52 million.

April 2025 CEO Tobi Lutke memo: employees must first prove "AI can't do this job" before applying for additional headcount; AI usage is included in performance reviews. More than half of merchant interactions with Support are AI-assisted and often fully resolved by AI. Internal productivity platform Shopify OS aggregates business data and recommends the resources and skill configurations a project needs.

Controversy: the memo was read as a "layoff filter" rather than a productivity plan. "Layoffs before AI" versus "AI-driven layoffs" is the key distinction for understanding Shopify.

### Anthropic — Eating Its Own Dog Food First

Organizational form: about 2,500 people (2026), no mass layoffs — an "AI-native expansion" organization.

On-the-ground practices (official report *Recursive Self-Improvement*): more than 80% of merged production code is written by Claude (May 2026); code output per engineer per quarter is **8x** the 2021–2025 baseline; engineers' roles shifted from "writing code" to "architect + judge" — AI automated code review embedded in CI/CD has intercepted about one-third of downtime-class production bugs in claude.ai's history.

Dissenting voices (also from internal research): the quality of AI-written code was objectively below human-written code until late 2025, reaching only "roughly on par" by mid-2026; employees self-report that 60% of their work uses Claude with 50% productivity gains, but 27% of AI-assisted work was "things they wouldn't have done anyway" (exploratory work), and most employees believe only 0–20% of their work can be "fully delegated" to AI; some employees went "about five months without writing code by hand" and worry about skill atrophy and a sense of meaninglessness — the psychological cost of being AI-native is real.

### OpenAI — The Highest-Resolution Sample of Whole-Organization Agent-ization

On-the-ground practices (official economic research *How Agents Are Transforming Work*): Codex has become the primary work tool for every department (including legal, finance, and recruiting), accounting for **99.8%** of the company's weekly output tokens; the average engineer runs 99% of output tokens through Codex; the heaviest users orchestrate 60+ hours of agent work time in a single day (multi-agent in parallel); 80.6% of sampled users have had Codex execute tasks estimated to require more than 30 minutes of human work.

The most important counter-evidence comes from Fortune (August 2026): OpenAI's own economic research shows **"no measurable correlation between AI usage and revenue per employee"** — the spread of AI-native tools does not guarantee that productivity will be realized. Even the maker of AI tools itself cannot produce evidence that "the more you use, the more you earn."

Latest development (Wired, August 2026): OpenAI appointed Codex lead Thibault Sottiaux to take over the entire ChatGPT product line; ChatGPT will transform into a "personalized agent super-app" driven by Codex at its core (a 40-person team, folded into ChatGPT within weeks). Its self-attribution is worth noting: the earlier failures of Operator/ChatGPT Agent were attributed to "too early, models unreliable" plus users not knowing what to do with agents; the new strategy is small, fast releases — "you can't do a big splash and then get it wrong." **Even the most aggressive agent-ization sample is hedging against the uncertainty of agent products with small, fast releases.**

### Notion — A Thousand People, No Layoffs, AI as the Second Growth Curve

About 1,000 people, no layoff record. ARR surpassed $600 million in December 2025, **roughly half of it from AI products**; paid AI add-on penetration rose from 10–20% in 2024 to over 50% by September 2025. Notion AI launched in November 2022 (about two weeks before ChatGPT's public launch). Its path is product-driven rather than organization-slimming — driving paid penetration through AI features rather than through layoffs.

### Cursor — King of Revenue per Employee

About 300 people: ARR $100 million in January 2025 → $500 million in June → $1 billion in November → about $4 billion by June 2026; revenue per employee of $3–13 million. In June 2026, SpaceX announced an all-stock acquisition at a $60 billion valuation (completed in August, folded into SpaceXAI).

Controversy: in April 2025, AI customer service program "Sam" fabricated and executed a nonexistent login policy, causing users to cancel their subscriptions — a textbook incident of "an AI agent acting beyond its authority."

### Duolingo — Zero Full-Time Layoffs and 11x Content Production

In January 2024, Duolingo cut about 10% of its contractors (outsourced translation and content production) and switched to generative AI for content; the CEO said the company has **never laid off a single full-time employee** since its founding in 2009. Content production: 1,800 course skills per quarter in 2024 → 7,100 in 2025 → 20,500 in Q1 2026 alone — about 11x in two years, which the company explicitly says "wouldn't have been possible without AI."

Controversy: the contractor cuts triggered a PR crisis (large-scale TikTok/Reddit discussion of "replacing workers with AI"); after the April 2025 AI-first memo sparked layoff speculation, the CEO publicly clarified, and in May 2026 the memo was reported to have been retracted. **The first cut of AI replacement lands on the most vulnerable flexible workers — a pattern that holds across cases.**

### Airbnb — 60% of Code Co-Written by AI

No AI-related layoffs; Q1 2026 earnings call: **60% of engineer-produced code is co-written with AI** (Google claims 30%+, Microsoft up to 30% — Airbnb is at the high end of public claims); the AI customer service bot handled 40% of customer service tickets without human escalation in Q1 2026 (from about 33% in early 2025), with plans to expand to 50+ languages.

Dissenting voice (the CEO's own admission): Chesky publicly acknowledged that "no one has truly solved the AI travel problem," listing the chatbot's four major flaws (text overload, inability to operate directly, difficulty comparing, and mismatch in multi-person booking scenarios).

## 7.3 Cross-Case Comparison: Six Patterns

1. **Three organizational paths coexist**: downsizing (Klarna), expansion (OpenAI/Anthropic), steady-state leverage (Shopify/Duolingo/Airbnb) — there is no single answer;
2. **The "first cut" of AI replacement lands on flexible labor**: Duolingo's contractors, Klarna's outsourced customer service — full-time layoffs are actually rare;
3. **Evaluation systems are being reshaped by AI**: Shopify (AI in performance reviews), Duolingo (AI-first memo);
4. **The tension between claims and verifiable data is the most valuable part of this book**: Klarna ($60 million in savings coexisting with rising customer service costs), OpenAI (its own research: no correlation between AI usage and revenue per employee), Anthropic (AI code quality was once below human quality) — the promotional surface and the factual surface must be placed side by side;
5. **Reversals and backtracking are the norm**: Klarna switching back to human agents, Duolingo retracting its memo, Cursor's Sam incident — no company's AI-native transformation is a straight line;
6. **Extremes in revenue per employee**: Cursor (300 people, $4 billion ARR) is the ceiling sample for small teams; Klarna ($1.24 million per employee) is the sample for large-organization transformation — the shared financial trait of AI-native organizations is per-capita output well above peers.
