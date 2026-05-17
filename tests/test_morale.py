from ringmaster.morale import MoraleEngine, MoraleState


def test_morale_changes_by_result_quality() -> None:
    baseline = MoraleState("a", morale=50)
    win_state = MoraleEngine().apply_show_result(baseline, match_rating=78, won=True)
    loss_state = MoraleEngine().apply_show_result(baseline, match_rating=40, won=False)
    assert win_state.morale > baseline.morale
    assert loss_state.morale < baseline.morale
