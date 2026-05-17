from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Contract:
    wrestler_id: str
    downside_guarantee: float
    appearance_bonus: float
    expires_on: date

    def weekly_cost(self, appearances: int) -> float:
        return round(self.downside_guarantee + (self.appearance_bonus * appearances), 2)

    def expires_within_days(self, on_date: date, days: int = 30) -> bool:
        return 0 <= (self.expires_on - on_date).days <= days
