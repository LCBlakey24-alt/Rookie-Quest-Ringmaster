from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SteamReadiness:
    cloud_save_ready: bool
    achievements_ready: bool
    workshop_ready: bool
    deck_profile_ready: bool
    controller_ui_ready: bool
    crash_reporting_ready: bool

    def completion_percent(self) -> float:
        flags = [
            self.cloud_save_ready,
            self.achievements_ready,
            self.workshop_ready,
            self.deck_profile_ready,
            self.controller_ui_ready,
            self.crash_reporting_ready,
        ]
        return round(sum(1 for f in flags if f) / len(flags) * 100, 2)


class SteamLaunchPlanner:
    def checklist(self, readiness: SteamReadiness) -> list[str]:
        items: list[str] = []
        if not readiness.cloud_save_ready:
            items.append("Implement Steam Cloud save sync + conflict resolution")
        if not readiness.achievements_ready:
            items.append("Define and wire achievement events")
        if not readiness.workshop_ready:
            items.append("Add workshop/mod upload and load-order pipeline")
        if not readiness.deck_profile_ready:
            items.append("Create Steam Deck input/profile preset")
        if not readiness.controller_ui_ready:
            items.append("Complete controller-first UI navigation pass")
        if not readiness.crash_reporting_ready:
            items.append("Integrate crash/telemetry reporting")
        return items
