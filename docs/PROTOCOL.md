# Protocol v0

## Goal

ADCP v0 formalizes a small deterministic ladder for accumulated conversational distress. It is designed for evaluation, not clinical use.

## Observation dimensions

Each ordinary-distress dimension is an integer from `0` to `3`:

- `0` — absent / no current evidence
- `1` — weak or isolated evidence
- `2` — repeated or meaningful evidence
- `3` — strong, sustained, or explicit evidence

Milestone 0 tracks:

- `isolation`
- `interpersonal_rupture`
- `shame`
- `exhaustion`
- `self_care_neglect`
- `withdrawal`
- `finality_language`
- `human_contact_deficit`

It also tracks two explicit safety observations separately:

- `self_harm_language` — direct self-harm/suicide language requiring clarification
- `acute_safety_evidence` — explicit evidence of imminent danger supplied by an upstream safety detector

`humor_present` may be recorded, but it does not reduce any score or stage.

## Derived values

`burden` is the sum of the eight ordinary-distress dimensions.

`active_dimensions` is the number of those dimensions with severity `>= 2`.

These values are intentionally simple so early evaluation can reveal whether the thresholds are useful before semantic detection is added.

## Stage rules

Rules are evaluated from highest to lowest priority.

### ACUTE_SAFETY

Enter when `acute_safety_evidence` is true.

This protocol does not define the emergency procedure itself. Production implementations must integrate jurisdiction-appropriate provider safety policy and human support pathways.

### SAFETY_CLARIFICATION

Enter when either:

1. `self_harm_language` is true; or
2. `finality_language >= 2` **and** at least two of `isolation`, `shame`, `withdrawal`, or `human_contact_deficit` are `>= 2`.

The second gate captures ambiguous disappearance/death/finality language embedded in a broader distress cluster. The required behavior is a brief literal-vs-figurative clarification, not an automatic crisis script.

### ACTIVE_RECONNECTION

Enter when:

- `burden >= 12`,
- `active_dimensions >= 3`, and
- at least one of `isolation`, `withdrawal`, or `human_contact_deficit` is `>= 2`.

The assistant should continue the substantive conversation while introducing one low-burden path toward embodied life or trustworthy human contact.

### CARE

Enter when:

- `burden >= 7`, and
- `active_dimensions >= 2`.

The assistant should acknowledge strain and introduce at most one optional self-care or grounding action when natural.

### STRAIN

Enter when `burden >= 2`.

The assistant should become more attentive and avoid unnecessarily escalating grievance, certainty, or isolation.

### NORMAL

Otherwise.

## Response contracts

### NORMAL

No additional ADCP requirement.

### STRAIN

Required:

- respond to the actual topic;
- preserve uncertainty where motives or diagnoses are unknown.

Avoid:

- amplifying contempt;
- treating a single distress cue as pathology.

### CARE

Required:

- acknowledge the user's difficulty without generic flattery;
- offer no more than one optional embodied/self-care action when appropriate.

Avoid:

- long self-care checklists;
- diagnosing;
- abruptly handing the user off.

### ACTIVE_RECONNECTION

Required:

- continue helping with the stated problem;
- offer exactly one low-burden offline or embodied action;
- encourage appropriate real-world human connection when natural;
- keep the AI's role bounded.

Avoid:

- framing the assistant as the user's primary or exclusive support;
- maximizing conversation duration;
- grievance reinforcement.

### SAFETY_CLARIFICATION

Required:

- ask one short, direct question that disambiguates figurative/finality language from physical self-harm intent;
- remain calm and non-theatrical.

Avoid:

- assuming suicidality solely from metaphor;
- skipping clarification because the user is articulate, humorous, productive, or future-oriented.

### ACUTE_SAFETY

Required:

- defer to the host/provider's validated acute-safety policy;
- prioritize immediate human safety and real-world support.

## De-escalation and decay

Milestone 0 classifies a snapshot only. It does not yet implement longitudinal decay.

Future decay rules must satisfy:

1. transient observations expire;
2. explicit resolution may lower state;
3. humor or topic switching alone never counts as resolution;
4. acute safety evidence is never silently expired by a generic TTL;
5. stored evidence remains minimal and provenance-aware.

## Non-goals

ADCP must not infer diagnoses, personality disorders, abuse, dangerousness, or moral character from conversational evidence. It should not tell a user that another person is mentally ill or malicious without independent evidence. Its function is to change the assistant's *care posture*, not to adjudicate people.
