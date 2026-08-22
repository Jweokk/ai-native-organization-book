# Chapter 9: Challenges, Risks, and the Future

## 9.1 Failure Cases: Transformations Done Wrong, and Ones Never Got Around To

**Klarna's reversal** (detailed in Chapter 7) is the most complete sample of a "transformation done wrong": AI customer service loudly replaced 700 people → quality collapsed in complex interactions → quietly switched back to human agents. Five lessons:

1. **Blind spots in the business case**: only labor-cost savings were counted; revenue loss, repeat-contact costs, and the "cancellation cost" (after publicly announcing that the work was automated, strong candidates no longer wanted to join) were not;
2. **Experiential knowledge cannot be rebuilt**: the tacit knowledge senior agents used to handle edge cases disappeared permanently when the teams were cut;
3. **Metric choice determines success or failure**: overall averages masked the quality collapse in retention-critical scenarios;
4. **A viable hybrid model**: three-layer routing (60–70% / 20–25% / 5–15%);
5. **Industry-wide contagion**: fintech, healthcare support, and insurance claims all show the same pattern of "full automation → quality degradation → quietly backfilling with humans."

**Samsung's Shadow AI incident**: in April 2023, three incidents in 20 days of employees uploading sensitive information (semiconductor equipment measurement data, source code) to ChatGPT led Samsung to ban generative AI outright and build its own alternative. **A "throw-the-baby-out-with-the-bathwater" ban sets the transformation back; the right posture is to provide a managed, enterprise-grade AI environment, offsetting Shadow AI with alternatives rather than bans.**

**Microsoft Copilot's licensing dilemma**: about 64% of enterprise Copilot licenses sit unused, and only 3.4% of M365 customers pay for advanced AI features; 72% of IT leaders say employees struggle to integrate Copilot into their daily workflows. **Between the purchase decision (made by the CIO) and the usage decision (made by frontline employees) stand three gates of organizational inertia — whether processes have been redesigned, whether leaders model the behavior, and whether performance reviews are tied to it: procurement ≠ adoption, and licenses ≠ value.**

**Chegg's cost of not transforming**: in May 2023 it admitted that ChatGPT had taken its student users; the stock plunged about 50% in a single day, followed by multiple rounds of layoffs, with the stock cumulatively down about 99% from its peak. Chegg's problem was not "doing the transformation wrong" but "not getting to the transformation in time" — its core business model (paid homework answers) was zeroed out directly by free LLMs. **There is a time window for building an AI-native organization.**

## 9.2 Five Root Causes of Failure

| Root cause | Representative case / data | Characteristic signals |
|------|-------------|---------|
| Environment mismatch (the enterprise was never designed for AI) | Pilots succeed, production always collapses; MIT 95% | Pilots held together by manual patching; collapse in production |
| Replacement mindset (layoffs first) | Klarna; "replacement-style automation" | Satisfaction/retention deteriorate; quietly rehiring |
| Procurement ≠ adoption (organizational inertia) | Copilot 64% of licenses idle | License costs sunk, low activity |
| Missing data and governance foundation | 60% of projects abandoned over data; Samsung leak | Shadow AI rampant; projects blocked by data |
| No value accounting | Only demos and usage rates, no P&L numbers | "Pilot boom, value void" |

## 9.3 Six Systemic Risks

1. **Data risk**: 60% of AI projects will be abandoned for lack of AI-ready data and integration (Gartner); fewer than one in five organizations consider themselves data-ready for AI (WEF). WEF's warning is worth remembering: **"garbage in, garbage out — just faster"**;
2. **Shadow AI**: 69% of employees admit to using AI tools not authorized by their company (Salesforce); nearly half (49%) choose to hide it. **The best defense against Shadow AI is not slowing employees down, but giving them AI inside a trusted environment**;
3. **Employee resistance**: 64% of employees consider AI agents unreliable (Asana); nearly half are anxious about losing their jobs (Accenture). "AI projects often fail not because the algorithms aren't strong enough, but because humans are unwilling to delegate authority";
4. **Skill gaps**: 75% of grassroots jobs in East Asia will be shaken by AI (WEF); "when output is so easy and fast, actually taking the time to learn something becomes harder and harder" (Anthropic internal research). **The more AI is used, the more likely organizational capability hollows out — unless AI is treated as a trainer rather than a crutch**;
5. **Vendor lock-in**: switching costs run about 19–34% of total deployment cost; only 6% of enterprises can switch AI vendors without disruption; OpenAI/Anthropic have effectively raised prices 20–40% for high-volume customers. **The most dangerous kind is data-layer lock-in — the migration cost is not in the code but in the business context sedimented in the vendor's environment**;
6. **The cost trap**: a single interaction is cheap ($0.5–2 vs. $6–13.5 for a human), but Gartner predicts that by 2030 the per-resolution cost of generative AI will exceed $3, surpassing many B2C offshore human agents — because repeated attempts on complex interactions, human takeovers, quality checks, operations, and compliance costs keep pushing the true cost up. **Counting only inference cost while ignoring system cost and reversal cost are the two blind spots of ROI models.**

## 9.4 The Counter-Data We Must Face

Two sets of counter-data selectively ignored by the AI-native narrative must be put on the table in this book:

1. **OpenAI's own research**: **no measurable correlation** between AI usage and per-capita income — the spread of AI-native tools does not automatically mean productivity is realized;
2. **Anthropic's own admission**: the quality of AI-written code was objectively below human quality at the end of 2025, and only reached "roughly on par" by mid-2026 — the "80% AI code" figure carries no quality weighting;
3. **Microsoft WTI 2026**: the average 15% productivity gain from AI is distributed extremely unevenly — less-experienced workers gained +34%, while top performers gained almost nothing.

Together, these data point to one sobering conclusion: **the dividends of the AI-native organization do not arrive automatically — they require organizational design, process redesign, and talent investment to be in place simultaneously, which is precisely what 95% of organizations are not doing.**

## 9.5 The Future: Three Directions We Can Expect

**1. Agents become a "digital workforce."** A Gartner survey: by 2030, CIOs expect 0% of IT work to be done by "humans without AI," 75% by "human + AI augmentation," and 25% by AI agents independently. Microsoft WTI 2025: 82% of leaders are confident about expanding capacity with a "digital workforce." **"Managing agents" will become a new job skill** (expected by 36% of leaders).

**2. Organizational forms keep evolving.** The 10:1 human-to-AI ratio is only the starting point (WEF); Block's World Model and the "Organizational Brain" (Yang Renbin) point in the same direction — AI takes on more and more coordination and information-routing functions, while humans focus on judgment, creation, and relationships. **But remember the warning from Chapter 4: speed is not intelligence; speed without integration is just faster blindness.**

**3. Pullbacks and reversals become the norm.** Klarna returning to human agents, Duolingo rescinding its memo, the Sam incident at Cursor — AI-native is not a "switch" to be flipped but a process of continuous calibration. **Organizations that can accept reversals and treat them as data are closer to reality than organizations that claim one-step arrival.**

## 9.6 The Core Judgment of This Chapter

Building an AI-native organization is, in essence, a **reorganization of organizational capabilities**: hand information routing to AI, leave judgment to humans, sediment experience into assets, and shift reviews from input to output. It fails on five root causes and succeeds on five patterns (Chapter 8), and the watershed that decides success or failure is always the same question: **are you applying AI as a band-aid to a legacy organization, or growing AI into the organization's DNA?**

This book offers no standard answers — it provides a map. A map won't walk for you, but at least it lets you know where 95% of people died.
