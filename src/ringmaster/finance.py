from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FinanceSnapshot:
    starting_cash: float
    ticket_revenue: float
    sponsor_revenue: float
    payroll_cost: float
    venue_cost: float
    production_cost: float

    @property
    def net_income(self) -> float:
        return round(self.ticket_revenue + self.sponsor_revenue - self.payroll_cost - self.venue_cost - self.production_cost, 2)

    @property
    def ending_cash(self) -> float:
        return round(self.starting_cash + self.net_income, 2)


class FinanceEngine:
    def project_week(
        self,
        starting_cash: float,
        attendance: int,
        ticket_price: float,
        sponsor_revenue: float,
        payroll_cost: float,
        venue_cost: float,
        production_cost: float,
    ) -> FinanceSnapshot:
        ticket_revenue = round(attendance * ticket_price, 2)
        return FinanceSnapshot(
            starting_cash=round(starting_cash, 2),
            ticket_revenue=ticket_revenue,
            sponsor_revenue=round(sponsor_revenue, 2),
            payroll_cost=round(payroll_cost, 2),
            venue_cost=round(venue_cost, 2),
            production_cost=round(production_cost, 2),
        )
