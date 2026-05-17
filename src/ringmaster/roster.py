from __future__ import annotations

from dataclasses import dataclass, field

from .development import Prospect


@dataclass
class MainRoster:
    wrestlers: list[str] = field(default_factory=list)


@dataclass
class DevelopmentRoster:
    prospects: list[Prospect] = field(default_factory=list)


@dataclass(frozen=True)
class GraduationResult:
    promoted_ids: list[str]
    stayed_ids: list[str]
    released_ids: list[str]


class RosterPipeline:
    def graduate_prospects(
        self,
        dev_roster: DevelopmentRoster,
        main_roster: MainRoster,
        readiness_threshold: int = 70,
        loyalty_threshold: int = 45,
    ) -> GraduationResult:
        promoted: list[str] = []
        stayed: list[str] = []
        released: list[str] = []

        remaining: list[Prospect] = []
        for p in dev_roster.prospects:
            if p.readiness >= readiness_threshold and p.loyalty >= loyalty_threshold:
                if p.wrestler_id not in main_roster.wrestlers:
                    main_roster.wrestlers.append(p.wrestler_id)
                promoted.append(p.wrestler_id)
            elif p.loyalty < 25 and p.readiness >= readiness_threshold:
                # unhappy ready talent may leave for another promotion
                released.append(p.wrestler_id)
            else:
                stayed.append(p.wrestler_id)
                remaining.append(p)

        dev_roster.prospects = remaining
        return GraduationResult(promoted, stayed, released)
