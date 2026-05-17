from pathlib import Path

from ringmaster.campaign import CampaignEngine
from ringmaster.savegame import create_save, load_from_file, save_to_file
from ringmaster.universe import create_custom_brand, generate_universe


def test_savegame_roundtrip(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    universe = generate_universe(repo_root)
    player = create_custom_brand(universe, "Save Test", "US", 450000)
    campaign = CampaignEngine(universe, player_brand_id=player.id)
    snapshot = campaign.advance_week(popularity_gain=2, budget_gain=50000)

    save = create_save(player.id, week=snapshot.week, brands=universe.brands, snapshot=snapshot)
    out = tmp_path / "career_save.json"
    save_to_file(save, out)

    loaded = load_from_file(out)
    assert loaded.player_brand_id == save.player_brand_id
    assert loaded.week == save.week
    assert len(loaded.brands) == len(save.brands)
    assert loaded.last_snapshot is not None
    assert loaded.last_snapshot.world_domination_score == snapshot.world_domination_score
