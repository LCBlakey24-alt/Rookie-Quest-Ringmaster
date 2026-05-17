from pathlib import Path

from ringmaster.campaign import CampaignEngine
from ringmaster.runtime import CareerRuntimeService
from ringmaster.universe import create_custom_brand, generate_universe


def test_runtime_advance_week_produces_outputs() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    universe = generate_universe(repo_root)
    brand = create_custom_brand(universe, "Runtime League", "US", 500000)
    campaign = CampaignEngine(universe, brand.id)

    result = CareerRuntimeService().advance_week(
        campaign=campaign,
        weekly_shows=3,
        monthly_ppvs=1,
        starting_cash=500000,
        attendance=1200,
        ticket_price=30,
        sponsor_revenue=10000,
        payroll_cost=22000,
        venue_cost=10000,
        production_cost=8000,
        entrance_budget=60000,
        star_demand=50000,
    )

    assert result.snapshot.week == 2
    assert result.finance.ending_cash > result.finance.starting_cash
