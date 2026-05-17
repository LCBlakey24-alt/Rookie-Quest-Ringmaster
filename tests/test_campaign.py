from pathlib import Path

from ringmaster.campaign import CampaignEngine
from ringmaster.universe import create_custom_brand, generate_universe


def test_campaign_snapshot_and_progression() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    universe = generate_universe(repo_root)
    brand = create_custom_brand(universe, "World Rising", "US", 400000)

    campaign = CampaignEngine(universe, player_brand_id=brand.id)
    s1 = campaign.snapshot()
    s2 = campaign.advance_week(popularity_gain=3, budget_gain=100000)

    assert s2.week == s1.week + 1
    assert s2.world_domination_score > s1.world_domination_score
    assert s2.market_share >= s1.market_share
