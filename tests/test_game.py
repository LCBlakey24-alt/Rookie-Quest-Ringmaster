from ringmaster.game import BookingSlot, WeeklyShow
from ringmaster.models import MatchOutcome, Segment, Wrestler


def test_weekly_show_average_rating() -> None:
    a = Wrestler("a", "Alpha", 80, 80, 80, 80, 80, 70, 65, 10)
    b = Wrestler("b", "Bravo", 70, 75, 78, 72, 74, 68, 60, 20)

    show = WeeklyShow("Test Show", seed=7)
    show.add_slot(BookingSlot(Segment("Opener", 10, 65, 60), a, b, MatchOutcome.CLEAN))
    show.add_slot(BookingSlot(Segment("Main", 18, 80, 82), a, b, MatchOutcome.DIRTY))

    results = show.run()
    assert len(results) == 2
    assert WeeklyShow.average_rating(results) > 0
