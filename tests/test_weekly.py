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
    show.add_slot(BookingSlot(Segment("Main", 18, 80, 78), a, b, MatchOutcome.CLEAN, storyline_id="f1"))

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


def test_weekly_loop_uses_each_segment_rating_for_morale() -> None:
    a = Wrestler("a", "Alpha", 95, 95, 95, 95, 95, 90, 90, 0)
    b = Wrestler("b", "Bravo", 95, 95, 95, 95, 95, 90, 90, 0)
    c = Wrestler("c", "Charlie", 10, 10, 10, 10, 10, 10, 10, 90)
    d = Wrestler("d", "Delta", 10, 10, 10, 10, 10, 10, 10, 90)

    show = WeeklyShow("Split Quality Card", seed=3)
    show.add_slot(BookingSlot(Segment("Hot Opener", 18, 100, 100), a, b, MatchOutcome.CLEAN))
    show.add_slot(BookingSlot(Segment("Cold Main", 4, 1, 1), c, d, MatchOutcome.NO_CONTEST))

    today = date(2026, 5, 17)
    report = WeeklyLoop().run_week(
        today=today,
        show=show,
        contracts=[],
        starting_cash=100000,
        attendance=500,
        ticket_price=20,
        sponsor_revenue=1000,
        venue_cost=3000,
        production_cost=2000,
    )

    morale_by_wrestler = {state.wrestler_id: state.morale for state in report.morale_updates}

    assert morale_by_wrestler["a"] > 50
    assert morale_by_wrestler["b"] >= 50
    assert morale_by_wrestler["c"] < 50
    assert morale_by_wrestler["d"] < 50


def test_weekly_loop_only_charges_appearance_bonus_for_booked_wrestlers() -> None:
    booked = Wrestler("booked", "Booked Star", 80, 80, 80, 80, 80, 70, 65, 0)
    opponent = Wrestler("opp", "Opponent", 70, 70, 70, 70, 70, 60, 60, 0)

    show = WeeklyShow("Payroll Test", seed=4)
    show.add_slot(BookingSlot(Segment("Main", 15, 80, 80), booked, opponent, MatchOutcome.CLEAN))

    today = date(2026, 5, 17)
    contracts = [
        Contract("booked", downside_guarantee=1000, appearance_bonus=500, expires_on=today + timedelta(days=60)),
        Contract("inactive", downside_guarantee=1000, appearance_bonus=500, expires_on=today + timedelta(days=60)),
    ]

    report = WeeklyLoop().run_week(
        today=today,
        show=show,
        contracts=contracts,
        starting_cash=100000,
        attendance=0,
        ticket_price=0,
        sponsor_revenue=0,
        venue_cost=0,
        production_cost=0,
    )

    assert report.finance.payroll_cost == 2500
