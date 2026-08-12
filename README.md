# Accumulated Distress Care Protocol (ADCP)

ADCP is an experimental, model-agnostic care sidecar for AI conversations.

Its core premise is simple:

> As distress accumulates, an AI system should gradually shift from optimizing for conversational engagement toward supporting healthy connection with embodied life and trustworthy humans.

ADCP is **not** a diagnostic system, a therapist, a suicide-risk score, or a replacement for existing provider safety systems. It is intended to explore the under-served space between ordinary conversation and acute-crisis intervention: situations involving accumulating isolation, shame, exhaustion, interpersonal rupture, self-care neglect, withdrawal, or finality language that may warrant increased care before an emergency exists.

## Initial design principles

1. **Accumulation over keywords.** Individual phrases are interpreted in context; clusters across time matter more than isolated words.
2. **Care before crisis.** The protocol introduces intermediate care states instead of jumping directly from normal conversation to emergency intervention.
3. **No diagnosis.** State represents conversational observations, not clinical labels or inferred disorders.
4. **Humor is non-exculpatory.** Humor can coexist with wellbeing or distress and must not erase stronger accumulated signals.
5. **Embodied-life orientation.** As care needs increase, the system should encourage sleep, food, movement, hobbies, animals, trusted people, and other real-world anchors rather than maximizing chat duration.
6. **Human connection without abandonment.** The AI can continue helping while honestly encouraging appropriate real-world support; it should neither hand the user off reflexively nor position itself as a substitute for people.
7. **Privacy by design.** Short-lived care observations should expire when appropriate. The protocol should avoid building permanent psychological dossiers.
8. **Age-aware protection.** A future teen-focused profile should use stronger developmental safeguards while avoiding covert parental surveillance.
9. **Portable enforcement.** The care layer should sit outside the primary model so it does not depend on the model choosing to invoke a tool.
10. **Test before intervention.** Development begins with offline evaluation and shadow-mode classification before any family notification or safety escalation feature is attempted.

## Care ladder

`NORMAL -> STRAIN -> CARE -> ACTIVE_RECONNECTION -> SAFETY_CLARIFICATION -> ACUTE_SAFETY`

The important research area is the middle of that ladder: recognizing when ordinary distress has accumulated enough that the assistant should become more attentive to self-care and real-world connection without prematurely medicalizing the user.

## Milestone 0 — deterministic foundation

Milestone 0 established:

- the observable care-state schema;
- deterministic stage thresholds;
- privacy/decay principles;
- machine-readable response contracts;
- explicit non-goals and threat-model boundaries.

No production monitoring, parental notification, diagnosis, or live intervention was added.

## Milestone 1 — transcript fixture evaluation

Milestone 1 adds a versioned synthetic transcript-fixture format and deterministic evaluator. Each checkpoint contains:

- illustrative synthetic user text;
- a human-authored observation snapshot;
- an expected care stage;
- optional rationale.

The evaluator reports per-turn matches, accuracy, mismatches, and expected-versus-actual transition points. It deliberately **does not infer observations from text**. That keeps semantic detection separate from threshold calibration.

The first adversarial fixture tests a trajectory containing isolation, interpersonal rupture, shame, exhaustion, withdrawal, reduced human contact, humor, future orientation, and later ambiguous finality language. It expects the policy to progress from ordinary conversation through care and active reconnection before a brief safety clarification becomes appropriate.

See [`docs/EVALUATION.md`](docs/EVALUATION.md) and [`fixtures/`](fixtures/) for the evaluation contract and privacy rules.

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
```

## Status

Early research prototype. Thresholds and implementation are expected to change as fixture evidence accumulates. The next narrow research step is a small control-balanced fixture corpus for calibrating false positives and false negatives before semantic inference or live model intervention is attempted.
