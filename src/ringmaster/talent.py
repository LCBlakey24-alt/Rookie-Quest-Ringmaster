from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TalentProfile:
    id: str
    ring_name: str
    alignment: str
    style: str
    age: int
    draw: int
    crowd_reaction: int
    dangerous: int
    injury_prone: int
    injures_others_risk: int
    promo: int
    finisher_name: str
    finisher_popularity: int
    technical: int
    psychology: int
    stamina: int
    athleticism: int
    safety: int


class TalentPool:
    @staticmethod
    def load_free_agents(repo_root: Path) -> list[TalentProfile]:
        payload = json.loads((repo_root / "data" / "samples" / "free_agents.json").read_text())
        return [TalentProfile(**p) for p in payload]


class TalentTrainer:
    def train_finisher(self, profile: TalentProfile, weeks: int, coach_skill: int) -> TalentProfile:
        gain = max(1, (coach_skill // 20) + (weeks // 2))
        return TalentProfile(**{**profile.__dict__, "finisher_popularity": min(100, profile.finisher_popularity + gain)})

    def train_promo(self, profile: TalentProfile, weeks: int, coach_skill: int) -> TalentProfile:
        gain = max(1, (coach_skill // 22) + (weeks // 2))
        return TalentProfile(**{**profile.__dict__, "promo": min(100, profile.promo + gain)})

    def train_safety(self, profile: TalentProfile, weeks: int, coach_skill: int) -> TalentProfile:
        gain = max(1, (coach_skill // 24) + (weeks // 3))
        new_safety = min(100, profile.safety + gain)
        new_injures_others = max(0, profile.injures_others_risk - (gain // 2))
        return TalentProfile(**{**profile.__dict__, "safety": new_safety, "injures_others_risk": new_injures_others})
