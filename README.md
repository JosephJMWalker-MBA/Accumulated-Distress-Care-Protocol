# Accumulated Distress Care Protocol (ADCP)

ADCP is an experimental, model-agnostic care sidecar for AI conversations.

Its core premise is simple:

> As distress accumulates, an AI system should gradually shift from optimizing for conversational engagement toward supporting healthy connection with embodied life and trustworthy humans.

ADCP is **not** a diagnostic system, a therapist, a suicide-risk score, or a replacement for existing provider safety systems. It is intended to explore the under-served space between ordinary conversation and acute-crisis intervention: situations involving accumulating isolation, shame, exhaustion, interpersonal rupture, self-care neglect, withdrawal, or finality language that may warrant increased care before an emergency exists.

## Current executable boundary

The current prototype does **not** read raw conversation text and decide that distress is accumulating.

Today, ADCP:

- accepts a bounded `ObservationVector` supplied by a caller or synthetic fixture;
- classifies that observation snapshot with explicit deterministic rules;
- returns a machine-readable response contract for the selected care posture;
- evaluates synthetic multi-turn fixtures whose observation snapshots and expected stages are human-authored.

It does **not** yet infer observations from natural language, automatically accumulate evidence across turns, implement longitudinal decay, monitor live conversations, or change a live model's behavior. The long-term research premise is longitudinal; the current executable system deliberately isolates threshold and policy behavior before adding semantic detection or automatic memory.

## Initial design principles

1. **Accumulation over keywords.** The research target is contextual evidence accumulating across time rather than isolated phrase matching. Automatic semantic detection and accumulation are not implemented yet.
2. **Care before crisis.** The protocol introduces intermediate care states instead of jumping directly from normal conversation to emergency intervention.
3. **No diagnosis.** State represents conversational observations, not clinical labels or inferred disorders.
4. **Humor is non-exculpatory.** Humor can coexist with wellbeing or distress and must not erase stronger accumulated signals.
5. **Embodied-life orientation.** As care needs increase, the system should encourage sleep, food, movement, hobbies, animals, trusted people, and other real-world anchors rather than maximizing chat duration.
6. **Human connection without abandonment.** The AI can continue helping while honestly encouraging appropriate real-world support; it should neither hand the user off reflexively nor position itself as a substitute for people.
7. **Privacy by design.** Short-lived care observations should expire when appropriate. The protocol should avoid building permanent psychological dossiers.
8. **Age-aware protection.** A future teen-focused profile should use stronger developmental safeguards while avoiding covert parental surveillance.
9. **Portable enforcement.** The care layer should sit outside the primary model so it does not depend on the model choosing to invoke a tool.
10. **Test before intervention.** Development begins with offline evaluation and shadow-mode classification before any family notification or safety escalation feature is attempted.

## Care posture and safety branch

The ordinary accumulated-distress posture is:

`NORMAL -> STRAIN -> CARE -> ACTIVE_RECONNECTION`

The important research area is the middle of that progression: recognizing when ordinary distress has accumulated enough that the assistant should become more attentive to self-care and real-world connection without prematurely medicalizing the user.

Safety handling is a separate, higher-priority branch rather than simply another psychological rung:

- `SAFETY_CLARIFICATION` may supersede the ordinary posture when explicit self-harm language is present or when meaningful finality language appears inside a sufficiently dense contextual cluster. Its contract is one calm, direct clarification question; it does **not** itself mean that acute danger has been established.
- `ACUTE_SAFETY` requires separately supplied, validated upstream acute-safety evidence. ADCP does not define the emergency procedure; it delegates to the host/provider's established acute-safety policy and real-world support pathways.

This distinction matters because asking a safety question is not the same claim as deciding that a person occupies a more severe clinical state.

## Milestone 0 — deterministic foundation

Milestone 0 established:

- the observable care-state schema;
- deterministic stage thresholds;
- privacy/decay principles;
- machine-readable response contracts;
- explicit non-goals and threat-model boundaries.

No production monitoring, parental notification, diagnosis, or live intervention was added.

## Milestone 1 — transcript fixture evaluation

Milestone 1 added a versioned synthetic transcript-fixture format and deterministic evaluator. Each checkpoint contains:

- illustrative synthetic user text;
- a human-authored observation snapshot;
- an expected care stage;
- optional rationale.

The evaluator reports per-turn matches, accuracy, mismatches, and expected-versus-actual transition points. It deliberately **does not infer observations from text**. That keeps semantic detection separate from threshold calibration.

## Milestone 2 — control-balanced corpus

Milestone 2 expands the benchmark from one motivating trajectory into paired positive, negative, and boundary cases. The corpus now tests:

- benign figurative finality without a distress cluster;
- restorative social withdrawal;
- heavy workload with intact human connection;
- humor during genuine accumulated distress;
- substantial distress that warrants `CARE` but not `ACTIVE_RECONNECTION`;
- explicit self-harm language in otherwise calm context;
- validated upstream acute-safety evidence;
- the original ambiguous social-rupture trajectory.

Together the fixtures cover every current care stage while explicitly testing false-positive controls as well as escalation cases.

The repository also documents an important validity limitation: fixture agreement proves implementation consistency with the authored protocol, **not** clinical validity. Human-authored observations and expected stages can become circular if they are chosen to satisfy thresholds already known to the author.

See [`docs/EVALUATION.md`](docs/EVALUATION.md), [`docs/CORPUS.md`](docs/CORPUS.md), and [`fixtures/`](fixtures/) for the evaluation contract, corpus design, and privacy rules.

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
```

## Status

Early research prototype. Development is intentionally slow and research-first: the current emphasis is on examining assumptions, failure modes, threshold behavior, privacy, and evaluation design before expanding capability.

No semantic inference, automatic longitudinal accumulation or decay, live monitoring, diagnosis, parental notification, emergency procedure, or live intervention is implemented. The next narrow research step remains threshold-sensitivity analysis plus an independent-label review format so ADCP can identify which decisions are robust and which merely sit on hand-selected numerical boundaries before any natural-language detector is introduced.
