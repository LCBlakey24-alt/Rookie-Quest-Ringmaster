from __future__ import annotations

from dataclasses import dataclass

from .campaign import CampaignEngine, CampaignSnapshot
from .finance import FinanceEngine, FinanceSnapshot
from .promotion import PromotionPlanner
from .production import EntranceAssignment, EntranceBudgetManager, EntranceDemand


@dataclass(frozen=True)
class RuntimeWeekResult:
    snapshot: CampaignSnapshot
    finance: FinanceSnapshot
    fan_trust_delta: float
    entrance_morale_delta: float


class CareerRuntimeService:
    def __init__(self) -> None:
        self.finance = FinanceEngine()
        self.promotion = PromotionPlanner()
        self.entrance = EntranceBudgetManager()

    def advance_week(
        self,
        campaign: CampaignEngine,
        weekly_shows: int,
        monthly_ppvs: int,
        starting_cash: float,
        attendance: int,
        ticket_price: float,
        sponsor_revenue: float,
        payroll_cost: float,
        venue_cost: float,
        production_cost: float,
        entrance_budget: float,
        star_demand: float,
    ) -> RuntimeWeekResult:
        snap = campaign.advance_week(popularity_gain=max(1, 3 - max(0, weekly_shows - 3)), budget_gain=40_000)

        finance = self.finance.project_week(
            starting_cash=starting_cash,
            attendance=attendance,
            ticket_price=ticket_price,
            sponsor_revenue=sponsor_revenue,
            payroll_cost=payroll_cost,
            venue_cost=venue_cost,
            production_cost=production_cost,
        )

        cadence = self.promotion.evaluate_balance(weekly_shows, monthly_ppvs)
        entrance = self.entrance.evaluate(
            total_budget=entrance_budget,
            demands=[EntranceDemand("top_star", minimum_budget=star_demand, star_power=80)],
            assignments=[EntranceAssignment("top_star", allocated_budget=entrance_budget)],
        )

        return RuntimeWeekResult(
            snapshot=snap,
            finance=finance,
            fan_trust_delta=cadence.projected_fan_trust_delta,
            entrance_morale_delta=entrance.morale_penalty,
        )
