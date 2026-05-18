from ringmaster.models import MatchOutcome, Segment, Wrestler
from ringmaster.sim import SimulationEngine


def build_wrestlers() -> tuple[Wrestler, Wrestler]:
    a = Wrestler("a", "Alpha", 80, 80, 80, 80, 80, 70, 65, 10)
    b = Wrestler("b", "Bravo", 70, 75, 78, 72, 74, 68, 60, 20)
    return a, b


def test_deterministic_with_same_seed() -> None:
    a, b = build_wrestlers()
    segment = Segment("Test", 12, 70, 75)

    first = SimulationEngine(seed=123).simulate_segment(segment, a, b, MatchOutcome.CLEAN)
    second = SimulationEngine(seed=123).simulate_segment(segment, a, b, MatchOutcome.CLEAN)

    assert first.rating == second.rating
    assert first.injury_risk_roll == second.injury_risk_roll


def test_rating_bounds() -> None:
    a, b = build_wrestlers()
    segment = Segment("Test", 40, 100, 100)

    result = SimulationEngine(seed=999).simulate_segment(segment, a, b, MatchOutcome.NO_CONTEST)
    assert 0.0 <= result.rating <= 100.0
