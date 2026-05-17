from __future__ import annotations

from dataclasses import dataclass

from .ppv import PPVEvent, PPVScheduler
from .production import EntranceAssignment, EntranceBudgetManager, EntranceDemand, EntranceBudgetReport
from .promotion import PromotionBalanceReport, PromotionPlanner


@dataclass(frozen=True)
class WeeklyPlanningSummary:
    cadence: PromotionBalanceReport
    entrance: EntranceBudgetReport
    ppv_events: list[PPVEvent]


class PlanningDashboardService:
    def __init__(self) -> None:
        self.promotion_planner = PromotionPlanner()
        self.entrance_manager = EntranceBudgetManager()
        self.ppv_scheduler = PPVScheduler()

    def build_summary(
        self,
        weekly_shows: int,
        monthly_ppvs: int,
        entrance_budget: float,
        demands: list[EntranceDemand],
        assignments: list[EntranceAssignment],
        ppv_names: list[str],
        ppv_themes: list[str],
    ) -> WeeklyPlanningSummary:
        cadence = self.promotion_planner.evaluate_balance(weekly_shows, monthly_ppvs)
        entrance = self.entrance_manager.evaluate(entrance_budget, demands, assignments)
        ppv_events = self.ppv_scheduler.build_monthly_schedule(ppv_names, ppv_themes)
        return WeeklyPlanningSummary(cadence=cadence, entrance=entrance, ppv_events=ppv_events)
