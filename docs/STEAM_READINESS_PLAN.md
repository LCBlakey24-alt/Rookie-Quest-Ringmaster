# Steam Readiness Plan

## Goal
Ship a stable, stream-friendly management game build on Steam with reliable saves, controller support, and mod/community hooks.

## Required Launch Pillars
1. Steam Cloud save support with conflict handling.
2. Achievements mapped to campaign milestones.
3. Workshop/mod uploader and safe mod load-order.
4. Steam Deck profile and controls.
5. Controller-first UI navigation.
6. Crash + telemetry reporting.

## Prototype Support Added
- `src/ringmaster/steam.py`
  - readiness state model
  - completion percentage calculation
  - launch checklist generator

## Recommended Next Milestones
- Milestone A: Save/Cloud compatibility pass
- Milestone B: Input/navigation pass for controller + Deck
- Milestone C: Achievements and telemetry integration
- Milestone D: Workshop alpha for fictional roster mods
