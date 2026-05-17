from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PromotionProfile:
    brand_id: str
    starting_cash: float
    weekly_shows: int
    monthly_ppvs: int


@dataclass(frozen=True)
class PromotionBalanceReport:
    weekly_shows: int
    monthly_ppvs: int
    workload_penalty: float
    ppv_saturation_penalty: float
    total_penalty: float
    projected_fan_trust_delta: float


class PromotionPlanner:
    """Planning rules for show cadence and sustainable growth."""

    MIN_STARTING_CASH = 50_000.0
    MAX_STARTING_CASH = 10_000_000.0

    def create_profile(
        self,
        brand_id: str,
        starting_cash: float,
        weekly_shows: int,
        monthly_ppvs: int,
    ) -> PromotionProfile:
        if not (self.MIN_STARTING_CASH <= starting_cash <= self.MAX_STARTING_CASH):
            raise ValueError("starting_cash out of allowed range")
        if weekly_shows < 1 or weekly_shows > 7:
            raise ValueError("weekly_shows must be between 1 and 7")
        if monthly_ppvs < 0 or monthly_ppvs > 4:
            raise ValueError("monthly_ppvs must be between 0 and 4")

        return PromotionProfile(
            brand_id=brand_id,
            starting_cash=round(starting_cash, 2),
            weekly_shows=weekly_shows,
            monthly_ppvs=monthly_ppvs,
        )

    def evaluate_balance(self, weekly_shows: int, monthly_ppvs: int) -> PromotionBalanceReport:
        workload_penalty = 0.0
        if weekly_shows > 3:
            workload_penalty = (weekly_shows - 3) * 4.5

        ppv_saturation_penalty = 0.0
        if monthly_ppvs > 1:
            ppv_saturation_penalty = (monthly_ppvs - 1) * 6.0

        total = round(workload_penalty + ppv_saturation_penalty, 2)
        projected_fan_trust_delta = round(-total * 0.35, 2)

        return PromotionBalanceReport(
            weekly_shows=weekly_shows,
            monthly_ppvs=monthly_ppvs,
            workload_penalty=round(workload_penalty, 2),
            ppv_saturation_penalty=round(ppv_saturation_penalty, 2),
            total_penalty=total,
            projected_fan_trust_delta=projected_fan_trust_delta,
        )

    def can_expand_show_count(self, available_cash: float, current_weekly_shows: int) -> bool:
        next_show_cost = 120_000 + current_weekly_shows * 35_000
        return available_cash >= next_show_cost and current_weekly_shows < 7

    def can_add_ppv(self, available_cash: float, current_monthly_ppvs: int) -> bool:
        next_ppv_cost = 300_000 + current_monthly_ppvs * 90_000
        return available_cash >= next_ppv_cost and current_monthly_ppvs < 4
