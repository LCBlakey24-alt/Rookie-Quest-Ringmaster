# Full Diagnostic Report (May 17, 2026)

## Scope
This report covers repository health checks for the current prototype after merge.

## What Was Checked
1. Unit test suite execution.
2. CLI smoke test.
3. Data schema validation script execution.
4. Packaging/dependency declaration review.

## Results

### 1) Unit Tests
- **Status:** PASS
- **Command:** `python -m pytest -q`
- **Output summary:** `43 passed in 0.32s`
- **Interpretation:** Core prototype logic currently has good regression coverage for included systems.

### 2) CLI Smoke Test
- **Status:** FAIL (packaging/runtime issue)
- **Command:** `python -m ringmaster.cli`
- **Error:** `ModuleNotFoundError: No module named 'ringmaster'`
- **Root cause:** The project uses `src/` layout and tests inject `pythonpath = ["src"]`, but direct CLI module execution without install or `PYTHONPATH=src` fails.
- **Impact:** New contributors can think the CLI is broken even though package code itself is valid.

### 3) Wrestler Schema Validator Tool
- **Status:** FAIL (missing dependency)
- **Command:** `python tools/validate_wrestlers.py`
- **Error:** `jsonschema is not installed. Install with: pip install jsonschema`
- **Root cause:** `jsonschema` is required by tooling but not declared in project dependencies.
- **Impact:** Validation workflow does not work out-of-the-box.

### 4) Packaging and Dependency Review
- **File reviewed:** `pyproject.toml`
- **Finding A:** `dependencies = []` despite `tools/validate_wrestlers.py` depending on `jsonschema`.
- **Finding B:** Project script entry point exists (`ringmaster = "ringmaster.cli:main"`) but README should clarify install/run flow for `src/` layout.
- **Risk level:** Medium (developer onboarding friction, false-positive breakage reports).

## Bug/Issue List (Actionable)

### High Priority
1. Add `jsonschema` to project dependencies (or optional `dev` extra with documented install command).
2. Add a quickstart run path for CLI in README:
   - `pip install -e .` then `ringmaster`
   - or `PYTHONPATH=src python -m ringmaster.cli`

### Medium Priority
3. Add CI command that runs `tools/validate_wrestlers.py` so schema tooling is continuously verified.
4. Add a one-command `make test`/`scripts/check.sh` to reduce setup ambiguity.

### Low Priority
5. Add a startup self-check command in CLI (`ringmaster doctor`) to verify data files and optional dependencies.

## Feature Gaps Before "Game Ready"

## A) Must-Have Gameplay Systems
- End-to-end playable loop connecting mode select -> booking -> sim -> persistence -> progression consequences.
- Complete contract system (clauses, non-compete, buyout, promises, disputes).
- Full injury/recovery/safety model connected to booking risk and medical staffing.
- Robust AI promotions that book, hire, react, and create market pressure.
- Championship/division/rankings logic with meaningful contender progression.

## B) Must-Have UX/Player Clarity
- Unified dashboard for weekly priorities with "why" explanations for score/morale/finance changes.
- Card builder usability polish (diffs, undo/redo, quick templates, warnings).
- Onboarding/tutorial path for first 3–4 in-game weeks.
- Accessibility baseline (font scaling, contrast-safe palettes, keyboard/controller paths).

## C) Must-Have Persistence/Mod Safety
- Versioned saves + migration handling.
- Mod load order + conflict diagnostics + safe-mode recovery.
- Deterministic replay snapshots for bug reproduction.

## D) Must-Have Production/Release Readiness
- CI pipeline with lint/tests/tooling checks.
- Crash logging and error reporting strategy.
- Performance targets for large universes.
- Store/demo launch checklist and support playbook.

## E) Steam/Platform Readiness
- Cloud save sync and conflict resolution.
- Achievement/event wiring.
- Controller-first navigation + Steam Deck profile pass.
- Workshop publishing pipeline.

## Recommended Build Order (Practical)
1. Fix packaging/onboarding blockers (CLI run path, dependencies, docs).
2. Connect one complete vertical slice loop (book -> simulate -> consequences -> save/load).
3. Implement AI competitor pressure and economy tuning.
4. Build explainability and onboarding UX.
5. Harden mod/save safety + platform launch requirements.
