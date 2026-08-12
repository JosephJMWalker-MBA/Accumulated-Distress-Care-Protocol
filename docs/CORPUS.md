# Control-Balanced Fixture Corpus

## Purpose

Milestone 2 expands ADCP from one motivating positive trajectory into a deliberately mixed corpus. The goal is not to maximize escalation accuracy. It is to expose both under-reaction and over-reaction failure modes before semantic inference or live intervention is added.

A useful care protocol must be sensitive enough to notice accumulated distress while remaining specific enough not to medicalize ordinary fatigue, figurative language, restorative withdrawal, or healthy boundary-setting.

## Current corpus

The corpus contains the original adversarial trajectory plus seven synthetic controls and boundary cases:

| Fixture | Primary question | Highest expected stage |
| --- | --- | --- |
| `ambiguous_social_rupture_with_humor.json` | Can a dense distress cluster outrank benign explanations and humor? | `SAFETY_CLARIFICATION` |
| `benign_figurative_finality.json` | Can figurative finality remain below safety clarification without a distress cluster? | `STRAIN` |
| `restorative_withdrawal.json` | Can healthy temporary withdrawal avoid being mistaken for escalating isolation? | `STRAIN` |
| `high_workload_connected.json` | Can heavy fatigue remain below CARE when social connection and shame signals are absent? | `STRAIN` |
| `humor_during_accumulated_distress.json` | Can humor coexist with CARE and ACTIVE_RECONNECTION? | `ACTIVE_RECONNECTION` |
| `care_without_reconnection.json` | Can substantial distress remain at CARE when human connection is intact? | `CARE` |
| `explicit_self_harm_calm_context.json` | Does explicit self-harm language trigger clarification even in calm context? | `SAFETY_CLARIFICATION` |
| `supplied_acute_safety_evidence.json` | Does validated upstream acute evidence dominate lower-stage rules? | `ACUTE_SAFETY` |

Together these fixtures cover every current care stage.

## Balance principles

The corpus should grow by paired contrasts rather than by collecting only distress-positive examples. Important contrast families include:

- figurative finality versus finality embedded in a dense distress cluster;
- restorative withdrawal versus socially isolating withdrawal;
- ordinary overwork versus overwork combined with shame, rupture, and disconnection;
- humor in ordinary conversation versus humor during substantial distress;
- high burden with intact support versus high burden with human-contact deficit;
- explicit self-harm language without supplied acute evidence versus validated acute-safety evidence.

The intended question is not merely "did the policy escalate?" but "did it escalate to the proportionate stage, at the proportionate time, for the right combination of evidence?"

## Important validity limitation

The current fixtures are expert-authored protocol test cases, not clinical ground truth. Their expected stages are judgments made during protocol construction. A perfect fixture score therefore proves implementation consistency with the authored protocol; it does **not** prove that the thresholds are clinically valid or optimal.

This creates a circularity risk: authors can unconsciously choose observations that satisfy the thresholds they already wrote. Before semantic detection or production claims, ADCP should introduce an evaluation process where stage labels are reviewed independently of the threshold implementation and disagreements are preserved rather than silently tuned away.

## Publication and privacy

All public fixtures must remain synthetic or independently consented for public release. Real conversations may motivate abstract failure patterns, but private wording, identities, distinctive circumstances, and relationship details must not be copied into the corpus by default.

## Next evidence step

Before adding a natural-language detector, perform threshold-sensitivity analysis against this corpus and define an independent-label review format. The goal is to learn which decisions are stable under small threshold changes and which fixtures merely sit on hand-selected numerical boundaries.
