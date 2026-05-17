from ringmaster.fictional import FictionalBrandSeed, fictional_brand_name, fictional_wrestler_name


def test_fictional_brand_name_is_stable() -> None:
    seed = FictionalBrandSeed("US", "United States")
    assert fictional_brand_name(seed) == fictional_brand_name(seed)


def test_fictional_wrestler_name_shape() -> None:
    name = fictional_wrestler_name("sample_seed")
    assert len(name.split()) == 2
