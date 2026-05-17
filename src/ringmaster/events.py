from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BackstageEvent:
    title: str
    description: str
    morale_delta: int
    cash_delta: float


class EventEngine:
    """Generates lightweight weekly backstage events from risk posture."""

    def generate(self, fan_trust_delta: float, entrance_morale_delta: float) -> list[BackstageEvent]:
        events: list[BackstageEvent] = []

        if fan_trust_delta <= -3.0:
            events.append(
                BackstageEvent(
                    title="Fan Fatigue Concerns",
                    description="Audience feedback says recent scheduling is too aggressive.",
                    morale_delta=-2,
                    cash_delta=-15000.0,
                )
            )

        if entrance_morale_delta < 0:
            events.append(
                BackstageEvent(
                    title="Top Star Entrance Dispute",
                    description="A major talent is unhappy with entrance production budget.",
                    morale_delta=-3,
                    cash_delta=0.0,
                )
            )

        if not events:
            events.append(
                BackstageEvent(
                    title="Locker Room Stable",
                    description="No major backstage incidents this week.",
                    morale_delta=1,
                    cash_delta=0.0,
                )
            )

        return events
