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
    winner_id: str | None = None
    finish_type: str | None = None
    loser_protected: bool = False
    storyline_id: str | None = None

    def resolved_winner_id(self) -> str | None:
        """Return the winner for legacy slots and explicit modern bookings.

        Older prototype code only stored an outcome, so by default decisive finishes
        are treated as wrestler_a winning. DQ/no-contest finishes are non-decisive
        unless a winner_id is explicitly supplied by newer booking flows.
        """
        if self.winner_id:
            return self.winner_id
        if self.outcome in {MatchOutcome.CLEAN, MatchOutcome.DIRTY, MatchOutcome.ROLL_UP}:
            return self.wrestler_a.id
        return None

    def is_clean_finish(self) -> bool:
        return self.outcome == MatchOutcome.CLEAN


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
