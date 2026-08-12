from __future__ import annotations

import pytest

from adcp import CareStage, ObservationVector, Severity, classify_stage, evaluate


@pytest.mark.parametrize(
    ("observations", "expected"),
    [
        (ObservationVector(), CareStage.NORMAL),
        (
            ObservationVector(isolation=Severity.WEAK, shame=Severity.WEAK),
            CareStage.STRAIN,
        ),
        (
            ObservationVector(
                interpersonal_rupture=Severity.STRONG,
                exhaustion=Severity.STRONG,
                shame=Severity.WEAK,
            ),
            CareStage.CARE,
        ),
        (
            ObservationVector(
                isolation=Severity.STRONG,
                interpersonal_rupture=Severity.STRONG,
                shame=Severity.MEANINGFUL,
                exhaustion=Severity.MEANINGFUL,
                withdrawal=Severity.MEANINGFUL,
            ),
            CareStage.ACTIVE_RECONNECTION,
        ),
        (
            ObservationVector(
                finality_language=Severity.MEANINGFUL,
                isolation=Severity.MEANINGFUL,
                shame=Severity.MEANINGFUL,
            ),
            CareStage.SAFETY_CLARIFICATION,
        ),
        (
            ObservationVector(self_harm_language=True),
            CareStage.SAFETY_CLARIFICATION,
        ),
        (
            ObservationVector(
                acute_safety_evidence=True,
                self_harm_language=True,
            ),
            CareStage.ACUTE_SAFETY,
        ),
    ],
)
def test_stage_classification(observations: ObservationVector, expected: CareStage) -> None:
    assert classify_stage(observations) is expected


def test_humor_never_lowers_stage() -> None:
    without_humor = ObservationVector(
        isolation=Severity.STRONG,
        interpersonal_rupture=Severity.STRONG,
        shame=Severity.MEANINGFUL,
        exhaustion=Severity.MEANINGFUL,
        withdrawal=Severity.MEANINGFUL,
    )
    with_humor = ObservationVector(
        isolation=Severity.STRONG,
        interpersonal_rupture=Severity.STRONG,
        shame=Severity.MEANINGFUL,
        exhaustion=Severity.MEANINGFUL,
        withdrawal=Severity.MEANINGFUL,
        humor_present=True,
    )

    assert classify_stage(without_humor) is CareStage.ACTIVE_RECONNECTION
    assert classify_stage(with_humor) is classify_stage(without_humor)


def test_figurative_finality_alone_does_not_force_safety_clarification() -> None:
    observations = ObservationVector(finality_language=Severity.MEANINGFUL)

    assert classify_stage(observations) is CareStage.STRAIN


def test_ambiguous_finality_requires_context_cluster() -> None:
    one_context_signal = ObservationVector(
        finality_language=Severity.MEANINGFUL,
        isolation=Severity.MEANINGFUL,
    )
    two_context_signals = ObservationVector(
        finality_language=Severity.MEANINGFUL,
        isolation=Severity.MEANINGFUL,
        withdrawal=Severity.MEANINGFUL,
    )

    assert classify_stage(one_context_signal) is CareStage.STRAIN
    assert classify_stage(two_context_signals) is CareStage.SAFETY_CLARIFICATION


def test_contract_matches_classified_stage() -> None:
    contract = evaluate(
        ObservationVector(
            isolation=Severity.STRONG,
            interpersonal_rupture=Severity.STRONG,
            exhaustion=Severity.MEANINGFUL,
            self_care_neglect=Severity.MEANINGFUL,
            human_contact_deficit=Severity.MEANINGFUL,
        )
    )

    assert contract.stage is CareStage.ACTIVE_RECONNECTION
    assert "keep_ai_role_bounded" in contract.requirements
    assert "maximize_session_duration" in contract.avoid


def test_severity_fields_require_severity_enum() -> None:
    with pytest.raises(TypeError, match="isolation must be a Severity"):
        ObservationVector(isolation=2)  # type: ignore[arg-type]
