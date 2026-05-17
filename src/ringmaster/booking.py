from __future__ import annotations

from dataclasses import dataclass

from .models import MatchOutcome, Segment


@dataclass(frozen=True)
class BookingSegment:
    segment: Segment
    preferred_outcome: MatchOutcome
    storyline_id: str | None = None


class BookingBoard:
    def __init__(self) -> None:
        self._segments: list[BookingSegment] = []

    @property
    def segments(self) -> list[BookingSegment]:
        return list(self._segments)

    def add_segment(self, item: BookingSegment) -> None:
        self._segments.append(item)

    def move_segment(self, from_index: int, to_index: int) -> None:
        if from_index < 0 or from_index >= len(self._segments):
            raise IndexError("from_index out of range")
        if to_index < 0 or to_index >= len(self._segments):
            raise IndexError("to_index out of range")
        item = self._segments.pop(from_index)
        self._segments.insert(to_index, item)

    def total_minutes(self) -> int:
        return sum(item.segment.length_minutes for item in self._segments)

    def pacing_warnings(self) -> list[str]:
        warnings: list[str] = []
        if not self._segments:
            return ["No segments booked"]

        # warn if too many long segments in a row
        long_streak = 0
        for item in self._segments:
            if item.segment.length_minutes >= 20:
                long_streak += 1
                if long_streak >= 2:
                    warnings.append("Two or more long segments back-to-back may hurt crowd pacing")
                    break
            else:
                long_streak = 0

        # warn if card length is too short/long
        total = self.total_minutes()
        if total < 60:
            warnings.append("Card runtime is short; audience may feel under-served")
        if total > 180:
            warnings.append("Card runtime is very long; fatigue risk increased")

        return warnings
