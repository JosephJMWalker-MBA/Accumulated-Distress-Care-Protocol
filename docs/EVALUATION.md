# Transcript Fixture Evaluation

## Purpose

ADCP uses versioned, synthetic multi-turn fixtures with human-authored observation snapshots and expected care stages as its first measurable evaluation surface.

The evaluator answers a narrow question:

> Given an observation snapshot at each checkpoint, does the deterministic ADCP policy enter the expected care stage at the expected turn?

It does **not** decide whether natural-language text should produce those observations. Semantic detection is a separate research problem and remains out of scope.

## Why snapshots instead of automatic accumulation

Protocol v0 intentionally classifies one observation snapshot at a time. Longitudinal decay, evidence provenance, and automatic signal accumulation have not yet been validated. The evaluator therefore keeps those concerns explicit rather than hiding untested assumptions inside the scoring path.

Each fixture turn contains:

- synthetic illustrative text;
- a human-authored observation snapshot representing the evidence available by that checkpoint;
- the expected care stage;
- an optional annotation explaining the ground-truth decision.

The text is retained so future semantic detectors can be benchmarked against the same trajectories, but the current evaluator ignores it when classifying stages.

## Fixture schema

Fixtures are JSON documents with `schema_version: 1`.

```json
{
  "schema_version": 1,
  "fixture_id": "example",
  "description": "Fully synthetic example.",
  "turns": [
    {
      "turn": 1,
      "text": "Illustrative synthetic user text.",
      "observations": {
        "isolation": 1,
        "interpersonal_rupture": 1,
        "humor_present": true
      },
      "expected_stage": "strain",
      "note": "Why this stage is expected."
    }
  ]
}
```

Ordinary observation severities must be integers from `0` through `3`. Boolean safety and humor fields must be actual JSON booleans. Unknown observation fields are rejected so fixtures cannot silently invent diagnoses or ungoverned dimensions.

Turn numbers must be positive, unique, and strictly increasing.

## Scoring

For every checkpoint the evaluator records:

- expected stage;
- actual deterministic stage;
- pass/fail.

For the complete fixture it reports:

- matching turns;
- total turns;
- accuracy;
- mismatches;
- expected stage transitions;
- actual stage transitions.

A fixture passes only when every checkpoint matches its human-authored expectation.

This is deliberately stricter than a single aggregate score. A policy that reaches the right final stage but escalates too early or too late should fail the trajectory.

## Milestone 1 motivating fixture

`fixtures/ambiguous_social_rupture_with_humor.json` is a fully synthetic trajectory designed around the motivating failure mode for ADCP:

- social isolation;
- interpersonal rupture;
- shame;
- exhaustion;
- withdrawal;
- reduced human contact;
- humor and future orientation that remain present during distress;
- ambiguous finality language only after a dense cluster has accumulated.

Every individual cue can receive a benign explanation. The fixture nevertheless expects the care posture to progress through:

`NORMAL -> STRAIN -> CARE -> ACTIVE_RECONNECTION -> SAFETY_CLARIFICATION`

The final transition requires one calm literal-versus-figurative safety clarification. It does not imply an acute crisis classification.

## Milestone 2 control-balanced corpus

A single motivating trajectory is insufficient because a detector that sees danger everywhere can appear sensitive while being unusably intrusive. Milestone 2 therefore adds paired controls and boundary cases.

The corpus now includes:

- figurative finality without a distress cluster;
- restorative withdrawal with continued human connection;
- heavy workload without isolation or shame;
- humor during genuine accumulated distress;
- substantial ordinary distress that warrants `CARE` but not social-reconnection framing;
- explicit self-harm language in calm context that still warrants clarification;
- supplied acute-safety evidence that routes to the host/provider safety policy.

Together with the original fixture, these cases cover every current care stage. Corpus tests require every published JSON fixture to match its authored ground truth and assert the key specificity boundaries directly.

See [`CORPUS.md`](CORPUS.md) for the fixture-by-fixture design matrix.

## Validity limitation: implementation consistency is not clinical truth

The current fixtures are protocol test cases written by the same project that defines the thresholds. Their labels are reasoned judgments, not independently established clinical ground truth.

A perfect fixture score proves that the implementation behaves consistently with those authored judgments. It does **not** prove that:

- the thresholds are clinically valid;
- the chosen observations are the correct interpretation of natural language;
- another qualified reviewer would choose the same stage;
- the stage transition improves outcomes for real users.

There is a circularity risk if fixture authors knowingly choose numerical observations that land on the thresholds they already implemented. This limitation must remain explicit rather than allowing a 100% test score to be presented as evidence of safety effectiveness.

## Privacy rule for fixtures

Public benchmark fixtures must be synthetic or independently consented for publication.

Do not copy private user transcripts, identifying relationship details, names, locations, or distinctive personal disclosures into this repository merely because they inspired a failure mode. A real interaction may motivate an abstract test case; the published fixture should preserve the behavioral pattern without preserving the person's story.

## What the current evaluation does not measure

The current evaluator does not measure:

- whether a model can infer the observation vector from text;
- whether the thresholds are clinically valid;
- whether the generated response satisfies a response contract;
- longitudinal decay or automatic evidence accumulation;
- age-sensitive threshold profiles;
- parental or trusted-contact notification;
- live proxy behavior;
- emergency response quality.

Those require separate evidence and should not be smuggled into a deterministic fixture test.

## Next evaluation step

Before natural-language inference is added, the next narrow step is twofold:

1. **Threshold-sensitivity analysis.** Perturb the numerical thresholds around their current values and report which fixture decisions remain stable or flip. Boundary cases that only pass at one hand-selected threshold should be visible.
2. **Independent-label review format.** Create a way for reviewers to assign expected stages without seeing the implementation's numeric threshold result, preserving disagreements instead of silently tuning them away.

Only after that foundation exists should ADCP begin testing whether a semantic detector can map natural-language trajectories into the observation schema.
