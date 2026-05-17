from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ContractType(str, Enum):
    EXCLUSIVE = "exclusive"
    NON_EXCLUSIVE = "non_exclusive"
    INDEPENDENT = "independent"


@dataclass(frozen=True)
class WrestlerCareerState:
    wrestler_name: str
    popularity: int
    money: float
    morale: int
    reliability: int
    injuries: int


@dataclass(frozen=True)
class BookingOpportunity:
    city: str
    show_name: str
    payout: float
    risk: int
    mandatory_attendance: bool


@dataclass(frozen=True)
class LifestyleChoiceResult:
    state: WrestlerCareerState
    note: str


class WrestlerCareerRPG:
    def apply_contract(self, state: WrestlerCareerState, contract: ContractType) -> WrestlerCareerState:
        if contract == ContractType.EXCLUSIVE:
            return WrestlerCareerState(
                wrestler_name=state.wrestler_name,
                popularity=min(100, state.popularity + 4),
                money=state.money + 25_000,
                morale=max(0, state.morale - 3),
                reliability=min(100, state.reliability + 5),
                injuries=state.injuries,
            )
        if contract == ContractType.NON_EXCLUSIVE:
            return WrestlerCareerState(
                state.wrestler_name,
                min(100, state.popularity + 2),
                state.money + 12_000,
                state.morale,
                min(100, state.reliability + 2),
                state.injuries,
            )
        return WrestlerCareerState(
            state.wrestler_name,
            min(100, state.popularity + 1),
            state.money + 6_000,
            min(100, state.morale + 2),
            state.reliability,
            state.injuries,
        )

    def decide_booking_attendance(
        self,
        state: WrestlerCareerState,
        booking: BookingOpportunity,
        skip_for_personal_activity: bool,
    ) -> LifestyleChoiceResult:
        if not skip_for_personal_activity:
            popularity_gain = 2 if booking.mandatory_attendance else 1
            injury_gain = 1 if booking.risk > 70 else 0
            return LifestyleChoiceResult(
                WrestlerCareerState(
                    wrestler_name=state.wrestler_name,
                    popularity=min(100, state.popularity + popularity_gain),
                    money=state.money + booking.payout,
                    morale=max(0, state.morale - (1 if booking.risk > 65 else 0)),
                    reliability=min(100, state.reliability + 1),
                    injuries=state.injuries + injury_gain,
                ),
                f"Worked {booking.show_name} in {booking.city}.",
            )

        if booking.mandatory_attendance:
            return LifestyleChoiceResult(
                WrestlerCareerState(
                    wrestler_name=state.wrestler_name,
                    popularity=max(0, state.popularity - 6),
                    money=state.money - 8_000,
                    morale=min(100, state.morale + 1),
                    reliability=max(0, state.reliability - 15),
                    injuries=state.injuries,
                ),
                "Skipped a mandatory booking: major backstage consequences.",
            )

        return LifestyleChoiceResult(
            WrestlerCareerState(
                wrestler_name=state.wrestler_name,
                popularity=max(0, state.popularity - 1),
                money=state.money,
                morale=min(100, state.morale + 2),
                reliability=max(0, state.reliability - 3),
                injuries=state.injuries,
            ),
            "Skipped optional booking for personal life activity.",
        )

    def in_match_decision(self, state: WrestlerCareerState, choose_safe_option: bool) -> LifestyleChoiceResult:
        if choose_safe_option:
            return LifestyleChoiceResult(
                WrestlerCareerState(
                    state.wrestler_name,
                    min(100, state.popularity + 1),
                    state.money,
                    state.morale,
                    min(100, state.reliability + 1),
                    state.injuries,
                ),
                "Chose safer sequence: lower pop, lower injury risk.",
            )

        return LifestyleChoiceResult(
            WrestlerCareerState(
                state.wrestler_name,
                min(100, state.popularity + 3),
                state.money,
                max(0, state.morale - 1),
                state.reliability,
                state.injuries + 1,
            ),
            "Chose high-risk spot: bigger pop, higher injury risk.",
        )
