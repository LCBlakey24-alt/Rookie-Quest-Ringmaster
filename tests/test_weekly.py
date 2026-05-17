from datetime import date, timedelta

from ringmaster.contracts import Contract
from ringmaster.game import BookingSlot, WeeklyShow
from ringmaster.models import MatchOutcome, Segment, Wrestler
from ringmaster.storylines import Storyline
from ringmaster.weekly import WeeklyLoop


def test_weekly_loop_finance_and_contract_alerts() -> None:
    a = Wrestler("a", "Alpha", 80, 80, 80, 80, 80, 70, 65, 10)
    b = Wrestler("b", "Bravo", 70, 75, 78, 72, 74, 68, 60, 20)

    show = WeeklyShow("Friday Fight", seed=12)
    show.add_slot(BookingSlot(Segment("Main", 18, 80, 78), a, b, MatchOutcome.CLEAN))

    today = date(2026, 5, 17)
    contracts = [
        Contract("a", downside_guarantee=1500, appearance_bonus=250, expires_on=today + timedelta(days=14)),
        Contract("b", downside_guarantee=1200, appearance_bonus=200, expires_on=today + timedelta(days=90)),
    ]

    report = WeeklyLoop().run_week(
        today=today,
        show=show,
        contracts=contracts,
        starting_cash=100000,
        attendance=1200,
        ticket_price=25,
        sponsor_revenue=3500,
        venue_cost=8000,
        production_cost=5000,
        storylines=[Storyline("f1", "Main Feud", "a", "b", heat=55, weeks_running=2)],
    )

    assert report.show_average_rating > 0
    assert report.finance.ticket_revenue == 30000
    assert report.finance.ending_cash > report.finance.starting_cash
    assert report.expiring_contract_ids == ["a"]


    assert len(report.updated_storylines) == 1
    assert report.updated_storylines[0].weeks_running == 3
    assert len(report.morale_updates) == 2
