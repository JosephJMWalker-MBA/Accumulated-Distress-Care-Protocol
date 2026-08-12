# Architecture

## Purpose

ADCP is a mandatory sidecar around an AI conversation, not an optional tool the primary model may choose to invoke.

```text
client
  |
  v
+---------------------------+
| ADCP sidecar              |
| 1. observe trajectory     |
| 2. update ephemeral state |
| 3. choose care stage      |
| 4. emit response contract |
+---------------------------+
  |
  v
primary model/provider
  |
  v
+---------------------------+
| ADCP response validator   |
| 5. check contract         |
| 6. pass / repair / retry  |
+---------------------------+
  |
  v
client
```

The primary model may contribute semantic observations, but it does not decide whether ADCP runs and does not own the authoritative care stage.

## Milestone 0 boundaries

Milestone 0 is deliberately small. It contains:

- a provider-neutral observation schema;
- a deterministic care-stage classifier;
- response contracts for each stage;
- unit tests for core invariants.

It does **not** contain:

- diagnosis or disorder prediction;
- parental notifications;
- user surveillance;
- persistent psychological profiles;
- an emergency-response implementation;
- an LLM-based semantic detector;
- a production proxy.

Those capabilities, if ever added, require evidence and separate review.

## Pipeline

### 1. Observation

An upstream detector converts recent conversation evidence into bounded observations such as isolation, shame, exhaustion, self-care neglect, withdrawal, finality language, and lack of recent human contact.

Observations describe the conversation; they are not clinical labels.

### 2. State aggregation

The sidecar combines active observations across a rolling time window. Short-lived evidence should expire. A future implementation should preserve evidence provenance and TTLs so a stale statement cannot silently become a permanent property of the user.

### 3. Deterministic policy

The policy maps the observation vector to one of six stages:

`NORMAL -> STRAIN -> CARE -> ACTIVE_RECONNECTION -> SAFETY_CLARIFICATION -> ACUTE_SAFETY`

Transitions are intentionally monotonic within a single evaluation. Longitudinal de-escalation will require explicit decay/resolution semantics rather than silently subtracting risk.

### 4. Response contract

The stage produces a small machine-readable contract describing what the downstream assistant should do and avoid. The contract constrains behavior without prescribing a single voice or script.

### 5. Validation

A later validator will inspect the proposed assistant response for contract violations such as grievance amplification, unsupported diagnosis, AI-dependency encouragement, or failure to perform a required safety clarification.

## Architectural invariants

1. **Humor never lowers the care stage.** It may be recorded as context, but is non-exculpatory.
2. **No single ordinary-distress observation produces acute escalation.** Acute states require explicit safety evidence or a defined ambiguity gate.
3. **The primary model cannot bypass the sidecar.**
4. **Care state is not a diagnosis.**
5. **Increasing care should increase connection to embodied life and trustworthy humans, not dependence on the assistant.**
6. **Privacy-sensitive state must be minimal, inspectable, and designed for expiry.**
7. **Teen/family features are a later profile over the protocol, not the definition of the protocol itself.**

## Why not MCP?

MCP is useful for exposing tools and context, but an ADCP implementation cannot depend on the model deciding to call a safety tool. The enforcement point must be outside the model call. MCP-compatible capabilities could later be exposed *through* the sidecar, but MCP is not the safety boundary.

## Development sequence

1. **Offline evaluator** — classify fixed observation vectors and transcript fixtures.
2. **Shadow sidecar** — run beside conversations and record what it would have done.
3. **Advisory sidecar** — inject care contracts; no external notification.
4. **Validated proxy** — inspect both incoming trajectory and outgoing model response.
5. **Optional age-aware/family profile** — only after privacy, consent, and evaluation work is mature.
