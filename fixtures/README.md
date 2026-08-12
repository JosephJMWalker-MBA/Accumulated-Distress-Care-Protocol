# ADCP Evaluation Fixtures

Fixtures in this directory are test artifacts for the deterministic ADCP policy.

## Publication rule

Fixtures committed to this public repository must be either:

1. fully synthetic; or
2. independently consented for public release with appropriate de-identification.

A private conversation may reveal a useful failure pattern, but its wording, names, identifying circumstances, and distinctive personal disclosures should not be copied into the public benchmark by default.

## Milestone 1 semantics

Each turn is an evaluation checkpoint containing a human-authored observation **snapshot** and expected care stage. The evaluator does not infer observations from the illustrative text and does not automatically accumulate or decay evidence across turns.

This keeps the first benchmark focused on deterministic threshold behavior before semantic classification is introduced.
