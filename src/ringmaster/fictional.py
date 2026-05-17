from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FictionalBrandSeed:
    country_code: str
    country_name: str


BRAND_PREFIXES = [
    "Iron",
    "Neon",
    "Crimson",
    "Titan",
    "Storm",
    "Midnight",
    "Rogue",
    "Solar",
    "Atlas",
    "Phantom",
]

BRAND_SUFFIXES = [
    "Grapple",
    "Ring",
    "Combat",
    "Crown",
    "Slam",
    "Clash",
    "Arena",
    "Circuit",
    "Alliance",
    "Federation",
]

WRESTLER_FIRST = [
    "Jett", "Nova", "Rex", "Vera", "Knox", "Sable", "Orion", "Blaze", "Kira", "Dax"
]

WRESTLER_LAST = [
    "Havoc", "Vale", "Storm", "Drake", "Voss", "Riot", "Crowe", "Frost", "Wilde", "Knight"
]


def _stable_idx(value: str, mod: int) -> int:
    return sum(ord(c) for c in value) % mod


def fictional_brand_name(seed: FictionalBrandSeed) -> str:
    p = BRAND_PREFIXES[_stable_idx(seed.country_code + seed.country_name, len(BRAND_PREFIXES))]
    s = BRAND_SUFFIXES[_stable_idx(seed.country_name + seed.country_code, len(BRAND_SUFFIXES))]
    return f"{p} {s}"


def fictional_wrestler_name(seed: str) -> str:
    first = WRESTLER_FIRST[_stable_idx(seed, len(WRESTLER_FIRST))]
    last = WRESTLER_LAST[_stable_idx(seed[::-1], len(WRESTLER_LAST))]
    return f"{first} {last}"
