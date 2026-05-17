# Professional Design Recommendation (Chosen Direction)

## Final Recommendation
Adopt **Style A: Broadcast Executive** as the primary game UI.

This is the strongest option for a management-heavy wrestling sim because it balances:
- high-density decision making (booking, contracts, finance),
- long-session readability,
- premium sports entertainment tone,
- scalability to Steam + controller-first console UX.

Use the other directions as supporting variants:
- **Style B (Fight Poster Noir):** use for splash screens, PPV branding, event intros.
- **Style C (Modern Sports App):** use as optional accessibility/light theme.

---

## Design System v1 (Implementation Ready)

### 1) Typography
- **Primary UI font:** Inter (fallback: Source Sans 3)
- **Display font:** Bebas Neue (fallback: Teko)
- **Usage rules:**
  - Data tables, forms, labels, and body text must use UI font.
  - Event names, show logos, and hero headers use display font.
  - Minimum body text size:
    - Desktop: 14px
    - Console TV mode: 18px

### 2) Color Tokens
- `bg.base`: `#0F1115`
- `bg.panel`: `#171A21`
- `bg.card`: `#232734`
- `text.primary`: `#E8ECF3`
- `text.secondary`: `#A7B0C0`
- `status.success`: `#37D67A`
- `status.warning`: `#FFB020`
- `status.danger`: `#FF5C5C`
- `status.info`: `#4DA3FF`

### 3) Spacing + Shape
- Grid: 8px baseline.
- Card padding: 16–20px.
- Corners: 10–14px radius.
- Borders: subtle (`#2C3140`) with low-contrast strokes.

### 4) Motion
- Transition duration: 120–180ms.
- Use motion to reinforce state changes (success/fail/alert) only.
- Disable non-essential motion in accessibility mode.

### 5) Core Screens (Priority)
1. Weekly Command Center (inbox, urgent actions, KPIs)
2. Booking Board (segment order + pacing warnings)
3. Roster Intelligence (morale/momentum/contracts)
4. Storyline Planner (heat trajectory + payoff windows)
5. Finance Cockpit (runway + revenue mix)
6. Global Rankings (world domination ladder + market share)

---

## Brand Treatment Rules
- Every promotion gets one accent color token (for chips, chart highlights, and headers).
- Accent color must pass contrast checks against `bg.panel`.
- Never use accent color for dense body copy.

---

## Console Readiness Rules
- Minimum selectable row height: 48px.
- Focus states must be obvious and high contrast.
- Key actions available in <= 3 inputs from screen entry.

---

## Deliverable Decision
Proceed with:
- `style_a_broadcast_executive.svg` as the canonical visual baseline,
- a follow-up implementation of this token system into first playable UI screens.
