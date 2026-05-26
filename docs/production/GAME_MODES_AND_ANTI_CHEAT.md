# Rookie Quest: Ringmaster — Game Modes and Anti-Cheat Rules

This document defines how roster editing, manager progression, sandbox freedom, and save integrity should work.

The key rule:

> A player should not be able to freely create, delete, or edit wrestlers inside a normal Manager Mode save.

If they can, the management game loses its challenge. Players could create perfect wrestlers, delete difficult contracts, erase injuries, remove morale problems, or bypass scouting and development.

---

## 1. Core Modes

### 1.1 Manager Mode

Manager Mode is the main intended game mode.

The player runs a wrestling company and must deal with the roster, money, staff, sponsors, fatigue, morale, injuries, production problems, and booking consequences.

In Manager Mode, the player **cannot** freely:

- create wrestlers from nothing,
- delete wrestlers from the world,
- directly edit wrestler stats,
- remove injuries manually,
- reset fatigue manually,
- rewrite contracts freely,
- give themselves money,
- remove sponsor penalties,
- erase bad show history.

The player **can**:

- hire wrestlers,
- release wrestlers if contract rules allow it,
- scout new talent,
- negotiate contracts,
- train wrestlers,
- develop popularity/momentum,
- book shows,
- choose winners/finishes,
- manage injuries/fatigue through rest and medical decisions,
- manage morale through booking and contracts,
- improve production through spending,
- accept/reject sponsors,
- take risks with match types.

Manager Mode should feel earned.

---

## 2. Sandbox / Commissioner Mode

Sandbox Mode is for creative freedom.

This is where full roster editing is allowed.

The player can:

- create wrestlers,
- edit wrestler stats,
- delete wrestlers,
- create custom companies,
- create dream rosters,
- edit money,
- edit sponsors,
- set titles,
- create custom staff,
- run fantasy booking without normal restrictions.

Sandbox Mode should be clearly labelled.

Recommended warning:

> Sandbox saves allow editing and may disable achievements/progression validation.

---

## 3. Roster Editor Purpose

The current `roster_management_v2.html` screen should be treated as a **Roster Editor / Sandbox Tool**, not as a normal Manager Mode roster screen.

It is useful for:

- building test rosters,
- creating fictional default data,
- custom saves,
- modding-style workflows,
- sandbox campaigns,
- developer balancing.

It should not be the default Manager Mode roster screen.

Manager Mode should instead have a different screen, such as:

- `roster_office.html`,
- `talent_management.html`,
- `contracts.html`,
- `scouting.html`,
- `training_center.html`.

Those screens should allow management actions, not direct editing.

---

## 4. Manager Mode Roster Actions

Manager Mode should use controlled actions.

### 4.1 Hiring

- Player can view available free agents.
- Player can scout unknown talent.
- Wrestlers have asking prices.
- Wrestlers can reject offers.
- Popular wrestlers demand better contracts.
- Risky/problematic wrestlers may have lower cost but higher backstage risk.

### 4.2 Releasing

- Player can release a wrestler only if contract rules allow it.
- Early release may cost money.
- Releasing popular wrestlers may reduce fan trust.
- Releasing loyal veterans may hurt morale.
- Releasing injured wrestlers may damage reputation.

### 4.3 Training

- Player can assign training focus:
  - in-ring,
  - promo,
  - stamina,
  - safety,
  - charisma,
  - character work.
- Training should be slow.
- Older wrestlers improve slower.
- High fatigue reduces training effectiveness.
- Injuries can be worsened by overtraining.

### 4.4 Development

- Younger wrestlers can improve over seasons.
- Veterans may decline physically but gain experience.
- Good booking increases popularity/momentum.
- Bad booking can damage morale and trust.

### 4.5 Medical / Rest

- Player can rest wrestlers.
- Rest lowers fatigue.
- Medical spend can reduce injury duration.
- Rushing someone back increases risk.

---

## 5. Achievements and Validation

For Steam-style achievements and fair progression, saves should have flags.

Recommended save flags:

```json
{
  "mode": "manager",
  "customRoster": false,
  "editorUsed": false,
  "achievementsEnabled": true,
  "saveIntegrity": "standard"
}
```

If a player uses editor tools, the save should become:

```json
{
  "mode": "sandbox",
  "customRoster": true,
  "editorUsed": true,
  "achievementsEnabled": false,
  "saveIntegrity": "modified"
}
```

This does not punish sandbox players. It just protects Manager Mode progression.

---

## 6. UI Rules

### Manager Mode UI

Do not show buttons like:

- Create Wrestler,
- Delete Wrestler,
- Edit Stats,
- Reset Roster,
- Set Money,
- Clear Injury.

Instead show actions like:

- Offer Contract,
- Release Talent,
- Send to Training,
- Rest Wrestler,
- Medical Review,
- Scout Talent,
- Negotiate.

### Sandbox UI

Show editing tools, but label them clearly:

- Roster Editor,
- Create Wrestler,
- Edit Stats,
- Delete Wrestler,
- Reset Default Roster,
- Import Custom Roster,
- Export Roster.

### Warnings

If the player enters editor tools from a Manager Mode save, show a warning:

> Using editor tools will convert this save to Sandbox Mode and disable Manager Mode achievements/progression validation.

---

## 7. Recommended Game Flow

### Normal Manager Mode

```text
New Game
→ Choose Manager Mode
→ Pick or create promotion identity
→ Receive starting roster / draft roster / hire from initial market
→ Manage contracts, shows, money, morale, and growth
```

### Sandbox Mode

```text
New Game
→ Choose Sandbox Mode
→ Edit roster / company / money / world
→ Book freely
→ Achievements/progression validation disabled
```

### Custom Roster Manager Mode

This can exist, but needs a clear rule.

Option A:

- Custom roster always counts as Sandbox.

Option B:

- Custom roster can be used in Manager Mode, but achievements are limited.

Recommended for first release:

- Custom roster = Sandbox / modified save.

This is simpler and harder to exploit.

---

## 8. Design Principle

Manager Mode is about solving problems.

Sandbox Mode is about creating toys.

Both are valuable, but they should not be mixed without clear save flags.
