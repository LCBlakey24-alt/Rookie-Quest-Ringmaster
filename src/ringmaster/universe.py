from __future__ import annotations

import json
from pathlib import Path

from .fictional import FictionalBrandSeed, fictional_brand_name
from .world import Brand, Country, ShowTemplate, Universe


def load_countries(repo_root: Path) -> list[Country]:
    data = json.loads((repo_root / "data" / "world" / "countries.json").read_text())
    return [Country(**item) for item in data]


def create_default_brands(countries: list[Country]) -> list[Brand]:
    brands: list[Brand] = []
    for idx, c in enumerate(countries, 1):
        brands.append(
            Brand(
                id=f"brand_{c.code.lower()}",
                name=fictional_brand_name(FictionalBrandSeed(c.code, c.name)),
                home_country=c.code,
                quality=max(45, min(95, 50 + (idx % 10) * 4)),
                popularity=max(35, min(95, 40 + (c.population_m // 20))),
                budget=float(200_000 + c.population_m * 2_500),
            )
        )
    return brands


def create_shows_for_brand(brand: Brand) -> list[ShowTemplate]:
    return [
        ShowTemplate(name=f"{brand.name} Weekly", weekly=True),
        ShowTemplate(name=f"{brand.name} Clash", weekly=False),
    ]


def generate_universe(repo_root: Path) -> Universe:
    countries = load_countries(repo_root)
    brands = create_default_brands(countries)
    shows_by_brand = {brand.id: create_shows_for_brand(brand) for brand in brands}
    return Universe(countries=countries, brands=brands, shows_by_brand=shows_by_brand)


def create_custom_brand(universe: Universe, name: str, home_country: str, starting_budget: float = 300_000.0) -> Brand:
    country_codes = {c.code for c in universe.countries}
    if home_country not in country_codes:
        raise ValueError(f"Unknown country code: {home_country}")

    brand_id = "custom_" + name.lower().replace(" ", "_")
    custom = Brand(
        id=brand_id,
        name=name,
        home_country=home_country,
        quality=55,
        popularity=30,
        budget=starting_budget,
    )
    universe.brands.append(custom)
    universe.shows_by_brand[custom.id] = create_shows_for_brand(custom)
    return custom
