from __future__ import annotations

from pathlib import Path

from .campaign import CampaignEngine
from .universe import create_custom_brand, generate_universe


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    universe = generate_universe(repo_root)

    rankings = universe.rankings()[:5]
    print("Top 5 Brands (Starting Universe):")
    for i, brand in enumerate(rankings, 1):
        print(f"{i}. {brand.name} [{brand.home_country}] | Pop {brand.popularity} | Quality {brand.quality} | Budget ${brand.budget:,.0f}")

    custom = create_custom_brand(universe, name="Player Created League", home_country="US", starting_budget=500000)
    print("\nCreated custom brand:")
    print(f"- {custom.name} ({custom.id}) in {custom.home_country}")
    print(f"- Shows: {', '.join(show.name for show in universe.shows_by_brand[custom.id])}")

    campaign = CampaignEngine(universe, player_brand_id=custom.id)
    start = campaign.snapshot()
    print("\nCampaign snapshot:")
    print(f"- Week {start.week} | Rank #{start.world_rank} | Market Share {start.market_share}% | Domination Score {start.world_domination_score}")

    progressed = campaign.advance_week(popularity_gain=3, budget_gain=120000)
    print("After one successful week:")
    print(f"- Week {progressed.week} | Rank #{progressed.world_rank} | Market Share {progressed.market_share}% | Domination Score {progressed.world_domination_score}")


if __name__ == "__main__":
    main()
