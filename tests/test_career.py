from ringmaster.campaign import CampaignSnapshot
from ringmaster.career import CareerDashboardService
from ringmaster.finance import FinanceSnapshot
from ringmaster.production import EntranceBudgetReport
from ringmaster.promotion import PromotionBalanceReport
from ringmaster.storylines import Storyline


def test_career_dashboard_ranks_storylines_by_heat() -> None:
    service = CareerDashboardService()

    dash = service.build(
        snapshot=CampaignSnapshot(week=3, player_brand_id="b1", world_rank=4, market_share=5.2, world_domination_score=61.4),
        finance=FinanceSnapshot(100000, 50000, 10000, 20000, 12000, 9000),
        cadence=PromotionBalanceReport(weekly_shows=4, monthly_ppvs=2, workload_penalty=4.5, ppv_saturation_penalty=6.0, total_penalty=10.5, projected_fan_trust_delta=-3.68),
        entrance=EntranceBudgetReport(total_budget=70000, assigned_budget=60000, unassigned_budget=10000, underfunded_wrestlers=["w1"], crowd_bonus=1.6, morale_penalty=-2.0),
        storylines=[
            Storyline("s1", "A", "w1", "w2", heat=60, weeks_running=4),
            Storyline("s2", "B", "w3", "w4", heat=88, weeks_running=2),
            Storyline("s3", "C", "w5", "w6", heat=75, weeks_running=1),
        ],
    )

    assert dash.top_storylines[0].id == "s2"
    assert len(dash.top_storylines) == 3
