from __future__ import annotations

from dataclasses import dataclass

from .campaign import CampaignSnapshot
from .finance import FinanceSnapshot
from .promotion import PromotionBalanceReport
from .production import EntranceBudgetReport
from .storylines import Storyline


@dataclass(frozen=True)
class CareerDashboard:
    snapshot: CampaignSnapshot
    finance: FinanceSnapshot
    cadence: PromotionBalanceReport
    entrance: EntranceBudgetReport
    top_storylines: list[Storyline]


class CareerDashboardService:
    def build(
        self,
        snapshot: CampaignSnapshot,
        finance: FinanceSnapshot,
        cadence: PromotionBalanceReport,
        entrance: EntranceBudgetReport,
        storylines: list[Storyline],
    ) -> CareerDashboard:
        ranked_storylines = sorted(storylines, key=lambda s: (s.heat, -s.weeks_running), reverse=True)
        return CareerDashboard(
            snapshot=snapshot,
            finance=finance,
            cadence=cadence,
            entrance=entrance,
            top_storylines=ranked_storylines[:5],
        )
