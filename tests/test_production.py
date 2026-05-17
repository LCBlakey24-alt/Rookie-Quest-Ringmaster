from ringmaster.production import (
    EntranceAssignment,
    EntranceBudgetManager,
    EntranceDemand,
    ProductionInventory,
    ProductionPlanner,
)


def test_upgrade_costs_increase_by_tier() -> None:
    planner = ProductionPlanner()
    inv = ProductionInventory(lighting_tier=1, laser_tier=0, pyro_tier=0)
    c1 = planner.upgrade_cost(inv, "lighting")
    inv2 = planner.apply_upgrade(inv, "lighting")
    c2 = planner.upgrade_cost(inv2, "lighting")
    assert c2 > c1


def test_entrance_budget_underfunding_penalty() -> None:
    manager = EntranceBudgetManager()
    demands = [
        EntranceDemand("w1", minimum_budget=50_000, star_power=75),
        EntranceDemand("w2", minimum_budget=25_000, star_power=55),
    ]
    assignments = [
        EntranceAssignment("w1", allocated_budget=30_000),
        EntranceAssignment("w2", allocated_budget=28_000),
    ]

    report = manager.evaluate(70_000, demands, assignments)
    assert "w1" in report.underfunded_wrestlers
    assert report.morale_penalty < 0
