from ringmaster.dashboard import PlanningDashboardService
from ringmaster.production import EntranceAssignment, EntranceDemand


def test_dashboard_combines_cadence_entrance_and_ppv() -> None:
    svc = PlanningDashboardService()
    summary = svc.build_summary(
        weekly_shows=4,
        monthly_ppvs=2,
        entrance_budget=70000,
        demands=[EntranceDemand("top_star", minimum_budget=50000, star_power=80)],
        assignments=[EntranceAssignment("top_star", allocated_budget=45000)],
        ppv_names=["Neon Collision"],
        ppv_themes=["Ladder"],
    )

    assert summary.cadence.total_penalty > 0
    assert summary.entrance.morale_penalty < 0
    assert len(summary.ppv_events) == 1
    assert summary.ppv_events[0].theme == "Ladder"
