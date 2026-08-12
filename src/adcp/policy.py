"""Deterministic Milestone 0 care-stage policy."""

from __future__ import annotations

from .models import CareStage, ObservationVector, ResponseContract, Severity


def classify_stage(observations: ObservationVector) -> CareStage:
    """Classify one observation snapshot into a care stage.

    Rules intentionally remain explicit and deterministic so threshold behavior
    can be evaluated before any semantic detector or production proxy is added.
    """

    if observations.acute_safety_evidence:
        return CareStage.ACUTE_SAFETY

    if observations.self_harm_language or _ambiguous_finality_cluster(observations):
        return CareStage.SAFETY_CLARIFICATION

    if (
        observations.burden >= 12
        and observations.active_dimensions >= 3
        and max(
            observations.isolation,
            observations.withdrawal,
            observations.human_contact_deficit,
        )
        >= Severity.MEANINGFUL
    ):
        return CareStage.ACTIVE_RECONNECTION

    if observations.burden >= 7 and observations.active_dimensions >= 2:
        return CareStage.CARE

    if observations.burden >= 2:
        return CareStage.STRAIN

    return CareStage.NORMAL


def response_contract(stage: CareStage) -> ResponseContract:
    """Return the behavioral contract associated with ``stage``."""

    return _CONTRACTS[stage]


def evaluate(observations: ObservationVector) -> ResponseContract:
    """Classify observations and return the resulting response contract."""

    return response_contract(classify_stage(observations))


def _ambiguous_finality_cluster(observations: ObservationVector) -> bool:
    if observations.finality_language < Severity.MEANINGFUL:
        return False

    contextual_dimensions = (
        observations.isolation,
        observations.shame,
        observations.withdrawal,
        observations.human_contact_deficit,
    )
    meaningful_context = sum(value >= Severity.MEANINGFUL for value in contextual_dimensions)
    return meaningful_context >= 2


_CONTRACTS: dict[CareStage, ResponseContract] = {
    CareStage.NORMAL: ResponseContract(
        stage=CareStage.NORMAL,
        requirements=(),
        avoid=(),
    ),
    CareStage.STRAIN: ResponseContract(
        stage=CareStage.STRAIN,
        requirements=(
            "respond_to_actual_topic",
            "preserve_uncertainty_about_unobserved_motives",
        ),
        avoid=(
            "amplify_contempt",
            "pathologize_single_cue",
        ),
    ),
    CareStage.CARE: ResponseContract(
        stage=CareStage.CARE,
        requirements=(
            "acknowledge_difficulty_without_generic_flattery",
            "offer_at_most_one_optional_embodied_action_when_natural",
        ),
        avoid=(
            "self_care_checklist",
            "diagnosis",
            "abrupt_handoff",
        ),
    ),
    CareStage.ACTIVE_RECONNECTION: ResponseContract(
        stage=CareStage.ACTIVE_RECONNECTION,
        requirements=(
            "continue_helping_with_stated_problem",
            "offer_exactly_one_low_burden_offline_or_embodied_action",
            "encourage_real_world_human_connection_when_natural",
            "keep_ai_role_bounded",
        ),
        avoid=(
            "exclusive_support_framing",
            "maximize_session_duration",
            "grievance_reinforcement",
        ),
    ),
    CareStage.SAFETY_CLARIFICATION: ResponseContract(
        stage=CareStage.SAFETY_CLARIFICATION,
        requirements=(
            "ask_one_short_direct_literal_vs_figurative_safety_question",
            "remain_calm_and_non_theatrical",
        ),
        avoid=(
            "assume_suicidality_from_metaphor_alone",
            "treat_humor_as_resolution",
        ),
    ),
    CareStage.ACUTE_SAFETY: ResponseContract(
        stage=CareStage.ACUTE_SAFETY,
        requirements=(
            "defer_to_validated_host_acute_safety_policy",
            "prioritize_immediate_human_safety_and_real_world_support",
        ),
        avoid=(
            "continue_as_ordinary_conversation",
            "invent_jurisdiction_specific_emergency_guidance",
        ),
    ),
}
