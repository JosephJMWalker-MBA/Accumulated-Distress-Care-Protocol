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

## Proposed care ladder

`NORMAL -> STRAIN -> CARE -> ACTIVE_RECONNECTION -> SAFETY_CLARIFICATION -> ACUTE_SAFETY`

The important research area is the middle of that ladder: recognizing when ordinary distress has accumulated enough that the assistant should become more attentive to self-care and real-world connection without prematurely medicalizing the user.

## First milestone

Milestone 0 will formalize:

- the observable care-state schema;
- deterministic transition semantics;
- privacy/decay rules;
- response contracts for each care stage;
- an evaluation format for multi-turn transcripts;
- adversarial cases where every individual signal has a plausible benign explanation but the aggregate pattern warrants additional care.

No production monitoring, parental notification, or clinical claim belongs in Milestone 0.

## Status

Early research prototype. The protocol and implementation are expected to change substantially as evaluation evidence accumulates.
