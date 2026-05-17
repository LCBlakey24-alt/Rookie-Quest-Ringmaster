from ringmaster.development import DevelopmentSystem, Prospect


def test_development_show_improves_readiness() -> None:
    system = DevelopmentSystem()
    plan = system.plan_show(enabled=True, training_quality=70)
    prospects = [Prospect("p1", "Rook Steel", potential=84, readiness=40, loyalty=65)]

    report = system.run_week(prospects, plan)
    assert report.total_cost > 0
    assert report.trained[0].readiness > prospects[0].readiness


def test_external_signing_can_reduce_loyalty() -> None:
    system = DevelopmentSystem()
    prospect = Prospect("p1", "Rook Steel", potential=84, readiness=60, loyalty=70)

    updated, note = system.evaluate_promotion_decision(prospect, signed_external_free_agent=True)
    assert updated.loyalty < prospect.loyalty
    assert "loyalty dropped" in note
