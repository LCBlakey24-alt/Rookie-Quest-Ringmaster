from __future__ import annotations

from dataclasses import dataclass

from .world import Brand, Universe


@dataclass(frozen=True)
class CampaignSnapshot:
    week: int
    player_brand_id: str
    world_rank: int
    market_share: float
    world_domination_score: float


class CampaignEngine:
    """Tracks global progression toward world-domination goals."""

    def __init__(self, universe: Universe, player_brand_id: str) -> None:
        self.universe = universe
        self.player_brand_id = player_brand_id
        self.week = 1

    def _ranking(self) -> list[Brand]:
        return self.universe.rankings()

    def _market_share(self, brand: Brand) -> float:
        total_pop = sum(max(1, b.popularity) for b in self.universe.brands)
        return round((brand.popularity / total_pop) * 100, 2)

    def _domination_score(self, brand: Brand, rank: int) -> float:
        # weighted blend of popularity dominance, quality, budget strength, and world rank bonus
        rank_bonus = max(0.0, 35.0 - (rank - 1) * 2.0)
        budget_factor = min(25.0, brand.budget / 200_000)
        return round(brand.popularity * 0.5 + brand.quality * 0.3 + budget_factor + rank_bonus, 2)

    def snapshot(self) -> CampaignSnapshot:
        ranking = self._ranking()
        brand = self.universe.get_brand(self.player_brand_id)
        if brand is None:
            raise ValueError(f"Unknown player brand id: {self.player_brand_id}")

        rank = next(i for i, b in enumerate(ranking, 1) if b.id == brand.id)
        return CampaignSnapshot(
            week=self.week,
            player_brand_id=brand.id,
            world_rank=rank,
            market_share=self._market_share(brand),
            world_domination_score=self._domination_score(brand, rank),
        )

    def advance_week(self, popularity_gain: int = 1, budget_gain: float = 25_000.0) -> CampaignSnapshot:
        updated_brands: list[Brand] = []
        for b in self.universe.brands:
            if b.id == self.player_brand_id:
                updated_brands.append(
                    Brand(
                        id=b.id,
                        name=b.name,
                        home_country=b.home_country,
                        quality=min(100, b.quality + 1),
                        popularity=min(100, b.popularity + popularity_gain),
                        budget=b.budget + budget_gain,
                    )
                )
            else:
                updated_brands.append(b)

        self.universe.brands = updated_brands
        self.week += 1
        return self.snapshot()
