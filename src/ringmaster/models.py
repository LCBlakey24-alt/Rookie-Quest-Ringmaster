from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class MatchOutcome(str, Enum):
    CLEAN = "clean"
    DIRTY = "dirty"
    ROLL_UP = "roll_up"
    DQ = "dq"
    NO_CONTEST = "no_contest"


@dataclass(frozen=True)
class Wrestler:
    id: str
    ring_name: str
    technique: int
    psychology: int
    stamina: int
    athleticism: int
    safety: int
    charisma: int
    popularity: int
    fatigue: int = 0

    @property
    def in_ring_average(self) -> float:
        return (self.technique + self.psychology + self.stamina + self.athleticism + self.safety) / 5


@dataclass(frozen=True)
class Segment:
    name: str
    length_minutes: int
    hype: int
    storyline_heat: int

    def normalized_length_factor(self) -> float:
        if self.length_minutes <= 6:
            return 0.9
        if self.length_minutes <= 15:
            return 1.0
        if self.length_minutes <= 25:
            return 0.95
        return 0.85
