from ringmaster.steam import SteamLaunchPlanner, SteamReadiness


def test_steam_completion_percent() -> None:
    r = SteamReadiness(True, False, False, True, False, True)
    assert r.completion_percent() == 50.0


def test_steam_checklist_generates_missing_items() -> None:
    r = SteamReadiness(False, False, False, False, False, False)
    checklist = SteamLaunchPlanner().checklist(r)
    assert len(checklist) == 6
    assert any("Steam Cloud" in item for item in checklist)
