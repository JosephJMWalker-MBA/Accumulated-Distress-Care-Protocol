from __future__ import annotations

from pathlib import Path

import pytest

from adcp import CareStage
from adcp.transcript import evaluate_fixture, load_fixture

FIXTURES = Path(__file__).parents[1] / "fixtures"


@pytest.mark.parametrize("path", sorted(FIXTURES.glob("*.json")), ids=lambda path: path.stem)
def test_every_published_fixture_matches_ground_truth(path: Path) -> None:
    result = evaluate_fixture(load_fixture(path))

    assert result.passed, (
        f"{result.fixture_id} mismatches: "
        f"{[(item.turn, item.expected_stage, item.actual_stage) for item in result.mismatches]}"
    )


def _stages(name: str) -> tuple[CareStage, ...]:
    fixture = load_fixture(FIXTURES / name)
    return tuple(turn.expected_stage for turn in fixture.turns)


def test_corpus_covers_every_care_stage() -> None:
    covered = {
        turn.expected_stage
        for path in FIXTURES.glob("*.json")
        for turn in load_fixture(path).turns
    }

    assert covered == set(CareStage)


def test_benign_figurative_finality_does_not_trigger_safety_clarification() -> None:
    stages = _stages("benign_figurative_finality.json")

    assert stages == (CareStage.NORMAL, CareStage.STRAIN, CareStage.NORMAL)
    assert CareStage.SAFETY_CLARIFICATION not in stages
    assert CareStage.ACUTE_SAFETY not in stages


def test_restorative_withdrawal_never_reaches_care_or_higher() -> None:
    stages = _stages("restorative_withdrawal.json")

    assert stages == (CareStage.STRAIN, CareStage.STRAIN, CareStage.NORMAL)
    assert max(_stage_rank(stage) for stage in stages) < _stage_rank(CareStage.CARE)


def test_high_workload_without_social_distress_stays_below_care() -> None:
    stages = _stages("high_workload_connected.json")

    assert stages == (CareStage.NORMAL, CareStage.STRAIN, CareStage.STRAIN)


def test_humor_does_not_block_care_or_reconnection() -> None:
    stages = _stages("humor_during_accumulated_distress.json")

    assert stages == (
        CareStage.STRAIN,
        CareStage.CARE,
        CareStage.ACTIVE_RECONNECTION,
    )


def test_high_burden_with_intact_social_connection_stays_at_care() -> None:
    stages = _stages("care_without_reconnection.json")

    assert stages == (CareStage.CARE, CareStage.CARE)


def test_explicit_self_harm_language_routes_to_clarification_not_acute() -> None:
    stages = _stages("explicit_self_harm_calm_context.json")

    assert stages == (CareStage.NORMAL, CareStage.SAFETY_CLARIFICATION)
    assert CareStage.ACUTE_SAFETY not in stages


def test_supplied_acute_evidence_routes_to_acute_safety() -> None:
    stages = _stages("supplied_acute_safety_evidence.json")

    assert stages == (CareStage.SAFETY_CLARIFICATION, CareStage.ACUTE_SAFETY)


def _stage_rank(stage: CareStage) -> int:
    order = (
        CareStage.NORMAL,
        CareStage.STRAIN,
        CareStage.CARE,
        CareStage.ACTIVE_RECONNECTION,
        CareStage.SAFETY_CLARIFICATION,
        CareStage.ACUTE_SAFETY,
    )
    return order.index(stage)
