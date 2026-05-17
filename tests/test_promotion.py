from ringmaster.promotion import PromotionPlanner


def test_balance_penalties_increase_for_overbooking() -> None:
    planner = PromotionPlanner()
    normal = planner.evaluate_balance(weekly_shows=2, monthly_ppvs=1)
    heavy = planner.evaluate_balance(weekly_shows=6, monthly_ppvs=3)

    assert normal.total_penalty == 0
    assert heavy.total_penalty > normal.total_penalty
    assert heavy.projected_fan_trust_delta < 0


def test_expansion_requires_cash() -> None:
    planner = PromotionPlanner()
    assert planner.can_expand_show_count(available_cash=500_000, current_weekly_shows=2)
    assert not planner.can_expand_show_count(available_cash=10_000, current_weekly_shows=2)
