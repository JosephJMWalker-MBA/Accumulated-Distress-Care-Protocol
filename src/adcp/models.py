"""Core data types for the Accumulated Distress Care Protocol."""

from __future__ import annotations

from dataclasses import dataclass, fields
from enum import IntEnum, StrEnum


class Severity(IntEnum):
    """Bounded observation severity for ordinary-distress dimensions."""

    ABSENT = 0
    WEAK = 1
    MEANINGFUL = 2
    STRONG = 3


class CareStage(StrEnum):
    """Ordered care posture selected by the deterministic policy."""

    NORMAL = "normal"
    STRAIN = "strain"
    CARE = "care"
    ACTIVE_RECONNECTION = "active_reconnection"
    SAFETY_CLARIFICATION = "safety_clarification"
    ACUTE_SAFETY = "acute_safety"


@dataclass(frozen=True, slots=True)
class ObservationVector:
    """Conversation observations consumed by the Milestone 0 policy.

    These fields are not diagnoses or durable user attributes. They describe
    evidence available to one evaluation of the conversation trajectory.
    """

    isolation: Severity = Severity.ABSENT
    interpersonal_rupture: Severity = Severity.ABSENT
    shame: Severity = Severity.ABSENT
    exhaustion: Severity = Severity.ABSENT
    self_care_neglect: Severity = Severity.ABSENT
    withdrawal: Severity = Severity.ABSENT
    finality_language: Severity = Severity.ABSENT
    human_contact_deficit: Severity = Severity.ABSENT
    self_harm_language: bool = False
    acute_safety_evidence: bool = False
    humor_present: bool = False

    ORDINARY_DIMENSIONS = (
        "isolation",
        "interpersonal_rupture",
        "shame",
        "exhaustion",
        "self_care_neglect",
        "withdrawal",
        "finality_language",
        "human_contact_deficit",
    )

    def __post_init__(self) -> None:
        for field in fields(self):
            if field.name not in self.ORDINARY_DIMENSIONS:
                continue
            value = getattr(self, field.name)
            if not isinstance(value, Severity):
                raise TypeError(f"{field.name} must be a Severity, got {type(value).__name__}")

    @property
    def burden(self) -> int:
        """Return the simple additive burden across ordinary dimensions."""

        return sum(int(getattr(self, name)) for name in self.ORDINARY_DIMENSIONS)

    @property
    def active_dimensions(self) -> int:
        """Count ordinary dimensions with meaningful-or-strong evidence."""

        return sum(
            getattr(self, name) >= Severity.MEANINGFUL for name in self.ORDINARY_DIMENSIONS
        )


@dataclass(frozen=True, slots=True)
class ResponseContract:
    """Machine-readable behavioral constraints for a selected care stage."""

    stage: CareStage
    requirements: tuple[str, ...]
    avoid: tuple[str, ...]
