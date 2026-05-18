from pathlib import Path

from ringmaster.universe import create_custom_brand, generate_universe


def test_generate_universe_has_country_brand_coverage() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    uni = generate_universe(repo_root)

    assert len(uni.countries) >= 20
    assert len(uni.brands) == len(uni.countries)
    assert all(uni.shows_by_brand[b.id] for b in uni.brands)


def test_create_custom_brand_is_added() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    uni = generate_universe(repo_root)
    before = len(uni.brands)

    brand = create_custom_brand(uni, name="Global Outlaws", home_country="US", starting_budget=450000)

    assert len(uni.brands) == before + 1
    assert brand.id in uni.shows_by_brand
