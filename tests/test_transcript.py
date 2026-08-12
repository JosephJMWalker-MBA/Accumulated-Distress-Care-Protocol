from __future__ import annotations

from pathlib import Path

import pytest

from adcp import CareStage
from adcp.transcript import evaluate_fixture, fixture_from_mapping, load_fixture

FIXTURES = Path(__file__).parents[1] / "fixtures"


def test_first_adversarial_fixture_matches_ground_truth() -> None:
    fixture = load_fixture(FIXTURES / "ambiguous_social_rupture_with_humor.json")
    result = evaluate_fixture(fixture)

    assert result.passed
    assert result.accuracy == 1.0
    assert result.matches == result.total == 8
    assert result.mismatches == ()


def test_first_adversarial_fixture_transitions_at_expected_turns() -> None:
    fixture = load_fixture(FIXTURES / "ambiguous_social_rupture_with_humor.json")
    result = evaluate_fixture(fixture)

    actual = tuple(
        (transition.turn, transition.to_stage) for transition in result.actual_transitions
    )
    assert actual == (
        (1, CareStage.NORMAL),
        (2, CareStage.STRAIN),
        (4, CareStage.CARE),
        (6, CareStage.ACTIVE_RECONNECTION),
        (8, CareStage.SAFETY_CLARIFICATION),
    )
    assert result.actual_transitions == result.expected_transitions


def test_fixture_evaluation_reports_mismatch_without_mutating_policy() -> None:
    fixture = fixture_from_mapping(
        {
            "schema_version": 1,
            "fixture_id": "intentional_mismatch",
            "turns": [
                {
                    "turn": 1,
                    "text": "A single ordinary sentence.",
                    "observations": {},
                    "expected_stage": "care",
                }
            ],
        }
    )

    result = evaluate_fixture(fixture)

    assert not result.passed
    assert result.accuracy == 0.0
    assert len(result.mismatches) == 1
    assert result.mismatches[0].expected_stage is CareStage.CARE
    assert result.mismatches[0].actual_stage is CareStage.NORMAL


def test_fixture_rejects_unknown_observation_field() -> None:
    with pytest.raises(ValueError, match="unknown observation fields: diagnosis"):
        fixture_from_mapping(
            {
                "schema_version": 1,
                "fixture_id": "invalid_field",
                "turns": [
                    {
                        "turn": 1,
                        "text": "Synthetic text.",
                        "observations": {"diagnosis": 3},
                        "expected_stage": "normal",
                    }
                ],
            }
        )


def test_fixture_rejects_boolean_as_severity() -> None:
    with pytest.raises(ValueError, match="isolation must be an integer from 0 to 3"):
        fixture_from_mapping(
            {
                "schema_version": 1,
                "fixture_id": "bool_is_not_severity",
                "turns": [
                    {
                        "turn": 1,
                        "text": "Synthetic text.",
                        "observations": {"isolation": True},
                        "expected_stage": "normal",
                    }
                ],
            }
        )


def test_fixture_requires_strictly_increasing_turn_numbers() -> None:
    with pytest.raises(ValueError, match="turn numbers must be unique and strictly increasing"):
        fixture_from_mapping(
            {
                "schema_version": 1,
                "fixture_id": "duplicate_turns",
                "turns": [
                    {
                        "turn": 2,
                        "text": "First synthetic checkpoint.",
                        "observations": {},
                        "expected_stage": "normal",
                    },
                    {
                        "turn": 2,
                        "text": "Second synthetic checkpoint.",
                        "observations": {},
                        "expected_stage": "normal",
                    },
                ],
            }
        )


def test_fixture_rejects_unknown_schema_version() -> None:
    with pytest.raises(ValueError, match="schema_version must be 1"):
        fixture_from_mapping(
            {
                "schema_version": 2,
                "fixture_id": "future_schema",
                "turns": [
                    {
                        "turn": 1,
                        "text": "Synthetic text.",
                        "observations": {},
                        "expected_stage": "normal",
                    }
                ],
            }
        )
