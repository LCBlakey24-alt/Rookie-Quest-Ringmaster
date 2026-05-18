from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StaffMember:
    id: str
    name: str
    role: str
    style: str
    skill: int
    salary: float


@dataclass(frozen=True)
class RosterNeed:
    style_focus: str
    technical_demand: int
    creative_demand: int


@dataclass(frozen=True)
class StaffSynergyReport:
    creative_bonus: float
    technical_bonus: float
    mismatch_penalty: float
    payroll_pressure: float
    net_effect: float


class StaffOffice:
    def evaluate_synergy(self, staff: list[StaffMember], need: RosterNeed, budget: float) -> StaffSynergyReport:
        creative = [s for s in staff if s.role in {"writer", "producer", "music"}]
        technical = [s for s in staff if s.role in {"technical", "lighting", "audio"}]

        creative_bonus = sum(s.skill for s in creative) / 120 if creative else 0.0
        technical_bonus = sum(s.skill for s in technical) / 120 if technical else 0.0

        mismatch_penalty = 0.0
        for s in staff:
            if s.style != need.style_focus:
                mismatch_penalty += 0.8

        payroll = sum(s.salary for s in staff)
        payroll_pressure = max(0.0, (payroll - budget) / max(1.0, budget) * 10)

        demand_gap = 0.0
        if creative_bonus * 20 < need.creative_demand:
            demand_gap += (need.creative_demand - creative_bonus * 20) / 25
        if technical_bonus * 20 < need.technical_demand:
            demand_gap += (need.technical_demand - technical_bonus * 20) / 25

        mismatch_penalty += demand_gap

        net = creative_bonus + technical_bonus - mismatch_penalty - payroll_pressure
        return StaffSynergyReport(
            creative_bonus=round(creative_bonus, 2),
            technical_bonus=round(technical_bonus, 2),
            mismatch_penalty=round(mismatch_penalty, 2),
            payroll_pressure=round(payroll_pressure, 2),
            net_effect=round(net, 2),
        )
