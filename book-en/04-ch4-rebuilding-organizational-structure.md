# Chapter 4: Rebuilding Organizational Structure — From Hierarchy to Network

## 4.1 The Legacy Organization's Deadlock

Linear division of labor has exposed a fundamental contradiction under AI acceleration:

| The old way | The new contradiction |
|--------|--------|
| Managing people by role | The people who can actually get things done span multiple roles |
| Breaking work down by process | AI completes in a day what used to take a week of milestones |
| Accepting deliverables at checkpoints | Deliverables themselves become "intermediate artifacts"; only the final outcome is value |
| Reporting and evaluation by rank | Those who take on fused roles don't receive the corresponding authority and rewards |

> When one person can use AI to leap over steps that previously had to be handed off, and produce something closer to the final outcome, the legacy organizational framework becomes a constraint.

The core proposition of restructuring organizational form is: **use AI to replace the coordination and information-routing functions that hierarchy used to perform, so that humans can focus on judgment and creation.**

## 4.2 MarsWave: Five Practices of a Small Team Building from Zero

A small company called MarsWave (Chinese: 火星电波), which pivoted from ListenHub, completed its AI-native transformation in five weeks. Its five practices are the most concrete Chinese sample of "what an AI-native organization looks like":

**1. Vibe coding shocks the organization.** The CTO used Claude Code to build version 0.1 alone overnight — ideas could be presented directly. Before: product requirements → PRD → review → development → testing → release (weeks). Now: say it to AI → see the result → iterate (hours). Alignment shifted from "long documents" to "seeing the prototype directly."

**2. The OPC model (human–machine–macro decision).** Humans handle judgment (what to do, why, whether it's good), AI writes 99% of the code (how to write, how to implement), and managers make macro decisions (direction, resources, cadence). **Humans don't manage processes or schedules; they manage judgment, quality, and review.**

**3. The birth of the Soul Team.** The first core role that was neither engineer nor product manager — responsible for the product's **personality and emotional output**; its lead has a media background and can't code. Insight: once AI can handle "feature implementation," humans' differentiating value shifts to the "human-like" parts — empathy, personality, warmth.

**4. A tool revolution.** Linear, Notion, and kanban boards were abandoned; all code moved into a unified repository with no permission barriers. The repository "isn't for humans to read — it's for AI to read as context." The CEO's ideas go directly to AI, are automatically organized into Markdown, and become development context. **Essence: AI becomes the intermediary of information transmission, instead of layer-by-layer transmission between people.**

**5. A new rhythm of front-load thinking and back-load review.** In the first few days of each month the whole team stops writing code to align on plans; at month's end they re-review the code, cutting and refactoring. "Faster isn't necessarily better" — rhythm matters more than speed.

**The failed experiment matters just as much**: before the formal transformation, there was the "Task Tavern" (a task bulletin board where anyone could pick up any task) — a programmer's two-day new feature reached 80,000 users on launch day, but under business pressure the strongest people were pulled back to old tasks, and it ultimately failed. Lesson: **process improvement (patching the old framework) isn't enough — you have to design from scratch.**

## 4.3 Shmool: A CEO's Firsthand Subtraction in a Mature Organization

Unlike MarsWave (building from zero), Itay Shmool's case is about **subtraction within an existing organization** — dismantling the traditional hierarchy (VP → Director → Manager → Team Lead) into a single-layer AI-native organization. Core numbers:

| Metric | Before | After |
|------|--------|--------|
| Decision latency | Days to weeks | Hours |
| Information fidelity | ~60% (decays with each transfer) | ~95% (direct transfer) |
| Builder-to-manager ratio | 3:1 | 8:1+ |
| Meeting overhead | ~30% of work week | ~10% of work week |

Three key insights:

1. **The truth about middle management**: many middle managers are not "redundant layers" — they are excellent builders themselves, just pulled into coordination work by the old structure. Give them the chance to build again and they thrive. **Distinguish the management function from the managers themselves — the function can be automated, but people should not be simply removed.**
2. **Guild Masters replace management**: once management layers are removed, a new mechanism is needed to maintain professional standards. Guild Masters are **expert roles** (not management roles) who sit within teams and set standards across teams — they create no new reporting lines and are "the quality immune system of a flat organization."
3. **The AI platform is a precondition**: flattening without AI infrastructure equals chaos, not lean. Five core capabilities: self-healing systems, an AI creative engine, a unified experimentation platform, automated code review, and operations AI agents. **"The AI platform is what replaces coordination — this is non-negotiable."**

The human side of the transformation matters just as much: "Behind every box in the architecture is a person with a mortgage, a family, and a career. **How you treat the people who leave defines your culture more than how you treat the people who stay.**"

## 4.4 Block: Replacing Hierarchy with a World Model

Block, the payments company (Jack Dorsey), offers the large-company version of the framework: **use AI to replace the coordination functions hierarchy performed, and build the company as an agent.**

Block's four-layer architecture:

```
┌──────────────────────────────────────────┐
│   Interfaces (Square / Cash App, etc.)   │  ← delivery surface
├──────────────────────────────────────────┤
│            Intelligence Layer            │  ← proactively composes and pushes solutions
├──────────────────────────────────────────┤
│               World Model                │  ← continuous machine-readable view of company + customers
├──────────────────────────────────────────┤
│               Capabilities               │  ← atomic financial components, no UI
└──────────────────────────────────────────┘
```

The revolutionary shift in the Intelligence Layer: from "product managers plan features" → the Intelligence Layer identifies timing and composes solutions; failure signals automatically become the roadmap; **product planning shifts from guess-driven to signal-driven.**

Three new human roles: Individual Contributors (ICs, given context by the World Model, making autonomous decisions), DRIs (Directly Responsible Individuals, short-term ownership of cross-domain problems, replacing project managers/product managers), and Player-Coaches (both building and developing people, replacing traditional managers).

> The World Model handles alignment; DRIs handle strategy and priorities; Player-Coaches handle craft and people development.

**A critique that must be heard** (a critical analysis of the Block framework): Dorsey's premise is that "the main value of humans is information routing," but if humans are also generating, interpreting, and creating signals, then subtracting humans means subtracting intelligence itself; the real bottleneck is not routing speed but **perspective loss** (signals die before they reach decision points). Core warning: **"Speed is not intelligence. Speed without integration is just faster blindness."**

## 4.5 Yang Renbin: The Organizational Brain and the AI Chief of Staff

In a 2026 interview with LatePost (Chinese: 晚点), Yang Renbin (Chinese: 杨仁斌), founder of Jingzhunxue (Chinese: 精准学) — an AI education brand founded by Yang Renbin — supplied the piece all previous perspectives were missing: **how the highest cognition and decision-making capability can be systematically injected into every frontline execution step.**

- **First principles of the organization**: solving three traditional deadlocks — the top-down decay of "highest cognition → frontline," the bottom-up distortion of "frontline facts → top," and the bandwidth bottleneck at the top;
- **Three steps**: ① model the decision layer's judgment methods into a callable "AI Chief of Staff / Organizational Brain" (initially injecting 300,000 characters of methodology) → ② inject it into every business site through context engineering (a decision-model index system) → ③ frontline real problems/disagreements/anomalies flow back, closing the loop to iterate the highest cognition;
- **AI coding is only 0% and 100%**: a hard rule that engineers are not allowed to modify code themselves — humans only give feedback and transform into "context engineers," going further than MarsWave's "AI writes 99% of the code";
- **Anti-document, anti-group-chat business discussion**: documents are negative assets (author bias plus information loss); preserve the original records of discussions, disagreements, and failures; deep discussions continue in AI conversations; offline voice must be transcribed to text and enter the context;
- **Context is Everything**: once model capability is replicable, what is truly scarce is context engineering;
- **Cultural premise**: "explain the Why thoroughly, and give enough AI (爱, 'love,' pronounced ài, is a pun on AI)"; an open culture — hiding problems is shameful, exposing them means solving them sooner; don't hold people accountable for making mistakes, hold them accountable for hiding problems or failing to update their judgment.

## 4.6 An International Comparison: The Changing Role of the Engineer

Anthropic's internal practice confirms the direction of role reconstruction: the engineer's role shifts from "writing code" to "**architect + referee**" — AI-powered automated code review is embedded in CI/CD, and post-hoc analysis shows it intercepted about one-third of the production bugs in claude.ai's history that caused downtime<sup>[7-28]</sup>; one engineer used AI to auto-fix 800+ API errors that humans estimated would take four years. At OpenAI, Codex became the primary work tool of every department (including non-technical ones such as legal, finance, and recruiting), accounting for 99.8% of the company's weekly output tokens<sup>[7-38]</sup>.

## 4.7 Three Paths: There Is No Single AI-Native Organization

Putting this chapter's cases together with the international ones, there are three parallel paths to the AI-native organization:

1. **The shrink path** (Klarna): hiring freeze + natural attrition, headcount −38%<sup>[7-01]</sup>, with AI replacing the headcount growth that demand would have required;
2. **The expansion path** (OpenAI/Anthropic): headcount and revenue grow together; AI-native is a growth engine, not a downsizing tool;
3. **The steady-state leverage path** (Shopify/Duolingo/Airbnb): full-time headcount flat or slightly up, with AI raising per-capita output.

**There is no single answer for organizational structure, but organizational principles converge**: AI handles information routing and execution; humans handle judgment, quality, and review; hierarchy grows thinner as coordination functions are replaced by AI platforms; experience shifts from a personal asset into an organizational asset. In the next chapter, we look at how workflows and decisions are concretely redesigned.
