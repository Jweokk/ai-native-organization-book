# Chapter 5: Redesigning Workflows and Decisions

## 5.1 Redesign First, Automate Second

In 1990, Michael Hammer published a famous article in the *Harvard Business Review* titled "Don't Automate, Obliterate." His core point is even more applicable in the AI era: **before automating a bad process, ask why that process exists in the first place.**

The first principle of AI-native workflow redesign is: **not "give everyone a chatbot," but redesign how work flows, how decisions get made, how data is captured, how humans review risk, and what AI is allowed to assist with or act on.**

The fundamental difference between an automation-first organization and an AI-native organization:

| Question | Automation-first organization | AI-native organization |
|------|--------------|--------------|
| Starting point | Where can we add AI? | **What work should change?** |
| Success metric | How many tasks were automated / how many prompts were used | Whether the outcomes of the whole workflow improved |
| Main risk | Faster rework | Discovering redesign gaps before scaling |
| Data approach | Use existing data | Redesign data capture around decisions |
| Human role | Post-hoc reviewer | Responsible designer, supervisor, and owner of exceptions |
| Scaling pattern | More tools and pilots | A repeatable workflow-redesign loop |

## 5.2 Nine Key Workflow Redesigns

**1. Start from business outcomes, not AI tools.** Outcomes must be specific enough to guide trade-offs: "30% fewer supplier-invoice exceptions without adding approval risk" beats "use AI in finance." Technology choices follow workflow intent.

**2. Map the real workflow before automating the official one.** The official process diagram and how employees actually work (inbox shortcuts / private spreadsheets / informal escalation paths / exception handling) exist side by side as two versions. Delete steps before automating: merge duplicate approvals, turn low-value checks into rules, give exceptions an owner. **Don't teach AI to preserve unnecessary work.**

**3. Redesign intake so AI gets better input.** Many AI projects die at the door: expecting AI to classify, route, or decide on messy input that was never designed for it. Required fields, structured options, validation at capture points, automatic enrichment from trusted systems, and flagging low-confidence cases. **Don't blame the model for weak input before redesigning the front door.**

**4. Separate rules / automation / AI assistance / agents / humans.** Not every step needs AI: stable rules → rule automation; system handoffs → workflow automation; language-intensive review → AI assistance; pattern recognition → AI models; low-risk multi-step tasks → constrained agents; high-accountability decisions → human plus AI support. Prevent two errors: using AI where rules suffice, and delegating high-risk decisions just because AI can generate confident-sounding suggestions.

**5. Build a workflow data foundation, not an abstract data lake.** Ask "have we captured the data needed to make the workflow better?" rather than "do we have data?" Record when humans override AI suggestions and why — the best learning comes from the redesigned workflow itself.

**6. Define decision rights before AI systems act.** If humans aren't clear on decision rights, AI is even less safe. The decision rights table is the tool that operationalizes this:

| Scenario | What AI may do | What humans retain |
|------|------------|------------|
| Classification / routing | AI acts on high confidence | Humans review low-confidence cases |
| Drafting | AI recommends drafts | Humans approve sensitive content; template and tone control |
| Low-value refunds | AI acts within limits | Humans review over-limit cases; thresholds + logs + fraud checks |
| Contract changes | AI assists only | Humans decide |
| Risk escalation | AI acts immediately | Humans investigate and close |

**7. Replace manual handoffs with event-driven work and review queues.** **Stop treating people as glue between systems.** Trigger → create record → enrich → apply rules → AI classify/summarize → route → exceptions enter a visible review queue (with context/priority/owner/deadline/escalation path). Don't make handoffs invisible; make important handoffs observable.

**8. Measure the whole workflow, not AI tasks.** Task-level time savings mislead (drafting got faster but review got slower; classification got faster but the queue got wrong). Metrics: cycle time, first-time-right rate, exception rate and exception age, review time, satisfaction, cost per completed case, rework rate, AI confidence and coverage, escalation quality, incidents/control violations. **After the pilot, ask: did the work improve, or did AI just make one step look faster?**

**9. Create a repeatable 90-day workflow-redesign cadence.**

**Processes themselves can be redesigned: a review system is not the same thing as a PR.** Amp, a 20-person team, pushes straight to main without pull requests and still passes SOC 2 — auditors never cared about the git workflow; they care that changes are authorized, tested, approved, and recorded. Their control stack: push permissions restricted by business function, signed commits (GitHub verified), fully automated CI validation, and an audit trail linking commits to business context. The scaling insight: risk is not uniform inside an enterprise, and calibrating every system to "the scariest one" is hidden waste — first ask "what risk is the PR actually managing," then decide where it is needed.

## 5.3 The 90-Day Redesign Cadence (The Actionable Core)

- **Days 1–15: Select** — a process with visible pain + measurable value + sufficient volume + controllable risk;
- **Days 16–30: Map** — the real workflow / systems / data / decisions / handoffs / approvals / exceptions / owners / current performance;
- **Days 31–45: Redesign** — delete steps, clarify ownership, define decision rights, standardize intake, improve data capture, assign people / rules / automation / AI / agents to each step;
- **Days 46–60: Build** — workflow / integrations / prompts / access control / review queues / dashboards / logs / training;
- **Days 61–75: Pilot** — real users run real cases inside safe boundaries, measuring the whole workflow;
- **Days 76–90: Govern and scale** — kill / fix / scale, record the lessons, pick the next process.

## 5.4 Eight Common Mistakes

① Treating AI access as transformation; ② automating before simplifying (AI accelerates work of the wrong shape); ③ using AI where rules suffice; ④ ignoring exception work (the real value lies in handling messy cases); ⑤ measuring prompts instead of outcomes; ⑥ excluding employees from the redesign; ⑦ giving agents power without control (requires thresholds / logs / permissions / review queues / rollback / named owners); ⑧ redesigning the whole company at once (start with one process).

## 5.5 Dividing Labor Between Humans and AI: From "Full Replacement" to "Three-Layer Routing"

Beyond workflow redesign, designing the boundary of human–AI division of labor is the core of decision redesign.

**Anthropic's internal evidence gives a key number: most employees believe that only 0–20% of work can be "fully delegated" to AI.** In other words, the human–AI division of labor in an AI-native organization is "supervised collaboration," not "hands-off automation." The number of autonomous actions Claude Code could take before human intervention was needed grew from about 10 to about 20 — this "intervention threshold" is dynamic and moves as model capability improves.

The hybrid-model **three-layer routing** that Klarna distilled from its customer-service reversal is currently the most mature template for dividing labor:

- **Layer 1: AI handles routine volume end to end** (targeting 60–70% of traffic) — order status, basic returns, FAQs;
- **Layer 2: AI-assisted human** (AI drafts, human reviews and sends, 20–25%);
- **Layer 3: Human-led high-value / escalation scenarios** (5–15% of traffic, but the greatest retention impact) — complex billing disputes, fraud, account cancellation.

**Lesson**: Klarna's first round of AI customer service only did Layer 1 (and did it aggressively); overall volume-based metrics (resolution rate, first-response time) looked good, but CSAT for complex interactions dropped significantly and the repeat-contact rate rose — the overall average masked a quality collapse in retention-critical scenarios. **You must track satisfaction for "complex/escalation interactions" separately.**

**Treating AI as a compiler leads to frustration; treating it as a collaborator works.** One engineer's observation is worth remembering: code gives certainty (same input, same output; a difference is a bug), humans give uncertainty (a colleague may understand intent and produce a better result), and AI sits between the two — rather than treating it as a compiler that precisely executes instructions, collaborate with it the way you would lead: share context, explain the desired outcome, set boundaries, respond to feedback. The core shift is investing in **expressing intent** — explaining why the work matters, what a good result looks like, and where judgment is needed. "The technology is new; leadership is not." This is also the underlying capability for the "human–AI division of labor design" in Chapter 8.

## 5.6 Corroboration with Chinese Practice

The three common features from Chapter 2 (AI-informed decisions replacing experience-based decisions, unifying business flow and workflow, making expertise reproducible) all have concrete implementation mechanisms in this chapter:

- **AI-informed decisions**: Huawei (Chinese: 华为) makes intelligent analytics a default capability of its data platform — "you don't go query it; the system gives it to you automatically";
- **Unifying business flow and workflow**: Feishu (Chinese: 飞书; Lark internationally) connects IM, documents, and business flows, with AI intervening in project nodes in real time;
- **Making expertise reproducible**: Transn's (Chinese: 传神) AI automatically records decision logic and updates business rules, turning personal experience into organizational assets — at the same time, Yang Renbin's "decision model index" from Chapter 4 (modeling the decision layer's judgment methods as a callable system) and the decision rights table are two sides of the same coin: one is the governance side, the other the cognition side.

## 5.7 The Core Judgment of This Chapter

**Workflow redesign is the minimal executable unit of the AI-native organization.** Organizational form (Chapter 4) is the skeleton; workflow redesign is the muscle — an organization doesn't need to finish "organizational restructuring" before becoming AI-native; it only needs to start with one workflow: map the real process, delete redundant steps, define decision rights, design for production, measure the whole flow, and iterate in 90-day cycles. **Reduce organizational friction (the denominator) first, then multiply talent and AI leverage (the numerator).** In the next chapter, we take on the hardest variable: people.
