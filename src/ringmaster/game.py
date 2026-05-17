from __future__ import annotations

from dataclasses import dataclass

from .models import MatchOutcome, Segment, Wrestler
from .sim import SegmentResult, SimulationEngine


@dataclass(frozen=True)
class BookingSlot:
    segment: Segment
    wrestler_a: Wrestler
    wrestler_b: Wrestler
    outcome: MatchOutcome


class WeeklyShow:
    def __init__(self, name: str, seed: int) -> None:
        self.name = name
        self.engine = SimulationEngine(seed=seed)
        self.slots: list[BookingSlot] = []

    def add_slot(self, slot: BookingSlot) -> None:
        self.slots.append(slot)

    def run(self) -> list[SegmentResult]:
        return [
            self.engine.simulate_segment(slot.segment, slot.wrestler_a, slot.wrestler_b, slot.outcome)
            for slot in self.slots
        ]

    @staticmethod
    def average_rating(results: list[SegmentResult]) -> float:
        if not results:
            return 0.0
        return round(sum(r.rating for r in results) / len(results), 2)
