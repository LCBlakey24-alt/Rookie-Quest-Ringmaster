from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Country:
    code: str
    name: str
    region: str
    population_m: int


@dataclass(frozen=True)
class Brand:
    id: str
    name: str
    home_country: str
    quality: int
    popularity: int
    budget: float


@dataclass(frozen=True)
class ShowTemplate:
    name: str
    weekly: bool


@dataclass
class Universe:
    countries: list[Country] = field(default_factory=list)
    brands: list[Brand] = field(default_factory=list)
    shows_by_brand: dict[str, list[ShowTemplate]] = field(default_factory=dict)

    def get_brand(self, brand_id: str) -> Brand | None:
        return next((b for b in self.brands if b.id == brand_id), None)

    def rankings(self) -> list[Brand]:
        return sorted(self.brands, key=lambda b: (b.popularity * 0.7 + b.quality * 0.3, b.budget), reverse=True)
