from ringmaster.modes import GameMode, rules_for_mode


def test_promoter_mode_has_full_control() -> None:
    rules = rules_for_mode(GameMode.PROMOTER)
    assert rules.can_control_finances
    assert rules.can_control_storylines
    assert rules.can_force_match_winners


def test_general_manager_mode_hides_results_control() -> None:
    rules = rules_for_mode(GameMode.GENERAL_MANAGER)
    assert not rules.can_force_match_winners
    assert rules.uses_hidden_match_outcomes


def test_wrestler_career_focuses_on_single_wrestler_progression() -> None:
    rules = rules_for_mode(GameMode.WRESTLER_CAREER)
    assert rules.can_train_single_wrestler
    assert not rules.can_control_storylines
