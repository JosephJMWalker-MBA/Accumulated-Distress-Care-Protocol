"""Accumulated Distress Care Protocol (ADCP)."""

from .models import CareStage, ObservationVector, ResponseContract, Severity
from .policy import classify_stage, evaluate, response_contract
from .transcript import (
    FixtureEvaluation,
    StageTransition,
    TranscriptFixture,
    TranscriptTurn,
    TurnEvaluation,
    evaluate_fixture,
    evaluate_fixture_path,
    fixture_from_mapping,
    load_fixture,
)

__all__ = [
    "CareStage",
    "FixtureEvaluation",
    "ObservationVector",
    "ResponseContract",
    "Severity",
    "StageTransition",
    "TranscriptFixture",
    "TranscriptTurn",
    "TurnEvaluation",
    "classify_stage",
    "evaluate",
    "evaluate_fixture",
    "evaluate_fixture_path",
    "fixture_from_mapping",
    "load_fixture",
    "response_contract",
]

__version__ = "0.2.0"
