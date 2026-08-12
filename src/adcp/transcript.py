"""Deterministic transcript-fixture evaluation for ADCP.

Milestone 1 intentionally consumes human-authored observation snapshots. It does
not infer observations from natural language and does not change live model
behavior.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .models import CareStage, ObservationVector, Severity
from .policy import classify_stage


@dataclass(frozen=True, slots=True)
class TranscriptTurn:
    """One user-turn evaluation checkpoint in a synthetic transcript fixture."""

    turn: int
    text: str
    observations: ObservationVector
    expected_stage: CareStage
    note: str = ""


@dataclass(frozen=True, slots=True)
class TranscriptFixture:
    """A versioned, synthetic multi-turn trajectory with human-authored labels."""

    schema_version: int
    fixture_id: str
    description: str
    turns: tuple[TranscriptTurn, ...]


@dataclass(frozen=True, slots=True)
class TurnEvaluation:
    """Expected-versus-actual classification for one fixture turn."""

    turn: int
    expected_stage: CareStage
    actual_stage: CareStage

    @property
    def passed(self) -> bool:
        return self.expected_stage is self.actual_stage


@dataclass(frozen=True, slots=True)
class StageTransition:
    """A stage change occurring at a fixture turn."""

    turn: int
    from_stage: CareStage | None
    to_stage: CareStage


@dataclass(frozen=True, slots=True)
class FixtureEvaluation:
    """Deterministic scoring result for an entire transcript fixture."""

    fixture_id: str
    turns: tuple[TurnEvaluation, ...]
    expected_transitions: tuple[StageTransition, ...]
    actual_transitions: tuple[StageTransition, ...]

    @property
    def passed(self) -> bool:
        return all(turn.passed for turn in self.turns)

    @property
    def matches(self) -> int:
        return sum(turn.passed for turn in self.turns)

    @property
    def total(self) -> int:
        return len(self.turns)

    @property
    def accuracy(self) -> float:
        return self.matches / self.total if self.total else 1.0

    @property
    def mismatches(self) -> tuple[TurnEvaluation, ...]:
        return tuple(turn for turn in self.turns if not turn.passed)


def load_fixture(path: str | Path) -> TranscriptFixture:
    """Load and strictly validate one JSON transcript fixture."""

    fixture_path = Path(path)
    with fixture_path.open(encoding="utf-8") as handle:
        payload = json.load(handle)

    if not isinstance(payload, dict):
        raise ValueError("fixture root must be a JSON object")

    return fixture_from_mapping(payload)


def fixture_from_mapping(payload: Mapping[str, Any]) -> TranscriptFixture:
    """Construct a validated fixture from already-decoded JSON-compatible data."""

    schema_version = payload.get("schema_version")
    if schema_version != 1:
        raise ValueError("schema_version must be 1")

    fixture_id = payload.get("fixture_id")
    if not isinstance(fixture_id, str) or not fixture_id.strip():
        raise ValueError("fixture_id must be a non-empty string")

    description = payload.get("description", "")
    if not isinstance(description, str):
        raise ValueError("description must be a string")

    raw_turns = payload.get("turns")
    if not isinstance(raw_turns, list) or not raw_turns:
        raise ValueError("turns must be a non-empty list")

    turns = tuple(_parse_turn(raw_turn) for raw_turn in raw_turns)
    turn_numbers = [turn.turn for turn in turns]
    if turn_numbers != sorted(turn_numbers) or len(set(turn_numbers)) != len(turn_numbers):
        raise ValueError("turn numbers must be unique and strictly increasing")

    return TranscriptFixture(
        schema_version=schema_version,
        fixture_id=fixture_id,
        description=description,
        turns=turns,
    )


def evaluate_fixture(fixture: TranscriptFixture) -> FixtureEvaluation:
    """Classify every fixture checkpoint and compare it with ground truth."""

    evaluations = tuple(
        TurnEvaluation(
            turn=turn.turn,
            expected_stage=turn.expected_stage,
            actual_stage=classify_stage(turn.observations),
        )
        for turn in fixture.turns
    )

    expected = tuple(turn.expected_stage for turn in fixture.turns)
    actual = tuple(turn.actual_stage for turn in evaluations)
    turn_numbers = tuple(turn.turn for turn in fixture.turns)

    return FixtureEvaluation(
        fixture_id=fixture.fixture_id,
        turns=evaluations,
        expected_transitions=_transitions(turn_numbers, expected),
        actual_transitions=_transitions(turn_numbers, actual),
    )


def evaluate_fixture_path(path: str | Path) -> FixtureEvaluation:
    """Load and evaluate a fixture in one call."""

    return evaluate_fixture(load_fixture(path))


def _parse_turn(payload: Any) -> TranscriptTurn:
    if not isinstance(payload, dict):
        raise ValueError("each turn must be a JSON object")

    turn = payload.get("turn")
    if isinstance(turn, bool) or not isinstance(turn, int) or turn <= 0:
        raise ValueError("turn must be a positive integer")

    text = payload.get("text")
    if not isinstance(text, str) or not text.strip():
        raise ValueError(f"turn {turn}: text must be a non-empty string")

    note = payload.get("note", "")
    if not isinstance(note, str):
        raise ValueError(f"turn {turn}: note must be a string")

    expected_raw = payload.get("expected_stage")
    try:
        expected_stage = CareStage(expected_raw)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"turn {turn}: invalid expected_stage {expected_raw!r}") from exc

    observations_raw = payload.get("observations", {})
    if not isinstance(observations_raw, dict):
        raise ValueError(f"turn {turn}: observations must be a JSON object")

    observations = _parse_observations(turn, observations_raw)
    return TranscriptTurn(
        turn=turn,
        text=text,
        observations=observations,
        expected_stage=expected_stage,
        note=note,
    )


def _parse_observations(turn: int, payload: Mapping[str, Any]) -> ObservationVector:
    allowed = set(ObservationVector.ORDINARY_DIMENSIONS) | {
        "self_harm_language",
        "acute_safety_evidence",
        "humor_present",
    }
    unknown = set(payload) - allowed
    if unknown:
        names = ", ".join(sorted(unknown))
        raise ValueError(f"turn {turn}: unknown observation fields: {names}")

    values: dict[str, Severity | bool] = {}
    for name in ObservationVector.ORDINARY_DIMENSIONS:
        raw = payload.get(name, 0)
        if isinstance(raw, bool) or not isinstance(raw, int):
            raise ValueError(f"turn {turn}: {name} must be an integer from 0 to 3")
        try:
            values[name] = Severity(raw)
        except ValueError as exc:
            raise ValueError(f"turn {turn}: {name} must be an integer from 0 to 3") from exc

    for name in ("self_harm_language", "acute_safety_evidence", "humor_present"):
        raw = payload.get(name, False)
        if not isinstance(raw, bool):
            raise ValueError(f"turn {turn}: {name} must be a boolean")
        values[name] = raw

    return ObservationVector(**values)


def _transitions(
    turn_numbers: tuple[int, ...], stages: tuple[CareStage, ...]
) -> tuple[StageTransition, ...]:
    transitions: list[StageTransition] = []
    previous: CareStage | None = None

    for turn, stage in zip(turn_numbers, stages, strict=True):
        if stage is not previous:
            transitions.append(StageTransition(turn=turn, from_stage=previous, to_stage=stage))
        previous = stage

    return tuple(transitions)
