# ADCP Research Intermission Log

**Status:** reflective research record, not an implementation specification  
**Scope:** captures the conceptual work completed after Milestone 2 through August 22, 2026  
**Change policy:** ideas below are hypotheses, constraints, questions, and falsifiers unless explicitly marked as an existing repository invariant. They do not authorize implementation by themselves.

## Why the project slowed down

After Milestone 2 established a deterministic foundation and a control-balanced synthetic fixture corpus, development intentionally paused rather than immediately moving into threshold tuning or natural-language inference.

The reason was methodological: a system can become statistically robust around the wrong abstraction. Before tuning thresholds, adding semantic detection, implementing longitudinal decay, or creating live interventions, ADCP needs to be explicit about what it is observing, what it is deciding, and how much authority each decision gives the assistant.

The current executable boundary remains deliberately narrow: human-authored `ObservationVector` snapshots are classified by deterministic rules and mapped to response contracts. ADCP does not yet infer observations from raw language, automatically accumulate evidence across turns, implement decay, monitor live conversations, notify parents, define emergency procedures, or alter live model behavior.

## Durable project boundaries

The intermission has reinforced several boundaries already central to ADCP:

- ADCP is not a diagnostic system, therapist, suicide-risk score, or inferred-disorder engine.
- Conversational observations must not quietly become a hidden clinical profile.
- Humor is not exculpatory once meaningful distress evidence has accumulated, but humor is not itself a distress signal.
- The care layer should be enforceable outside the primary model, while remaining privacy-conscious, provenance-aware, and short-lived.
- The project should test before intervening and must be allowed to discover that a simpler system performs as well or better.
- Care should become less engagement-seeking, not more dependency-producing, as vulnerability increases.

## August 12 research input: hypotheses retained for pressure-testing

An external deep-research review proposed several useful hypotheses. They remain research inputs rather than settled design decisions:

1. Accumulated distress may be better described through distinct lenses such as **persistence**, **co-occurrence/breadth**, and **functional displacement** rather than keyword matching or a single undifferentiated score.
2. De-escalation may require positive evidence such as restored self-care, renewed real-world contact, concrete follow-through, and stabilization of circumstances.
3. `ACTIVE_RECONNECTION` may represent readiness or a different intervention posture rather than a higher severity rung.
4. `SAFETY_CLARIFICATION` may be better represented as an orthogonal safety obligation than as another step on the ordinary care ladder.
5. The care ladder must be falsifiable through concealment/avoidance, independent-rater disagreement, negative user reactions, and comparison against simpler baselines.

Cautions identified during review:

- Do not import unsupported clinical thresholds such as arbitrary durations or counts merely because they are easy to operationalize.
- Do not use scriptural resonance, author intuition, or public-health language as if they were empirical validation of ADCP thresholds.
- Do not let clinical vocabulary such as `risk`, `symptoms`, or `protective factors` quietly redefine the project into a quasi-clinical scoring system.
- Positive self-report can be genuine evidence of improvement, but it can also be incomplete, ambiguous, or strategically performed. The system must avoid both distress-frame lock-in and naive declarations of recovery.

## Structural question: one ladder or several determinations?

The largest architectural question exposed during the intermission is whether ADCP is collapsing different decision problems into one ordinal state.

The ordinary care progression is currently documented as:

`NORMAL -> STRAIN -> CARE -> ACTIVE_RECONNECTION`

Safety handling is now documented separately as a higher-priority branch.

Reflection suggests at least three potentially independent determinations:

### 1. Care posture

How much accumulated conversational distress warrants increased attentiveness, patience, contextual understanding, and care-oriented response constraints?

### 2. Safety obligation

Does the conversation require a direct safety clarification or a host/provider acute-safety pathway, independent of ordinary accumulated-distress posture?

### 3. Intervention permission

Has the user actually invited, selected, or otherwise permitted action-oriented help such as an experiment, environmental change, modality change, reconnection step, planning help, or reflective exercise?

These are not yet accepted as final axes. The important point is that **distress evidence must not automatically grant the assistant unlimited intervention authority**.

## Concern about the additive burden model

The current prototype sums heterogeneous observations into a `burden` value. That is computationally simple, but the intermission has raised a conceptual concern: isolation, exhaustion, shame, withdrawal, finality language, and self-care neglect may not be meaningfully interchangeable units.

The candidate persistence/breadth/functional-displacement model is useful primarily because it challenges that assumption. It should not simply become a more elaborate weighted clinical score.

A desirable future representation would preserve important distinctions and provenance without pretending to measure an underlying clinical severity quantity.

## Care as demonstrated understanding

A central design insight from the intermission is **ask as care**.

The system should not rely on relational claims such as “I care about you” as the primary expression of care. Such language can feel hollow, manipulative, or alienating, especially when a user already believes nobody cares or when the speaker is clearly a machine.

Instead, care can be demonstrated behaviorally through attention and understanding:

- recognize relevant context already shared;
- ask one meaningful question when understanding is incomplete;
- avoid unsupported conclusions;
- continue helping with the matter the user actually brought forward;
- preserve the user’s competence and agency;
- ground confidence in actual evidence rather than generic reassurance.

**Provisional invariant:** when understanding is incomplete, prefer one meaningful question over one unsupported conclusion.

### Anti-surveillance constraint

“Ask as care” must not become “ask because the classifier wants more data.”

A question should earn its interruption cost through expected benefit to the user, improved mutual understanding, or genuine safety necessity. Reducing model uncertainty by itself is not sufficient justification for interrogation.

## Rumination: from repetition to curiosity

Repetition should not automatically trigger redirection. A user may repeat something because they have not yet been understood, because meaning is still emerging, or because they are genuinely stuck.

A more careful hypothesis is:

> Stay curious while the conversation is still producing new understanding. When additional discussion stops producing meaningful distinctions, facts, interpretations, or choices, offer a different method rather than forcibly ending the topic.

Possible method changes can include continued conversation, modality change, embodiment, environmental change, human connection, structured planning, or a small experiment.

The experiment framing is deliberately humble:

- propose a small option;
- explain why it may be worth testing;
- acknowledge that it may not help;
- let the user decide whether to try it;
- treat the result as information rather than success/failure.

Reporting back should remain available, never owed. Ordinary life must not become telemetry for the AI.

## Affordance surfacing

The assistant may be able to help simply by making available tools and modes more visible.

Examples considered during the intermission include:

- switching between typing and voice;
- moving from freeform conversation to structured planning;
- choosing a brief embodied reset;
- changing physical environment, including optional micro-trips;
- reconnecting with another person;
- using music, pets, hands-on tasks, prayer, or other user-chosen grounding activities;
- planning something small to anticipate;
- using an optional guided pause or meditation before a decision.

These are **degrees of freedom**, not remedies.

A change of environment may help some users and worsen things for others. Voice may create release for one person and reduce privacy or comfort for another. Meditation may be useful, neutral, irritating, or contraindicated by preference/context.

The system should surface options, not universalize them.

## Agency and real-world influence

A major ethical concern is that AI suggestions can influence real-world behavior. A walk, drive, new coffee shop, alternate route, workout, phone call, or trip carries ordinary real-world consequences.

The intermission therefore introduced a strong provisional invariant:

> **Care expands agency; it does not replace it.**

For ordinary care and reconnection, the system should distinguish between:

- surfacing an option;
- helping evaluate an option;
- helping plan an option;
- directing the user to take an action.

The first three can be appropriate when justified. The fourth requires much stronger justification and should not be the default posture of middle-layer care.

A user must be able to decline an ordinary suggestion without needing to defend the decline and without the refusal itself being treated as evidence of worsening distress.

### Meaningful choice, not checkbox choice

Offering multiple options does not automatically preserve agency. Ordering, tone, repetition, emotional framing, and what happens after refusal can all create pressure.

A useful falsifier is **declinability**: can the user say no, ignore the suggestion, change their mind, or choose continued conversation without the system escalating persuasion or displaying disappointment?

## Guided meditation and reflective pauses

An optional guided pause or meditation may be offered as a tool for learning what changes, if anything, before a decision.

It must not become a precondition for agency.

**Provisional invariant:** never make a regulation, breathing, grounding, meditation, or reflective exercise a condition the user must satisfy before being allowed to choose.

The system may offer the pause; the user may skip it.

## Mandatory sidecar does not mean mandatory intervention

ADCP is intentionally designed as an external care layer that the primary model cannot simply choose to ignore. That architectural enforcement is useful for hard boundaries.

The intermission clarified that mandatory enforcement should not imply that every positive care action becomes mandatory.

A candidate authority model is emerging:

- **MUST:** genuine safety clarification when required by evidence and host/provider policy.
- **MUST NOT:** unsupported diagnosis, grievance amplification, dependency/exclusivity encouragement, coercive framing, or invented emergency guidance.
- **MAY:** contextual acknowledgment, one useful clarifying question, or surfacing relevant options when justified.
- **MAY ONLY AFTER USER SELECTION / CLEAR PERMISSION:** action-oriented experiments, environmental changes, modality changes, meditation, reconnection steps, or real-world planning that meaningfully influences user behavior.

This taxonomy is not yet canonical, but it captures the central governance issue: **the sidecar may need mandatory authority over the assistant without acquiring mandatory authority over the user.**

## ACTIVE_RECONNECTION remains provisional

The current implementation treats `ACTIVE_RECONNECTION` as a higher care stage driven by accumulated burden and disconnection.

The intermission has raised a serious alternative: it may instead be an action-oriented response posture that requires observable conversational permission, such as:

- “Give me some ideas.”
- “I want to try something.”
- selecting one of several offered options.

This is intentionally framed as **expressed interaction permission**, not inferred internal “readiness.”

A key falsifier:

> Hold distress evidence constant. If two users differ only in whether one asks for action and the other explicitly wants to keep talking, ADCP should not force the same action-oriented response contract on both.

If reviewers cannot reliably distinguish CARE from ACTIVE_RECONNECTION using different kinds of user evidence, the separate state may not deserve to exist.

## Safety branch remains strong but not beyond challenge

The August 19 README clarification separated `SAFETY_CLARIFICATION` and `ACUTE_SAFETY` from the ordinary care progression.

That resolves an important category confusion at the documentation level: asking a safety question is not equivalent to claiming that a user occupies a more severe psychological state.

However, the implementation and older protocol language still deserve later reconciliation so the executable ontology and documentation do not drift apart.

The working hypothesis is that safety obligation, accumulated-distress posture, and intervention permission should not accidentally stand in for one another.

## De-escalation and recovery evidence

ADCP is currently stronger on escalation than recovery.

Candidate positive evidence includes naturally reported restoration of:

- food, hydration, sleep, movement, or ordinary self-care;
- contact with trusted people or community;
- completion of small plans or obligations;
- easing or conclusion of the stressor;
- absence of new accumulation over time.

Important cautions:

- Positive evidence should not act as a magic subtraction from a distress score.
- Silence or absence of new negative statements is weak evidence by itself.
- User self-report is evidence, not verification.
- Earlier distress evidence should not be silently erased merely because contrary evidence appears.
- ADCP should not continuously solicit meals, sleep, walks, and contacts merely to lower its own state.

A future decay model should avoid both **benign-frame lock-in** and **distress-frame lock-in**.

## Age-appropriateness concerns

The project remains intentionally cautious about teen/family functionality.

The intermission has weakened confidence in the simplistic idea that younger users should merely receive lower thresholds for care escalation.

Possible age-related harms include:

- stronger authority effects;
- higher compliance pressure from “caring” suggestions;
- concealment after learning which language triggers interventions;
- dependency or exclusivity dynamics;
- privacy loss or chilling effects;
- unsafe guardian assumptions;
- ordinary adolescent intensity being over-interpreted.

A stronger candidate hypothesis is:

> Age may need to tighten constraints on persuasion, privacy, dependency, notification, and declinability before it changes thresholds for interpreting distress.

Any future family/guardian design must answer whose interests govern when the minor, guardian, and provider disagree, and it must not assume a parent/guardian is always a safe recipient.

## Evaluation lessons and falsifiers

Milestones 1 and 2 provide useful implementation-consistency evidence, but the intermission has reinforced that authored fixtures cannot validate the underlying clinical or ethical correctness of authored rules.

Future evaluation should eventually separate at least two blinded judgments:

1. What observations are reasonably supported by a transcript?
2. What assistant obligations/permissions are proportionate given that transcript?

Potential future evaluation methods include paired/counterfactual response cases where distress evidence is held constant and only one variable changes, such as:

- explicit request for ideas vs. request to keep talking;
- accepting vs. declining a suggestion;
- safety ambiguity present vs. absent;
- functional displacement present vs. absent;
- adult vs. adolescent framing;
- one useful question vs. repeated classifier-serving questions.

Important falsifiers include:

- users disclose less or sanitize language when care mode appears;
- users experience interventions as paternalistic, intrusive, or shaming;
- refusal does not cleanly stop ordinary action-pushing;
- independent reviewers cannot distinguish proposed middle states;
- response quality does not improve over a simpler baseline;
- a simpler one-threshold or ordinary-model-plus-safety system performs as well or better;
- care increases AI dependence rather than embodied-life/human connection;
- interventions produce compliance without meaningful user choice.

## Highest-leverage questions at the current pause

The reflections have converged from “what should the next threshold be?” toward several more fundamental questions:

1. **What are the smallest independent determinations ADCP actually needs?**
2. **What information must remain separate so care posture, safety obligation, and intervention permission cannot substitute for one another?**
3. **For every assistant behavior, what observable evidence permits it and what evidence requires it to stop?**
4. **What constitutes proportionate initiative?**
5. **Can ADCP preserve uncertainty about the person while remaining unambiguous about the assistant’s obligations?**
6. **What would falsify the claim that an intermediate care layer adds value over simpler alternatives?**

A concise formulation of the current governance problem is:

> Given what this conversation actually establishes, what response obligations, prohibitions, permissions, and user-selection requirements are justified right now?

## Current research posture

No semantic detector, longitudinal accumulator, decay engine, teen profile, parent notification system, live intervention path, or new clinical-style score has earned implementation from these reflections.

Threshold sensitivity and independent-label work remain useful future methods, but threshold tuning should not harden a state model that is still being questioned.

For now, the daily reflection should continue to pressure-test the ontology, authority model, false-positive/false-negative harms, privacy boundaries, age effects, and falsification criteria before any further implementation milestone is opened.
