from ringmaster.career_rpg import (
    BookingOpportunity,
    ContractType,
    WrestlerCareerRPG,
    WrestlerCareerState,
)


def _state() -> WrestlerCareerState:
    return WrestlerCareerState("Rook Steel", popularity=40, money=10000, morale=65, reliability=70, injuries=0)


def test_mandatory_skip_has_strong_penalty() -> None:
    engine = WrestlerCareerRPG()
    booking = BookingOpportunity("Tokyo", "Mega Dome", payout=12000, risk=72, mandatory_attendance=True)
    result = engine.decide_booking_attendance(_state(), booking, skip_for_personal_activity=True)
    assert result.state.reliability < 70
    assert result.state.popularity < 40


def test_risky_in_match_choice_trades_pop_for_injury() -> None:
    engine = WrestlerCareerRPG()
    result = engine.in_match_decision(_state(), choose_safe_option=False)
    assert result.state.popularity > 40
    assert result.state.injuries == 1


def test_exclusive_contract_boosts_money_and_popularity() -> None:
    engine = WrestlerCareerRPG()
    updated = engine.apply_contract(_state(), ContractType.EXCLUSIVE)
    assert updated.money > 10000
    assert updated.popularity > 40
