from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from .contracts import Contract
from .finance import FinanceEngine, FinanceSnapshot
from .game import WeeklyShow
from .models import MatchOutcome
from .morale import MoraleEngine, MoraleState
from .storylines import Storyline, StorylineEngine


@dataclass(frozen=True)
class WeeklyReport:
    show_name: str
    show_average_rating: float
    finance: FinanceSnapshot
    expiring_contract_ids: list[str]
    updated_storylines: list[Storyline]
    morale_updates: list[MoraleState]


class WeeklyLoop:
    def __init__(self, finance_engine: FinanceEngine | None = None, storyline_engine: StorylineEngine | None = None, morale_engine: MoraleEngine | None = None) -> None:
        self.finance_engine = finance_engine or FinanceEngine()
        self.storyline_engine = storyline_engine or StorylineEngine()
        self.morale_engine = morale_engine or MoraleEngine()

    def run_week(
        self,
        today: date,
        show: WeeklyShow,
        contracts: list[Contract],
        starting_cash: float,
        attendance: int,
        ticket_price: float,
        sponsor_revenue: float,
        venue_cost: float,
        production_cost: float,
        storylines: list[Storyline] | None = None,
    ) -> WeeklyReport:
        results = show.run()
        rating = WeeklyShow.average_rating(results)

        payroll = round(sum(c.weekly_cost(1) for c in contracts), 2)
        finance = self.finance_engine.project_week(
            starting_cash=starting_cash,
            attendance=attendance,
            ticket_price=ticket_price,
            sponsor_revenue=sponsor_revenue,
            payroll_cost=payroll,
            venue_cost=venue_cost,
            production_cost=production_cost,
        )
        expiring = [c.wrestler_id for c in contracts if c.expires_within_days(today, 30)]

        updated_storylines: list[Storyline] = []
        if storylines and results:
            main_rating = results[-1].rating
            for s in storylines:
                updated_storylines.append(self.storyline_engine.progress(s, main_rating, clean_finish=True))

        morale_updates: list[MoraleState] = []
        if show.slots and results:
            latest = results[-1]
            for slot in show.slots:
                won_a = slot.outcome in {MatchOutcome.CLEAN, MatchOutcome.DIRTY, MatchOutcome.ROLL_UP}
                morale_updates.append(self.morale_engine.apply_show_result(MoraleState(slot.wrestler_a.id, 50), latest.rating, won_a))
                morale_updates.append(self.morale_engine.apply_show_result(MoraleState(slot.wrestler_b.id, 50), latest.rating, not won_a))

        return WeeklyReport(show.name, rating, finance, expiring, updated_storylines, morale_updates)
