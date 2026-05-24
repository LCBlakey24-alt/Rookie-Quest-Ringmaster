"""Core package for Rookie Quest: Ringmaster."""

from .booking import BookingBoard, BookingSegment
from .campaign import CampaignEngine, CampaignSnapshot
from .career import CareerDashboard, CareerDashboardService
from .career_rpg import (
    BookingOpportunity,
    ContractType,
    LifestyleChoiceResult,
    WrestlerCareerRPG,
    WrestlerCareerState,
)
from .development import DevelopmentReport, DevelopmentShowPlan, DevelopmentSystem, Prospect
from .dialogue import DialogueContext, DialogueEngine, DialogueOutcome
from .events import BackstageEvent, EventEngine
from .fictional import FictionalBrandSeed, fictional_brand_name, fictional_wrestler_name
from .finance import FinanceEngine, FinanceSnapshot
from .game import BookingSlot, WeeklyShow
from .models import MatchOutcome, Segment, Wrestler
from .modes import GameMode, ModeRules, rules_for_mode
from .morale import MoraleEngine, MoraleState
from .ppv import PPVEvent, PPVScheduler
from .production import (
    EntranceAssignment,
    EntranceBudgetManager,
    EntranceBudgetReport,
    EntranceDemand,
    ProductionInventory,
    ProductionPlanner,
)
from .promotion import PromotionBalanceReport, PromotionPlanner, PromotionProfile
from .roster import DevelopmentRoster, GraduationResult, MainRoster, RosterPipeline
from .runtime import CareerRuntimeService, RuntimeWeekResult
from .savegame import SaveGame, create_save, load_from_file, save_to_file
from .show_assignment import AssignmentReport, ShowAssignment, ShowAssignmentEngine
from .sim import SegmentResult, SimulationEngine
from .staff import RosterNeed, StaffMember, StaffOffice, StaffSynergyReport
from .steam import SteamLaunchPlanner, SteamReadiness
from .storylines import Storyline, StorylineEngine
from .talent import TalentPool, TalentProfile, TalentTrainer
from .universe import create_custom_brand, generate_universe
from .weekly import WeeklyLoop, WeeklyReport
from .world import Brand, Country, ShowTemplate, Universe

__all__ = [
    "AssignmentReport",
    "BackstageEvent",
    "BookingBoard",
    "BookingOpportunity",
    "BookingSegment",
    "BookingSlot",
    "Brand",
    "CampaignEngine",
    "CampaignSnapshot",
    "CareerDashboard",
    "CareerDashboardService",
    "CareerRuntimeService",
    "ContractType",
    "Country",
    "DevelopmentReport",
    "DevelopmentRoster",
    "DevelopmentShowPlan",
    "DevelopmentSystem",
    "DialogueContext",
    "DialogueEngine",
    "DialogueOutcome",
    "EntranceAssignment",
    "EntranceBudgetManager",
    "EntranceBudgetReport",
    "EntranceDemand",
    "EventEngine",
    "FictionalBrandSeed",
    "FinanceEngine",
    "FinanceSnapshot",
    "GameMode",
    "GraduationResult",
    "LifestyleChoiceResult",
    "MainRoster",
    "MatchOutcome",
    "ModeRules",
    "MoraleEngine",
    "MoraleState",
    "PPVEvent",
    "PPVScheduler",
    "ProductionInventory",
    "ProductionPlanner",
    "PromotionBalanceReport",
    "PromotionPlanner",
    "PromotionProfile",
    "Prospect",
    "RosterNeed",
    "RosterPipeline",
    "RuntimeWeekResult",
    "SaveGame",
    "Segment",
    "SegmentResult",
    "ShowAssignment",
    "ShowAssignmentEngine",
    "ShowTemplate",
    "SimulationEngine",
    "StaffMember",
    "StaffOffice",
    "StaffSynergyReport",
    "SteamLaunchPlanner",
    "SteamReadiness",
    "Storyline",
    "StorylineEngine",
    "TalentPool",
    "TalentProfile",
    "TalentTrainer",
    "Universe",
    "WeeklyLoop",
    "WeeklyReport",
    "WeeklyShow",
    "Wrestler",
    "WrestlerCareerRPG",
    "WrestlerCareerState",
    "create_custom_brand",
    "create_save",
    "fictional_brand_name",
    "fictional_wrestler_name",
    "generate_universe",
    "load_from_file",
    "rules_for_mode",
    "save_to_file",
]
