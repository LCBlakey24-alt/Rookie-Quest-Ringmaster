# Rookie Quest: Ringmaster — Steam Ready Master To-Do List

This is the main production checklist for turning **Rookie Quest: Ringmaster** from an HTML prototype / simulation experiment into a Steam-ready commercial game.

The target is not just "it launches". The target is:

- playable for long sessions,
- stable across saves and updates,
- clear enough for new players,
- deep enough for wrestling-management fans,
- legal and fictional by default,
- marketable on Steam,
- expandable after release without yearly sequel resets.

---

## 0. Current Reality Check

### Current state

The project currently has a strong prototype direction:

- dark premium wrestling-management UI style,
- campaign dashboard,
- booking board,
- pre-show intel,
- broadcast team selection,
- referee crew selection,
- production/sponsor setup,
- post-show night report,
- weekly fallout,
- roster momentum page,
- fictional-by-default design direction.

### Not Steam-ready yet

The project is still far from Steam-ready because it needs:

- a real game runtime/engine decision,
- persistent save system outside browser localStorage,
- proper data models,
- a reliable simulation core,
- actual campaign progression,
- content volume,
- settings/accessibility,
- QA testing,
- packaging/build pipeline,
- Steamworks integration,
- store assets/trailer/demo/marketing plan.

---

## 1. Product Definition

### 1.1 Lock the game identity

- [ ] Confirm final title: **Rookie Quest: Ringmaster**.
- [ ] Confirm subtitle/tagline.
- [ ] Confirm genre label: wrestling promoter / wrestling management simulation.
- [ ] Confirm core fantasy: "Run a wrestling company from small shows to global domination."
- [ ] Confirm no real wrestling companies, wrestlers, logos, protected catchphrases, arenas, or copyrighted storylines in default content.
- [ ] Confirm tone: serious management depth with chaotic wrestling flavour.
- [ ] Confirm business promise: one expandable game, no yearly reset, no pay-to-win.

### 1.2 Define launch version

Decide whether Steam launch is:

- [ ] Early Access launch,
- [ ] full 1.0 launch,
- [ ] free demo first,
- [ ] paid Early Access with roadmap.

Recommended path:

1. Internal prototype.
2. Closed playtest.
3. Public Steam demo.
4. Early Access.
5. Full 1.0.

### 1.3 Define minimum Steam product promise

The store page must only promise things that are actually in or confidently planned.

- [ ] Write one-paragraph game pitch.
- [ ] Write feature bullets.
- [ ] Write what players can do in the current build.
- [ ] Write what is planned later.
- [ ] Avoid overpromising career mode, story mode, consoles, online sharing, or AI features until real.

---

## 2. Legal / IP Safety

### 2.1 Fictional wrestling universe

- [ ] Replace all real-world placeholder inspirations with original fictional names.
- [ ] Maintain a forbidden-content checklist:
  - real wrestler names,
  - real promotion names,
  - real faction names,
  - real title belt names,
  - real event names,
  - real logos,
  - copyrighted catchphrases,
  - recognisable likenesses.
- [ ] Add fictional name generator for:
  - wrestlers,
  - promotions,
  - shows,
  - venues,
  - belts,
  - sponsors,
  - broadcasters,
  - wrestling schools.
- [ ] Add a content linter/checklist before release.

### 2.2 Brand protection

- [ ] Check trademark availability for **Rookie Quest: Ringmaster**.
- [ ] Check Steam search for similar names.
- [ ] Check domain/social availability.
- [ ] Confirm whether **Rookie Quest** is used consistently as publisher/brand.
- [ ] Decide whether game title displays as:
  - Rookie Quest: Ringmaster,
  - Rookie Quest Ringmaster,
  - Ringmaster: A Rookie Quest Game.

### 2.3 Licences and dependencies

- [ ] List every library/package used.
- [ ] Confirm licence for every dependency.
- [ ] Remove or replace anything not commercially safe.
- [ ] Add `THIRD_PARTY_NOTICES.md`.
- [ ] Add open-source licence documentation if needed.
- [ ] Confirm all music/SFX/fonts/art are commercial-use safe.

### 2.4 AI-generated content policy

- [ ] Track which assets are AI-generated.
- [ ] Do not use AI-generated likenesses of real wrestlers.
- [ ] Ensure all default content is fictional.
- [ ] Add internal rule: AI can assist drafting, but final published assets/content must be reviewed.

---

## 3. Technical Foundation

### 3.1 Choose final engine/runtime

Current HTML prototypes are useful, but Steam needs a packaged desktop game.

Options:

- [ ] Godot desktop app.
- [ ] Unity desktop app.
- [ ] Electron/Tauri app wrapping web UI.
- [ ] Custom Python app with UI framework.
- [ ] Web app converted to desktop package.

Recommended practical route for current project:

- Short term: continue HTML prototype to refine systems.
- Production route: consider **Godot** or **Tauri/Electron**.
- If management UI remains web-like, Tauri/Electron may be fastest.
- If later adding richer visuals/animated scenes, Godot/Unity may be stronger.

Decision needed:

- [ ] Pick the actual Steam build tech stack.
- [ ] Document why.
- [ ] Create migration plan from prototype pages to production app.

### 3.2 Code architecture

- [ ] Separate UI from simulation logic.
- [ ] Move formulas out of HTML files.
- [ ] Create `/src/simulation/` for core rules.
- [ ] Create `/src/data/` for data loading.
- [ ] Create `/src/ui/` for presentation.
- [ ] Create `/src/save/` for save/load.
- [ ] Create `/src/steam/` for Steam integrations.
- [ ] Create `/tests/` for formula and save tests.

### 3.3 Data-driven design

Every major system should be data-driven.

- [ ] Wrestlers stored in JSON/SQLite.
- [ ] Promotions stored in JSON/SQLite.
- [ ] Staff stored in data files.
- [ ] Sponsors stored in data files.
- [ ] Equipment stored in data files.
- [ ] Venues stored in data files.
- [ ] Event types stored in data files.
- [ ] Storyline templates stored in data files.
- [ ] Achievements stored in data files.

### 3.4 Save system

- [ ] Replace browser localStorage with versioned save files.
- [ ] Add manual save.
- [ ] Add autosave.
- [ ] Add save slots.
- [ ] Add save preview info:
  - promotion name,
  - date/week,
  - cash,
  - rank,
  - last show rating.
- [ ] Add save migration support.
- [ ] Add corrupt-save fallback.
- [ ] Add backup saves.
- [ ] Add save export/import for debugging.
- [ ] Test loading saves after updates.

### 3.5 Deterministic simulation

- [ ] Add campaign seed.
- [ ] Add show seed.
- [ ] Add segment seed.
- [ ] Ensure repeated simulations can be reproduced for debugging.
- [ ] Store random events in the save file.
- [ ] Log major decisions and generated outcomes.

---

## 4. Core Game Loop

The minimum satisfying loop:

1. Review dashboard.
2. Check roster morale/momentum.
3. Review pre-show intel.
4. Plan card.
5. Assign staff/referee/production.
6. Run show.
7. Read night report.
8. Apply fallout.
9. Advance week.
10. Repeat.

### 4.1 Dashboard

- [ ] Current week/date.
- [ ] Cash.
- [ ] Popularity.
- [ ] Fan trust.
- [ ] Morale.
- [ ] Story clarity.
- [ ] Momentum movers.
- [ ] Upcoming show.
- [ ] Warnings.
- [ ] Last show summary.
- [ ] This week's fallout.
- [ ] Sponsor obligations.
- [ ] Production risk.
- [ ] Contract warnings.
- [ ] Injury warnings.
- [ ] Fatigue warnings.

### 4.2 Weekly planning

- [ ] Choose show schedule.
- [ ] Choose venue.
- [ ] Choose ticket pricing.
- [ ] Choose production budget.
- [ ] Choose marketing spend.
- [ ] Choose sponsor package.
- [ ] Choose staffing level.
- [ ] Review estimated cost/revenue.
- [ ] Review overbooking risk.
- [ ] Review fatigue pressure.

### 4.3 Booking board

- [ ] Add/edit/remove segments.
- [ ] Reorder segments.
- [ ] Set segment type:
  - match,
  - promo,
  - angle,
  - video package,
  - interview,
  - contract signing,
  - sponsor segment,
  - surprise return,
  - open challenge,
  - backstage attack.
- [ ] Set participants.
- [ ] Set winner/finish.
- [ ] Set match type.
- [ ] Set title/non-title.
- [ ] Set storyline link.
- [ ] Set segment goal.
- [ ] Set time allocation.
- [ ] Show total runtime.
- [ ] Show crowd pacing risk.
- [ ] Show sponsor obligations.
- [ ] Show hard-out/overrun warning.
- [ ] Show fatigue risk.
- [ ] Show duplicate/rematch warning.
- [ ] Save card.
- [ ] Run show.

### 4.4 Post-show report

- [ ] Overall show score.
- [ ] Segment-by-segment scores.
- [ ] Crowd mood.
- [ ] Wrestler performance notes.
- [ ] Referee incidents.
- [ ] Announcer/commentary review.
- [ ] Production review.
- [ ] Sponsor review.
- [ ] Equipment incidents.
- [ ] Timing/overrun report.
- [ ] Financial report.
- [ ] Roster momentum changes.
- [ ] Injury/fatigue changes.
- [ ] Storyline heat changes.
- [ ] Company fallout.
- [ ] Save report to history.

---

## 5. Simulation Systems

### 5.1 Wrestler model

Each wrestler needs:

- [ ] Name.
- [ ] Age.
- [ ] Gender/presentation category.
- [ ] Nationality/home region.
- [ ] Role:
  - main event,
  - upper card,
  - mid card,
  - opener,
  - prospect,
  - veteran,
  - enhancement talent.
- [ ] Alignment:
  - face,
  - heel,
  - tweener.
- [ ] Style:
  - powerhouse,
  - technical,
  - brawler,
  - high flyer,
  - showbiz entertainer,
  - hardcore,
  - comedy,
  - striker,
  - submission specialist.
- [ ] Popularity.
- [ ] Momentum.
- [ ] Morale.
- [ ] Fatigue.
- [ ] Injury status.
- [ ] Contract status.
- [ ] Personality traits.
- [ ] Preferred match types.
- [ ] Preferred announcer style.
- [ ] Promo skill.
- [ ] In-ring skill.
- [ ] Safety skill.
- [ ] Stamina.
- [ ] Charisma.
- [ ] Star power.
- [ ] Backstage influence.
- [ ] Ego.
- [ ] Loyalty.
- [ ] Discipline.

### 5.2 Match scoring

- [ ] Base score from wrestler skill.
- [ ] Style compatibility.
- [ ] Popularity bonus.
- [ ] Momentum bonus.
- [ ] Storyline heat bonus.
- [ ] Match type suitability.
- [ ] Time allocation suitability.
- [ ] Fatigue penalty.
- [ ] Injury penalty.
- [ ] Chemistry bonus/penalty.
- [ ] Referee effect.
- [ ] Production/camera effect.
- [ ] Crowd pacing effect.
- [ ] Finish quality effect.
- [ ] Repetition/rematch fatigue penalty.

### 5.3 Promo/angle scoring

- [ ] Promo skill.
- [ ] Charisma.
- [ ] Story relevance.
- [ ] Segment placement.
- [ ] Crowd energy.
- [ ] Commentary support.
- [ ] Production quality.
- [ ] Sponsor intrusion penalty.
- [ ] Overexposure penalty.
- [ ] Clear next-step bonus.

### 5.4 Storyline system

- [ ] Create feud/storyline.
- [ ] Assign wrestlers.
- [ ] Set story type:
  - title chase,
  - betrayal,
  - revenge,
  - mentor/student,
  - faction war,
  - underdog rise,
  - monster push,
  - retirement arc,
  - comedy rivalry,
  - tournament story.
- [ ] Track heat.
- [ ] Track clarity.
- [ ] Track fatigue.
- [ ] Track payoff expectation.
- [ ] Track weeks active.
- [ ] Warn when story drags.
- [ ] Warn when payoff is overdue.
- [ ] Boost when callbacks land.
- [ ] Penalise confusing booking.

### 5.5 Roster momentum

- [ ] Momentum states:
  - Cold,
  - Stable,
  - Rising,
  - Hot,
  - Red Hot.
- [ ] Momentum affected by:
  - match score,
  - promo score,
  - win/loss,
  - title win/loss,
  - crowd reaction,
  - ignored fan demand,
  - pre-show intel response,
  - bad referee call,
  - announcer mismatch,
  - injury,
  - overexposure,
  - being left off shows.
- [ ] Add momentum history graph.
- [ ] Add notes per wrestler.
- [ ] Add "push recommendation" system.

### 5.6 Morale/backstage system

- [ ] Morale affected by wins/losses.
- [ ] Morale affected by being booked/ignored.
- [ ] Morale affected by late changes.
- [ ] Morale affected by title decisions.
- [ ] Morale affected by bad referee calls.
- [ ] Morale affected by dangerous equipment.
- [ ] Morale affected by contract disputes.
- [ ] Add backstage incidents.
- [ ] Add personality conflicts.
- [ ] Add mentor relationships.
- [ ] Add factions/cliques.
- [ ] Add discipline system.

### 5.7 Referee system

- [ ] Referee stats:
  - control,
  - accuracy,
  - toughness,
  - drama,
  - bias,
  - experience,
  - consistency.
- [ ] Ref can improve finish credibility.
- [ ] Ref can miss rope break.
- [ ] Ref can count too slow/fast.
- [ ] Ref can call wrong winner.
- [ ] Ref can get bumped.
- [ ] Ref can get injured.
- [ ] Ref can lose locker-room trust.
- [ ] Ref incidents affect fan trust/story clarity/morale.
- [ ] Add backup referee logic.

### 5.8 Broadcast team system

- [ ] Ring announcer stats:
  - hype,
  - clarity,
  - professionalism,
  - showmanship,
  - name accuracy.
- [ ] Commentator stats:
  - knowledge,
  - focus,
  - chemistry,
  - story clarity,
  - excitement,
  - professionalism.
- [ ] Wrestlers have announcer style preferences.
- [ ] Bad announcing annoys talent.
- [ ] Commentary improves/weakens story clarity.
- [ ] Commentary can go off-topic.
- [ ] Commentary can save weak segments.
- [ ] Announcer/commentator contracts.

### 5.9 Production system

- [ ] Production crew stats:
  - camera quality,
  - timing discipline,
  - director skill,
  - ad-break control,
  - chaos risk.
- [ ] Production can miss important shots.
- [ ] Production can improve entrances.
- [ ] Production can botch replays.
- [ ] Production can cut away at wrong moment.
- [ ] Production can save a messy segment with good coverage.
- [ ] Production costs affect finances.

### 5.10 Sponsor system

- [ ] Sponsor packages.
- [ ] Sponsor money.
- [ ] Required mentions.
- [ ] Required branded segment.
- [ ] Sponsor happiness.
- [ ] Sponsor fines.
- [ ] Sponsor pressure.
- [ ] Sponsor can improve revenue but hurt show flow.
- [ ] Sponsor can demand a wrestler/segment.
- [ ] Sponsor can pull funding after bad PR.

### 5.11 Timing/overrun system

- [ ] Show target runtime.
- [ ] Hard-out rules.
- [ ] Overrun warnings.
- [ ] Fine if show overruns.
- [ ] Forced cut-short decision.
- [ ] Player chooses which segment/match to shorten.
- [ ] Shortened match affects wrestlers/morale/story payoff.
- [ ] Going over time affects sponsors/broadcasters.
- [ ] Streaming slots more flexible than TV.

### 5.12 Equipment system

- [ ] Ring quality.
- [ ] Rope quality.
- [ ] Barricade quality.
- [ ] Lighting quality.
- [ ] Stage quality.
- [ ] Pyro quality.
- [ ] Screen/LED quality.
- [ ] Audio reliability.
- [ ] Equipment affects:
  - safety,
  - visuals,
  - crowd immersion,
  - injury risk,
  - production quality,
  - repair costs.

---

## 6. Economy / Business Systems

### 6.1 Revenue

- [ ] Ticket sales.
- [ ] Merchandise.
- [ ] Sponsors.
- [ ] Broadcast deals.
- [ ] Streaming subscriptions.
- [ ] PPV buys.
- [ ] Licensing.
- [ ] International touring.

### 6.2 Costs

- [ ] Talent wages.
- [ ] Staff wages.
- [ ] Venue rental.
- [ ] Production crew.
- [ ] Equipment setup.
- [ ] Travel.
- [ ] Marketing.
- [ ] Insurance/medical.
- [ ] Sponsor penalties.
- [ ] Overrun fines.
- [ ] Repairs.

### 6.3 Contracts

- [ ] Wrestler contracts.
- [ ] Staff contracts.
- [ ] Referee contracts.
- [ ] Sponsor contracts.
- [ ] Broadcast deals.
- [ ] Venue deals.
- [ ] Contract expiration warnings.
- [ ] Negotiation minigame/lightweight flow.
- [ ] Exclusive/non-exclusive deals.
- [ ] Release clauses.
- [ ] Morale impact of contract disputes.

### 6.4 Company progression

- [ ] Local indie.
- [ ] Regional company.
- [ ] National brand.
- [ ] International brand.
- [ ] Global powerhouse.
- [ ] Company rank.
- [ ] Market share.
- [ ] Expansion unlocks.
- [ ] Bigger venues unlock.
- [ ] Better sponsors unlock.
- [ ] Better broadcast deals unlock.

---

## 7. Content Needed For Steam Early Access

### 7.1 Minimum launchable content

- [ ] 60+ fictional wrestlers.
- [ ] 12+ fictional promotions.
- [ ] 20+ fictional venues.
- [ ] 20+ fictional sponsors.
- [ ] 12+ referees.
- [ ] 12+ announcers/commentators.
- [ ] 20+ production/equipment options.
- [ ] 40+ storyline templates.
- [ ] 30+ match types/segment types.
- [ ] 50+ backstage events.
- [ ] 50+ pre-show intel events.
- [ ] 100+ report flavour lines.

### 7.2 Tutorial content

- [ ] First campaign tutorial.
- [ ] Booking board tutorial.
- [ ] Pre-show intel tutorial.
- [ ] Staff assignment tutorial.
- [ ] Post-show report tutorial.
- [ ] Roster momentum tutorial.
- [ ] Finances tutorial.
- [ ] Save/load tutorial.

### 7.3 Difficulty settings

- [ ] Casual promoter.
- [ ] Balanced sim.
- [ ] Brutal booker.
- [ ] Sandbox/no bankruptcy.
- [ ] Custom difficulty.

---

## 8. User Interface / UX

### 8.1 Navigation

- [ ] Persistent top navigation.
- [ ] Clear back/forward flow.
- [ ] Breadcrumbs or current mode label.
- [ ] No dead-end screens.
- [ ] Every screen explains next action.
- [ ] Hotkeys for common actions.
- [ ] Confirm destructive actions.

### 8.2 Accessibility

- [ ] Scalable UI.
- [ ] Font size options.
- [ ] High contrast mode.
- [ ] Colourblind-safe indicators.
- [ ] Keyboard navigation.
- [ ] Controller support if targeting Steam Deck/console later.
- [ ] Reduce motion option.
- [ ] Clear icons with text labels.

### 8.3 Settings menu

- [ ] Display resolution.
- [ ] Windowed/fullscreen/borderless.
- [ ] UI scale.
- [ ] Text speed.
- [ ] Autosave frequency.
- [ ] Audio volume.
- [ ] Music volume.
- [ ] SFX volume.
- [ ] Reset tutorial prompts.
- [ ] Data/export options.

### 8.4 Polish pass

- [ ] Loading states.
- [ ] Empty states.
- [ ] Error states.
- [ ] Tooltip system.
- [ ] Explanation panels.
- [ ] Search/filter/sort tables.
- [ ] Consistent buttons.
- [ ] Consistent card styling.
- [ ] Screen transitions.
- [ ] Better icons.

---

## 9. Steam Features

### 9.1 Steam onboarding

- [ ] Create Steamworks partner account.
- [ ] Complete digital paperwork.
- [ ] Pay Steam Direct app fee.
- [ ] Set app name.
- [ ] Configure packages/depots.
- [ ] Configure test branches.
- [ ] Add developer/publisher info.

### 9.2 Steam store page

- [ ] Short description.
- [ ] Long description.
- [ ] Feature bullets.
- [ ] Early Access section if applicable.
- [ ] Roadmap section if applicable.
- [ ] System requirements.
- [ ] Supported languages.
- [ ] Genre tags.
- [ ] Screenshots.
- [ ] Trailer.
- [ ] Capsule art.
- [ ] Library art.
- [ ] Header/capsule/icon assets.
- [ ] Content survey/age-rating requirements.
- [ ] Wishlist campaign.

### 9.3 Steam build pipeline

- [ ] Create Windows build.
- [ ] Create Linux build if supported.
- [ ] Create Steam Deck test build.
- [ ] Configure SteamPipe.
- [ ] Configure depots.
- [ ] Upload first private build.
- [ ] Test install/uninstall.
- [ ] Test updates.
- [ ] Test beta branches.
- [ ] Test clean machine launch.
- [ ] Test controller/keyboard/mouse.

### 9.4 Steamworks optional features

- [ ] Achievements.
- [ ] Steam Cloud saves.
- [ ] Steam Input / controller config.
- [ ] Rich Presence.
- [ ] Steam Deck support.
- [ ] Steam Playtest.
- [ ] Demo.
- [ ] Workshop/mod support later.
- [ ] Crash/error reporting.

### 9.5 Achievements ideas

- [ ] First Bell — Run your first show.
- [ ] Packed House — Sell out a venue.
- [ ] Chaos Merchant — Survive a show with a ref bump and sponsor penalty.
- [ ] Red Hot — Get a wrestler to Red Hot momentum.
- [ ] The Hard Out — Finish within one minute of a strict TV deadline.
- [ ] Wrong Winner — Experience a referee wrong-winner disaster.
- [ ] Sponsor Nightmare — Lose money from sponsor penalties.
- [ ] Booker of the Year — Finish a season with high fan trust.
- [ ] From Gym Hall To Gold — Reach national status.
- [ ] No Yearly Reset — Complete five seasons in one save.

---

## 10. Build Quality / QA

### 10.1 Testing

- [ ] Unit tests for formulas.
- [ ] Unit tests for save migration.
- [ ] Unit tests for score ranges.
- [ ] Unit tests for campaign economy.
- [ ] Unit tests for injury/fatigue risk.
- [ ] Unit tests for sponsor penalties.
- [ ] Unit tests for overrun fines.
- [ ] Regression tests for old saves.
- [ ] Smoke test for every major screen.
- [ ] Long-run simulation test for 5 seasons.

### 10.2 Performance

- [ ] Load time under acceptable threshold.
- [ ] Smooth UI with large roster.
- [ ] Smooth UI with long show history.
- [ ] No memory leaks over long sessions.
- [ ] Save/load fast enough.
- [ ] Large generated universe does not freeze.

### 10.3 Bug tracking

- [ ] Create issue templates.
- [ ] Add labels:
  - bug,
  - sim-balance,
  - ui-ux,
  - steam,
  - legal-ip,
  - content,
  - economy,
  - save-load,
  - accessibility.
- [ ] Add milestone structure:
  - Prototype,
  - Vertical Slice,
  - Demo,
  - Early Access,
  - 1.0.

### 10.4 Release criteria

Do not release until:

- [ ] No known save-corrupting bugs.
- [ ] No crash on launch.
- [ ] No dead-end navigation.
- [ ] At least one full season can be played.
- [ ] Player can recover from mistakes.
- [ ] Tutorial explains the basic loop.
- [ ] Steam build installs cleanly.
- [ ] Store page accurately describes game.
- [ ] All default content is fictional and IP-safe.

---

## 11. Steam Demo Plan

### 11.1 Demo scope

Recommended demo:

- [ ] 8-week campaign slice.
- [ ] One fictional promotion.
- [ ] 16–24 wrestlers.
- [ ] Limited venues.
- [ ] Limited sponsors.
- [ ] Full booking loop.
- [ ] Post-show reports.
- [ ] Roster momentum.
- [ ] Save disabled or limited.
- [ ] Clear wishlist call-to-action.

### 11.2 Demo goal

The demo should prove:

- [ ] the booking loop is fun,
- [ ] reports are funny/interesting,
- [ ] choices have consequences,
- [ ] players want to keep building the promotion,
- [ ] the game has a unique voice.

---

## 12. Early Access Plan

### 12.1 Early Access launch requirements

- [ ] Stable weekly loop.
- [ ] Save/load stable.
- [ ] 1–3 seasons playable.
- [ ] Enough content variety.
- [ ] Visible roadmap.
- [ ] Feedback button/link.
- [ ] Clear known limitations.
- [ ] Regular update plan.

### 12.2 Early Access roadmap ideas

- [ ] Career wrestler mode later.
- [ ] Story mode seasons later.
- [ ] Mod support.
- [ ] Deeper contracts.
- [ ] Rival promotions.
- [ ] Talent scouting.
- [ ] More production disasters.
- [ ] Steam Workshop.
- [ ] Steam Deck polish.
- [ ] Console version investigation after PC success.

---

## 13. Marketing / Community

### 13.1 Positioning

Possible description:

> Rookie Quest: Ringmaster is a wrestling promotion management sim where every booking decision, staff mistake, sponsor demand, ref bump, and backstage grudge can change the future of your company.

### 13.2 Audience

- [ ] Wrestling fans.
- [ ] Football Manager-style sim players.
- [ ] Booking simulator players.
- [ ] Management/tycoon fans.
- [ ] Players who like emergent stories.

### 13.3 Store hooks

- [ ] "Football Manager meets wrestling chaos."
- [ ] "Book the card. Manage the egos. Survive the sponsors."
- [ ] "Every show creates a story."
- [ ] "No yearly reset. Build one living promotion."

### 13.4 Community pipeline

- [ ] Discord or community hub.
- [ ] Devlog schedule.
- [ ] Steam announcements.
- [ ] TikTok/Instagram feature clips.
- [ ] GIFs of report chaos.
- [ ] Short videos of bad referee calls / sponsor chaos.
- [ ] Wishlist push.
- [ ] Demo feedback form.

---

## 14. Suggested Development Phases

### Phase 1 — Prototype cleanup

- [ ] Keep current HTML prototype.
- [ ] Fix navigation.
- [ ] Move shared styles to CSS.
- [ ] Move simulation formulas to JS modules.
- [ ] Add simple save wrapper.
- [ ] Add show history page.
- [ ] Add production effects to night report.

### Phase 2 — Vertical slice

- [ ] Pick engine/runtime.
- [ ] Rebuild core loop in final architecture.
- [ ] Add persistent save files.
- [ ] Add first tutorial.
- [ ] Add 20 wrestlers.
- [ ] Add 8-week playable campaign.
- [ ] Add balance pass.
- [ ] Add first QA pass.

### Phase 3 — Steam demo

- [ ] Steam store coming soon page.
- [ ] Trailer.
- [ ] Screenshots.
- [ ] Demo build.
- [ ] Steam Playtest/demo QA.
- [ ] Wishlist campaign.

### Phase 4 — Early Access

- [ ] 1–3 seasons playable.
- [ ] Contracts.
- [ ] Injuries.
- [ ] Rival promotions.
- [ ] More content.
- [ ] Steam achievements/cloud.
- [ ] Community feedback cycle.

### Phase 5 — 1.0

- [ ] Full campaign progression.
- [ ] Polished UI.
- [ ] Steam Deck support target.
- [ ] Robust mod/export tools.
- [ ] Strong tutorial/onboarding.
- [ ] Balanced economy.
- [ ] Final QA.

---

## 15. Immediate Next 25 Tasks

These are the next practical tasks from the current repo state.

1. [ ] Add show history page.
2. [ ] Save every night report into a report history array.
3. [ ] Wire production setup into night report.
4. [ ] Add overrun/fine calculation.
5. [ ] Add sponsor mention calculation.
6. [ ] Add production incident generation.
7. [ ] Add equipment incident generation.
8. [ ] Add forced cut-short warning in booking board.
9. [ ] Add match finish selector.
10. [ ] Add winner selector.
11. [ ] Add storyline assignment per segment.
12. [ ] Add title match toggle.
13. [ ] Add roster selector instead of free-text participants.
14. [ ] Add persistent campaign state wrapper.
15. [ ] Replace repeated localStorage logic with helper functions.
16. [ ] Add shared CSS file.
17. [ ] Add shared navigation component.
18. [ ] Add real save/load screen.
19. [ ] Add settings screen.
20. [ ] Add first tutorial overlay.
21. [ ] Add content seed file for wrestlers.
22. [ ] Add content seed file for staff/referees/sponsors.
23. [ ] Add simple automated smoke test.
24. [ ] Decide final engine/runtime.
25. [ ] Create Steam demo scope document.

---

## 16. Steam Readiness Definition

The game is Steam-ready when:

- [ ] The full core loop works without manual workaround.
- [ ] Saves work across updates.
- [ ] The game has at least one satisfying multi-week campaign arc.
- [ ] The player can understand what to do next.
- [ ] The player sees clear consequences from choices.
- [ ] Default content is legally safe and fictional.
- [ ] The game has enough content to avoid feeling empty.
- [ ] The Steam build installs, launches, saves, quits, and reloads cleanly.
- [ ] Store page screenshots match the actual game.
- [ ] Trailer shows real gameplay.
- [ ] The demo/Early Access description is honest.
- [ ] There is a post-launch update plan.

---

## 17. Brutal Truth Checklist

Before asking players for money, answer these honestly:

- [ ] Is the core loop fun after 10 shows?
- [ ] Does the player care about at least 5 wrestlers?
- [ ] Do reports surprise the player without feeling random?
- [ ] Do choices create readable consequences?
- [ ] Can a new player understand the game in 10 minutes?
- [ ] Does the save system work reliably?
- [ ] Are the Steam screenshots exciting?
- [ ] Is the trailer honest and clear?
- [ ] Is the game stable enough that negative reviews will not be mostly technical?
- [ ] Is the Early Access scope honest?

If any answer is no, keep building.
