from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class GameMode(str, Enum):
    PROMOTER = "promoter"
    GENERAL_MANAGER = "general_manager"
    WRESTLER_CAREER = "wrestler_career"


@dataclass(frozen=True)
class ModeRules:
    can_control_finances: bool
    can_control_storylines: bool
    can_force_match_winners: bool
    can_train_single_wrestler: bool
    uses_hidden_match_outcomes: bool


MODE_RULES: dict[GameMode, ModeRules] = {
    GameMode.PROMOTER: ModeRules(
        can_control_finances=True,
        can_control_storylines=True,
        can_force_match_winners=True,
        can_train_single_wrestler=False,
        uses_hidden_match_outcomes=False,
    ),
    GameMode.GENERAL_MANAGER: ModeRules(
        can_control_finances=False,
        can_control_storylines=False,
        can_force_match_winners=False,
        can_train_single_wrestler=False,
        uses_hidden_match_outcomes=True,
    ),
    GameMode.WRESTLER_CAREER: ModeRules(
        can_control_finances=False,
        can_control_storylines=False,
        can_force_match_winners=False,
        can_train_single_wrestler=True,
        uses_hidden_match_outcomes=True,
    ),
}


def rules_for_mode(mode: GameMode) -> ModeRules:
    return MODE_RULES[mode]
