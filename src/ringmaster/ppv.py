from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PPVEvent:
    name: str
    week_of_month: int
    theme: str


class PPVScheduler:
    def build_monthly_schedule(self, event_names: list[str], themes: list[str]) -> list[PPVEvent]:
        if len(event_names) > 4:
            raise ValueError("A month can support at most 4 PPVs in this prototype")

        events: list[PPVEvent] = []
        for idx, name in enumerate(event_names, start=1):
            theme = themes[idx - 1] if idx - 1 < len(themes) else "Classic"
            events.append(PPVEvent(name=name, week_of_month=idx, theme=theme))
        return events
