# ADCP Evaluation Fixtures

Fixtures in this directory are test artifacts for the deterministic ADCP policy.

## Publication rule

Fixtures committed to this public repository must be either:

1. fully synthetic; or
2. independently consented for public release with appropriate de-identification.

A private conversation may reveal a useful failure pattern, but its wording, names, identifying circumstances, and distinctive personal disclosures should not be copied into the public benchmark by default.

## Current semantics

Each turn is an evaluation checkpoint containing a human-authored observation **snapshot** and expected care stage. The evaluator does not infer observations from the illustrative text and does not automatically accumulate or decay evidence across turns.

This keeps the benchmark focused on deterministic threshold behavior before semantic classification is introduced.

## Corpus design

The fixture set is intentionally control-balanced rather than escalation-heavy. It includes cases where ADCP should escalate and cases where alarming surface language, fatigue, withdrawal, or humor should **not** trigger a disproportionate care stage.

Current contrast families include:

- benign figurative finality versus clustered finality;
- restorative withdrawal versus isolating withdrawal;
- high workload with intact connection versus accumulated distress;
- humor in ordinary strain versus humor during substantial distress;
- `CARE` with intact human support versus `ACTIVE_RECONNECTION` when social disconnection is meaningful;
- explicit self-harm language versus supplied acute-safety evidence.

See [`../docs/CORPUS.md`](../docs/CORPUS.md) for the design matrix and validity limitations.

## Ground-truth limitation

Expected stages are protocol-development judgments, not clinical labels. Passing every fixture demonstrates consistency with the authored protocol, not clinical effectiveness. The project must preserve this distinction as the corpus grows.
