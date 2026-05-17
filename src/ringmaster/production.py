from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProductionInventory:
    lighting_tier: int = 1
    laser_tier: int = 0
    pyro_tier: int = 0


@dataclass(frozen=True)
class EntranceDemand:
    wrestler_id: str
    minimum_budget: float
    star_power: int


@dataclass(frozen=True)
class EntranceAssignment:
    wrestler_id: str
    allocated_budget: float


@dataclass(frozen=True)
class EntranceBudgetReport:
    total_budget: float
    assigned_budget: float
    unassigned_budget: float
    underfunded_wrestlers: list[str]
    crowd_bonus: float
    morale_penalty: float


class ProductionPlanner:
    def upgrade_cost(self, inventory: ProductionInventory, category: str) -> float:
        if category == "lighting":
            return 80_000 + inventory.lighting_tier * 35_000
        if category == "laser":
            return 120_000 + inventory.laser_tier * 50_000
        if category == "pyro":
            return 150_000 + inventory.pyro_tier * 60_000
        raise ValueError(f"Unknown category: {category}")

    def apply_upgrade(self, inventory: ProductionInventory, category: str) -> ProductionInventory:
        if category == "lighting":
            return ProductionInventory(inventory.lighting_tier + 1, inventory.laser_tier, inventory.pyro_tier)
        if category == "laser":
            return ProductionInventory(inventory.lighting_tier, inventory.laser_tier + 1, inventory.pyro_tier)
        if category == "pyro":
            return ProductionInventory(inventory.lighting_tier, inventory.laser_tier, inventory.pyro_tier + 1)
        raise ValueError(f"Unknown category: {category}")


class EntranceBudgetManager:
    def evaluate(
        self,
        total_budget: float,
        demands: list[EntranceDemand],
        assignments: list[EntranceAssignment],
    ) -> EntranceBudgetReport:
        assigned = round(sum(a.allocated_budget for a in assignments), 2)
        remaining = round(total_budget - assigned, 2)

        assigned_map = {a.wrestler_id: a.allocated_budget for a in assignments}
        underfunded: list[str] = []
        crowd_bonus = 0.0
        morale_penalty = 0.0

        for d in demands:
            given = assigned_map.get(d.wrestler_id, 0.0)
            if given < d.minimum_budget:
                underfunded.append(d.wrestler_id)
                morale_penalty -= min(8.0, (d.minimum_budget - given) / 10_000)
            else:
                crowd_bonus += min(6.0, (given - d.minimum_budget) / 15_000 + d.star_power * 0.01)

        if remaining < 0:
            morale_penalty -= 3.5

        return EntranceBudgetReport(
            total_budget=round(total_budget, 2),
            assigned_budget=assigned,
            unassigned_budget=remaining,
            underfunded_wrestlers=underfunded,
            crowd_bonus=round(crowd_bonus, 2),
            morale_penalty=round(morale_penalty, 2),
        )
