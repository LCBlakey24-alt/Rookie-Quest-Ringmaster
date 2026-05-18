from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Storyline:
    id: str
    name: str
    wrestler_a_id: str
    wrestler_b_id: str
    heat: int = 50
    weeks_running: int = 0

    def clamped_heat(self) -> int:
        return max(0, min(100, self.heat))


class StorylineEngine:
    def progress(self, storyline: Storyline, segment_rating: float, clean_finish: bool) -> Storyline:
        heat_delta = 0
        if segment_rating >= 80:
            heat_delta += 8
        elif segment_rating >= 65:
            heat_delta += 4
        elif segment_rating < 50:
            heat_delta -= 6

        if clean_finish:
            heat_delta += 1

        new_heat = max(0, min(100, storyline.heat + heat_delta))
        return Storyline(
            id=storyline.id,
            name=storyline.name,
            wrestler_a_id=storyline.wrestler_a_id,
            wrestler_b_id=storyline.wrestler_b_id,
            heat=new_heat,
            weeks_running=storyline.weeks_running + 1,
        )
