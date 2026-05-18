from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MoraleState:
    wrestler_id: str
    morale: int = 50


class MoraleEngine:
    def apply_show_result(self, state: MoraleState, match_rating: float, won: bool) -> MoraleState:
        delta = 0
        if match_rating >= 75:
            delta += 6
        elif match_rating >= 60:
            delta += 3
        elif match_rating < 45:
            delta -= 8

        if won:
            delta += 2
        else:
            delta -= 1

        return MoraleState(state.wrestler_id, max(0, min(100, state.morale + delta)))
