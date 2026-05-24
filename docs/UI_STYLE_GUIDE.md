# Rookie Quest: Ringmaster — UI Style Guide

## Design Direction

Rookie Quest: Ringmaster should look and feel like a premium wrestling management simulation: part executive control room, part sports-broadcast dashboard, part arena production desk.

The visual style should be:
- dark navy and charcoal as the base,
- metallic gold for prestige, headings, trims, and primary actions,
- off-white text for readability,
- muted grey-blue supporting text,
- teal/green for positive movement,
- amber for caution,
- crimson for danger, injuries, budget warnings, and risk.

The game should not look like a bright mobile app or a generic admin dashboard. It should feel dramatic, readable, premium, and built for long management sessions.

## Core Palette

| Token | Hex | Use |
| --- | --- | --- |
| Deep Navy | `#0B1324` | Main background and arena atmosphere |
| Charcoal | `#11151C` | Secondary background |
| Panel Dark | `#171A21` | Main panels/cards |
| Card Dark | `#232734` | Nested cards, rows, controls |
| Border Grey | `#2C3140` | Panel borders and dividers |
| Gold Accent | `#D4AF37` | Primary actions, headings, trim, premium highlights |
| Gold Dark | `#9B7A20` | Gold gradients and depth |
| Off White | `#F2F2F2` | Primary text |
| Muted Text | `#A7B0C0` | Labels, helper text, subtitles |
| Muted Teal | `#19A7A5` | Charts, info, positive stats |
| Success Green | `#37D67A` | Positive changes and safe status |
| Warning Amber | `#FFB020` | Warnings and pressure states |
| Danger Crimson | `#C62828` | Injuries, risks, budget trouble |

## Typography

Use `Inter, Arial, sans-serif` for prototype UI text.

Headings should be bold, uppercase, and slightly letter-spaced. The main logo/title treatment should feel like a premium wrestling event logo: heavy, metallic, gold/silver where possible, and dramatic without sacrificing readability.

## Layout Rules

Every major screen should support decision-making first.

Preferred layout pattern:
- Top command/header bar: week, brand, current mode, and main actions.
- Main working area: the screen's primary decision tool.
- Right or secondary panel: context, warnings, recommendations, or summaries.
- KPI cards: visible at a glance for cash, popularity, morale, fan trust, rank, or show timing.

Avoid clutter for the sake of drama. The game can be atmospheric, but the data must stay clear.

## Component Rules

Panels:
- Dark panel background.
- 1px steel/grey border.
- Rounded corners around 14–16px.
- Gold trim only on important or premium panels.

Buttons:
- Primary buttons use gold gradients.
- Secondary buttons use dark cards with grey borders.
- Danger buttons use crimson.
- Do not overuse bright teal/green as primary actions.

Tables:
- Use dark row cards rather than plain spreadsheet lines.
- Highlight the first column or key identity field.
- Keep numeric columns aligned and readable.

Alerts:
- Green = safe/positive.
- Amber = caution.
- Crimson = danger/problem.
- Gold = important story/premium highlight.

## Current Core Screens

The first redesigned prototype screens are:
- `ui/main_menu.html`
- `ui/campaign_dashboard.html`
- `ui/booking_board.html`
- `ui/brand_creator.html`
- `ui/select_brand.html`
- `ui/weekly_planner.html`

These screens define the v0.1 visual direction. Other prototype screens should be updated later to match this style rather than inventing new visual systems.

## Design Principles

1. Clear data-first layout.
2. Premium wrestling presentation.
3. Readable at a glance.
4. Built for long-session management gameplay.
5. Fictional by default: no real wrestling companies, logos, protected talent names, or copyrighted wrestling references in default content.
6. Every screen should help the player make a decision.
