# Rookie-Quest-Ringmaster

A wrestling manager simulation game inspired by the depth of Football Manager, with a focus on storytelling, booking psychology, backstage politics, and business strategy.

## Vision

Build the definitive pro wrestling management sim where players can:
- run a promotion from indie startup to global powerhouse,
- craft long-term storylines and protect wrestler momentum,
- manage morale, locker room politics, injuries, and contracts,
- balance creative risk with financial sustainability.

## UI Design Direction

Rookie Quest: Ringmaster now has a locked visual direction for the v0.1 prototypes: a premium dark sports-management dashboard with wrestling broadcast atmosphere.

Core visual principles:
- dark navy and charcoal interface foundations,
- metallic gold accents for prestige, headings, trims, and primary actions,
- clean data-first layouts built for long management sessions,
- teal/green for positive movement, amber for warnings, and crimson for danger,
- fictional-by-default presentation with no real wrestling companies, protected talent names, or copyrighted logos.

The current core UI screens being redesigned around this style are:
- `ui/main_menu.html`
- `ui/campaign_dashboard.html`
- `ui/booking_board.html`
- `ui/brand_creator.html`
- `ui/select_brand.html`
- `ui/weekly_planner.html`

See `docs/UI_STYLE_GUIDE.md` for the full style guide.

## Core Design Pillars

1. **Creative Depth**
   - Segment-level show booking (matches, promos, angles, surprises).
   - Long-term arcs with payoff tracking and narrative coherence scoring.
2. **Human Drama**
   - Wrestler personalities, chemistry, ego, discipline, and loyalty.
   - Dynamic locker room factions and mentor/rival relationships.
3. **Sports-Business Strategy**
   - TV rights, sponsorships, merch, touring, and production spend.
   - Data-driven growth with fan segmentation and market heat maps.
4. **Consequences That Matter**
   - Every decision changes momentum, fan trust, morale, and finances.
   - AI promotions evolve and react to player behavior.

## MVP Scope (First Playable)

### Simulation Systems
- **Roster model**: skills, traits, style compatibility, popularity by region.
- **Booking model**: card structure, segment goals, match agenting, finishes.
- **Fan response model**: crowd reaction + broader audience rating.
- **Economy model**: ticket sales, payroll, venue costs, streaming revenue.
- **Health model**: fatigue, injury risk, medical recovery, time off effects.

### Management Systems
- Contracts (exclusive/non-exclusive, downside guarantees, clauses).
- Talent development (training focus, gimmick tweaks, role assignment).
- Backstage events (conflicts, morale swings, discipline choices).
- Scouting & recruiting (regions, schools, free agents, veteran returns).

### Game Loop
1. Weekly planning (budget + strategy).
2. Talent talks and contract decisions.
3. Show booking (major + minor segments).
4. Simulation + post-show report.
5. Long-term analysis (storyline health, brand growth, roster balance).

## Suggested Technical Architecture

- **Engine**: Unity (C#) for rapid UI tooling and simulation at scale.
- **Data layer**: JSON/SQLite hybrid for moddable content + deterministic sim.
- **Simulation core**:
  - deterministic turn resolver,
  - event bus for backstage/world incidents,
  - weighted narrative evaluator.
- **UI**: dashboard-heavy desktop-first UX (tables, filters, timeline views).
- **Testing**:
  - unit tests for formulas and constraints,
  - snapshot tests for generated show reports,
  - Monte Carlo balance tests for economy and injuries.

## Feature Roadmap

### Phase 1 — Prototype (4–6 weeks)
- Build wrestler schema + basic booking card.
- Simulate one show with a post-show grade.
- Add simple finances and morale impacts.

### Phase 2 — Vertical Slice (6–10 weeks)
- Full weekly loop with contracts and injuries.
- AI competitor promotions and talent poaching.
- Regional popularity simulation and attendance forecasting.

### Phase 3 — Early Access Candidate
- Multiple show brands, championships, and PPV cadence.
- Storyline planner with arc milestones and payoff recommendations.
- Mod support for rosters, companies, events, belts, and arenas.

## Differentiators (How to Beat “Football Manager for Wrestling” Expectations)

- **Booking Psychology Engine**: understands overexposure, rematch fatigue, and payoff timing.
- **Promo & Character System**: voice/style archetypes influence segment outcomes.
- **Wrestler Safety & Style Logic**: risky styles pop ratings but increase burnout/injury.
- **History-Driven Worlds**: records and callbacks influence fan memory and reactions.
- **Creative Assistant Tools**: optional AI-generated feud suggestions and card balancing hints.

## KPIs for Balancing

- Match quality variance by card position and crowd exhaustion.
- Storyline retention (weeks sustained before fan drop-off).
- Roster morale volatility and disciplinary event frequency.
- Revenue mix health (gate vs media vs merch).
- Injury incidence rate per 100 matches by style/risk profile.

## Next 10 Implementation Tasks

1. Define canonical wrestler data schema.
2. Implement deterministic random seed handling.
3. Build segment scoring formula v1.
4. Create weekly budget + cashflow simulation.
5. Add contract expiration and negotiation flow.
6. Build basic roster management UI.
7. Implement injury/fatigue progression system.
8. Add simple AI booking for rival promotions.
9. Generate post-show analytics report.
10. Add save/load with versioned schema migration.

## Development Principles

- Keep formulas transparent and inspectable by players.
- Prefer data-driven tuning over hardcoded behavior.
- Support modding early to grow community content.
- Separate “simulation truth” from “presentation text.”

## Contributing

Open an issue with one of these tags:
- `sim-balance`
- `ai-booking`
- `ui-ux`
- `economy`
- `modding`

Include reproduction steps, expected outcome, and balancing concerns where relevant.

## Detailed Mega Backlog

For a massive checklist of features and production tasks, see **`GAME_FEATURES_AND_BACKLOG.md`**.

## Steam + Console Feature Shortlist

For a market-focused, launch-ready feature list, see **`docs/FEATURES_FOR_STEAM_AND_CONSOLES.md`**.

## Intro Loading Video Prototype

A prototype loading intro video and storyboard are available here:
- `assets/video/loading_intro.mp4`
- `assets/video/intro_loading_storyboard.md`

## Starter Implementation Assets

To turn planning into build-ready execution, use:
- `data/schemas/wrestler.schema.json` (canonical wrestler schema v1)
- `docs/production/FIRST_12_WEEKS_PLAN.md` (execution plan)
- `scripts/generate_loading_intro.sh` (intro video prototype generator)

## Data Validation Quickstart

Validate wrestler sample data against the canonical schema:

```bash
python tools/validate_wrestlers.py
```

If needed, install dependency:

```bash
pip install jsonschema
```

## Framework Prototype (Now Implemented)

A first playable framework has been added in Python under `src/ringmaster/`:
- `models.py` — core domain objects (`Wrestler`, `Segment`, `MatchOutcome`)
- `sim.py` — deterministic seed-based segment simulation engine
- `cli.py` — runnable prototype that simulates a main event and prints results

### Run Prototype

```bash
python -m ringmaster.cli
```

### Run Tests

```bash
python -m pytest -q
```

> Tip: install locally with `pip install -e .` to run commands without setting `PYTHONPATH`.

## New Framework Systems

The prototype now includes:
- `src/ringmaster/weekly.py` — weekly loop orchestration and report generation
- `src/ringmaster/finance.py` — weekly revenue/cost projection
- `src/ringmaster/contracts.py` — basic contract model with expiration alerts
- `src/ringmaster/storylines.py` — feud heat progression engine
- `src/ringmaster/morale.py` — wrestler morale change model from show outcomes

## Global Universe Framework

The framework now supports global competition setup:
- country database (`data/world/countries.json`)
- auto-generated local brand per country
- multi-show setup per brand (weekly + special)
- custom player brand creation for "start your own company" mode

## World Domination Progression

New campaign tracking system:
- `src/ringmaster/campaign.py` computes weekly world rank, market share, and domination score for the player brand.
- Supports long-term progression toward global #1 status.

## Final Design Decision

The project should proceed with the premium dark **Rookie Quest: Ringmaster** design direction captured in `docs/UI_STYLE_GUIDE.md`.

## Save/Load Prototype

A versioned savegame module is now included at `src/ringmaster/savegame.py` to persist campaign progress (player brand, week, brands, and latest campaign snapshot).

## Intro + Start Screen Prototype

Added a playable intro/start concept:
- `assets/branding/ringmaster_logo.svg`
- `ui/intro_screen.html`
- `docs/design/INTRO_VIDEO_AND_START_SCREEN.md`

## Fictional Content Policy

To avoid licensing/trademark issues, all promotions, talent names, logos, and storylines in this project are fictional-by-default.
The generator now uses fictional naming (`src/ringmaster/fictional.py`) instead of real-world promotion naming conventions.

## Show/PPV Cadence Balancing

New prototype modules add gameplay rules for promotion setup and scheduling:
- `src/ringmaster/promotion.py` for starting budget, weekly show count, monthly PPV count, expansion affordability checks, and overbooking penalties.
- `src/ringmaster/ppv.py` for customizable monthly PPV event scheduling with theme support.

Design intent: running too many weekly shows or too many PPVs introduces trust/quality penalties to enforce strategic balance.

## Entrance Production and Budgeting

New systems now support lights/lasers/pyro investment and wrestler-specific entrance budgeting:
- `src/ringmaster/production.py` includes production inventory upgrades and cost scaling.
- PPV/show entrance budget can be split per wrestler and evaluated against wrestler minimum demands.
- Underfunding entrances creates morale penalties; over-delivery can improve crowd bonus.

## Weekly Planner Prototype

Added `ui/weekly_planner.html` for interactive planning of show cadence, PPV schedule, and entrance budget pressure with immediate balance feedback.
