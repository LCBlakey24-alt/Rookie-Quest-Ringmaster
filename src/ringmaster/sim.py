from __future__ import annotations

import random
from dataclasses import dataclass

from .models import MatchOutcome, Segment, Wrestler


@dataclass(frozen=True)
class SegmentResult:
    segment_name: str
    rating: float
    crowd_reaction: str
    injury_risk_roll: float


class SimulationEngine:
    """Deterministic simulation core using a seed-scoped RNG."""

    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)

    def simulate_segment(
        self,
        segment: Segment,
        wrestler_a: Wrestler,
        wrestler_b: Wrestler,
        outcome: MatchOutcome,
    ) -> SegmentResult:
        base_in_ring = (wrestler_a.in_ring_average + wrestler_b.in_ring_average) / 2
        promo_boost = (wrestler_a.charisma + wrestler_b.charisma) / 40
        popularity_boost = (wrestler_a.popularity + wrestler_b.popularity) / 50
        fatigue_penalty = (wrestler_a.fatigue + wrestler_b.fatigue) / 30

        outcome_modifier = {
            MatchOutcome.CLEAN: 1.05,
            MatchOutcome.DIRTY: 0.98,
            MatchOutcome.ROLL_UP: 0.95,
            MatchOutcome.DQ: 0.9,
            MatchOutcome.NO_CONTEST: 0.85,
        }[outcome]

        noise = self._rng.uniform(-3.0, 3.0)
        raw = (
            base_in_ring * 0.5
            + segment.hype * 0.2
            + segment.storyline_heat * 0.2
            + promo_boost
            + popularity_boost
            - fatigue_penalty
            + noise
        ) * segment.normalized_length_factor() * outcome_modifier

        rating = max(0.0, min(100.0, round(raw, 2)))
        injury_risk_roll = round(self._rng.random(), 4)

        if rating >= 85:
            crowd = "Electric"
        elif rating >= 70:
            crowd = "Hot"
        elif rating >= 55:
            crowd = "Warm"
        else:
            crowd = "Cold"

        return SegmentResult(segment.name, rating, crowd, injury_risk_roll)
