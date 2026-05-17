from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Prospect:
    wrestler_id: str
    name: str
    potential: int
    readiness: int
    loyalty: int


@dataclass(frozen=True)
class DevelopmentShowPlan:
    enabled: bool
    weekly_cost: float
    training_quality: int


@dataclass(frozen=True)
class DevelopmentReport:
    trained: list[Prospect]
    total_cost: float
    warnings: list[str]


class DevelopmentSystem:
    def plan_show(self, enabled: bool, training_quality: int) -> DevelopmentShowPlan:
        if training_quality < 1 or training_quality > 100:
            raise ValueError("training_quality must be between 1 and 100")
        weekly_cost = 0.0 if not enabled else round(20_000 + training_quality * 600, 2)
        return DevelopmentShowPlan(enabled=enabled, weekly_cost=weekly_cost, training_quality=training_quality)

    def run_week(self, prospects: list[Prospect], plan: DevelopmentShowPlan) -> DevelopmentReport:
        if not plan.enabled:
            return DevelopmentReport(trained=prospects, total_cost=0.0, warnings=["Development show disabled"])

        trained: list[Prospect] = []
        for p in prospects:
            growth = max(1, plan.training_quality // 20)
            new_readiness = min(100, p.readiness + growth)
            trained.append(Prospect(p.wrestler_id, p.name, p.potential, new_readiness, p.loyalty))

        return DevelopmentReport(trained=trained, total_cost=plan.weekly_cost, warnings=[])

    def evaluate_promotion_decision(self, trained_prospect: Prospect, signed_external_free_agent: bool) -> tuple[Prospect, str]:
        """If player skips prospect promotion and signs external talent, prospect loyalty drops."""
        if not signed_external_free_agent:
            boosted = Prospect(
                trained_prospect.wrestler_id,
                trained_prospect.name,
                trained_prospect.potential,
                min(100, trained_prospect.readiness + 3),
                min(100, trained_prospect.loyalty + 4),
            )
            return boosted, "Prospect promoted internally; loyalty and readiness improved"

        dropped = Prospect(
            trained_prospect.wrestler_id,
            trained_prospect.name,
            trained_prospect.potential,
            trained_prospect.readiness,
            max(0, trained_prospect.loyalty - 12),
        )
        return dropped, "External signing blocked pathway; prospect loyalty dropped"
