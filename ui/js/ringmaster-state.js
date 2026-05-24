/*
  Rookie Quest: Ringmaster
  Shared prototype game-state helpers.

  This file is the first step away from scattered localStorage logic inside every
  HTML screen. It is still browser-prototype storage, but it creates one stable
  API that can later be replaced by real save files for Steam builds.
*/

(function () {
  const STORAGE_KEYS = Object.freeze({
    brandProfile: 'ringmaster_brand_profile',
    campaignState: 'ringmaster_campaign_state',
    week: 'ringmaster_week',
    bookingCard: 'ringmaster_booking_card',
    broadcastTeam: 'ringmaster_broadcast_team',
    refereeAssignment: 'ringmaster_referee_assignment',
    productionSetup: 'ringmaster_production_setup',
    preShowIntel: 'ringmaster_pre_show_intel',
    rosterState: 'ringmaster_roster_state',
    lastShowReport: 'ringmaster_last_show_report',
    lastFallout: 'ringmaster_last_fallout',
    lastRosterChanges: 'ringmaster_last_roster_changes',
    showHistory: 'ringmaster_show_history'
  });

  const DEFAULT_CAMPAIGN_STATE = Object.freeze({
    week: 1,
    popularity: 67,
    fanTrust: 68,
    morale: 72,
    storyClarity: 65,
    cash: 500000
  });

  const DEFAULT_ROSTER = Object.freeze([
    { name: 'Raven Blade', role: 'High-flying rebel', popularity: 64, morale: 70, fatigue: 18, momentum: 58, notes: ['Crowd likes the entrance energy.'] },
    { name: 'Kayla Stone', role: 'Technical ace', popularity: 61, morale: 74, fatigue: 12, momentum: 55, notes: ['Reliable promo presence.'] },
    { name: 'L. Cross', role: 'Main-event striker', popularity: 72, morale: 68, fatigue: 22, momentum: 65, notes: ['Feels close to a title moment.'] },
    { name: 'Victor Kane', role: 'Arrogant powerhouse', popularity: 70, morale: 62, fatigue: 20, momentum: 60, notes: ['Ego needs careful handling.'] },
    { name: 'J. Strike', role: 'Underdog brawler', popularity: 53, morale: 72, fatigue: 15, momentum: 48, notes: ['Could climb with the right feud.'] },
    { name: 'Nova Vale', role: 'Flashy prospect', popularity: 45, morale: 76, fatigue: 10, momentum: 44, notes: ['Fans are starting to notice.'] },
    { name: 'Brick Atlas', role: 'Monster heel', popularity: 57, morale: 58, fatigue: 28, momentum: 50, notes: ['Needs protected booking.'] },
    { name: 'Mara Voltage', role: 'Showbiz wildcard', popularity: 49, morale: 80, fatigue: 8, momentum: 52, notes: ['Thrives with theatrical presentation.'] }
  ]);

  function clone(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function readJson(key, fallback = null) {
    try {
      const raw = window.localStorage.getItem(key);
      if (raw === null || raw === undefined || raw === '') return clone(fallback);
      return JSON.parse(raw);
    } catch (error) {
      console.warn(`[RingmasterState] Failed to read ${key}`, error);
      return clone(fallback);
    }
  }

  function writeJson(key, value) {
    window.localStorage.setItem(key, JSON.stringify(value));
    return value;
  }

  function remove(key) {
    window.localStorage.removeItem(key);
  }

  function clamp(value, min = 0, max = 100) {
    const number = Number(value);
    if (Number.isNaN(number)) return min;
    return Math.max(min, Math.min(max, Math.round(number)));
  }

  function getWeek() {
    return Number(window.localStorage.getItem(STORAGE_KEYS.week) || 1);
  }

  function setWeek(week) {
    const safeWeek = Math.max(1, Number(week) || 1);
    window.localStorage.setItem(STORAGE_KEYS.week, String(safeWeek));
    const campaign = getCampaignState();
    campaign.week = safeWeek;
    setCampaignState(campaign);
    return safeWeek;
  }

  function advanceWeek() {
    return setWeek(getWeek() + 1);
  }

  function getBrandProfile() {
    return readJson(STORAGE_KEYS.brandProfile, null);
  }

  function setBrandProfile(profile) {
    return writeJson(STORAGE_KEYS.brandProfile, profile || {});
  }

  function hasCampaign() {
    const profile = getBrandProfile();
    return Boolean(profile && profile.brand_name);
  }

  function getCampaignState() {
    const profile = getBrandProfile();
    const fallback = clone(DEFAULT_CAMPAIGN_STATE);
    if (profile && profile.starting_cash) fallback.cash = Number(profile.starting_cash);
    const state = readJson(STORAGE_KEYS.campaignState, fallback) || fallback;
    return { ...fallback, ...state, week: Number(state.week || getWeek() || 1) };
  }

  function setCampaignState(state) {
    const current = getCampaignState();
    const next = {
      ...current,
      ...state,
      popularity: clamp(state?.popularity ?? current.popularity),
      fanTrust: clamp(state?.fanTrust ?? current.fanTrust),
      morale: clamp(state?.morale ?? current.morale),
      storyClarity: clamp(state?.storyClarity ?? current.storyClarity),
      cash: Math.max(0, Math.round(Number(state?.cash ?? current.cash ?? 0))),
      week: Math.max(1, Number(state?.week ?? current.week ?? 1))
    };
    return writeJson(STORAGE_KEYS.campaignState, next);
  }

  function applyFallout(fallout) {
    const current = getCampaignState();
    const safeFallout = fallout || {};
    const next = {
      ...current,
      popularity: clamp(current.popularity + Number(safeFallout.popularity || 0)),
      fanTrust: clamp(current.fanTrust + Number(safeFallout.fanTrust || 0)),
      morale: clamp(current.morale + Number(safeFallout.morale || 0)),
      storyClarity: clamp(current.storyClarity + Number(safeFallout.storyClarity || 0)),
      cash: Math.max(0, Math.round(current.cash + Number(safeFallout.cash || 0)))
    };
    setCampaignState(next);
    setLastFallout(safeFallout);
    return next;
  }

  function getBookingCard() {
    return readJson(STORAGE_KEYS.bookingCard, []);
  }

  function setBookingCard(card) {
    return writeJson(STORAGE_KEYS.bookingCard, Array.isArray(card) ? card : []);
  }

  function clearBookingCard() {
    remove(STORAGE_KEYS.bookingCard);
  }

  function getRoster() {
    const roster = readJson(STORAGE_KEYS.rosterState, null);
    return Array.isArray(roster) && roster.length ? roster : clone(DEFAULT_ROSTER);
  }

  function setRoster(roster) {
    return writeJson(STORAGE_KEYS.rosterState, Array.isArray(roster) ? roster : clone(DEFAULT_ROSTER));
  }

  function resetRoster() {
    return setRoster(clone(DEFAULT_ROSTER));
  }

  function getShowHistory() {
    const history = readJson(STORAGE_KEYS.showHistory, []);
    return Array.isArray(history) ? history : [];
  }

  function addShowHistoryEntry(entry) {
    const history = getShowHistory();
    const nextEntry = {
      id: entry?.id || `show-${Date.now()}`,
      createdAt: entry?.createdAt || new Date().toISOString(),
      week: Number(entry?.week || getWeek()),
      showName: entry?.showName || 'Untitled Show',
      overall: Number(entry?.overall || 0),
      crowdMood: entry?.crowdMood || 'Unknown',
      notes: Array.isArray(entry?.notes) ? entry.notes : []
    };
    history.unshift({ ...entry, ...nextEntry });
    const trimmed = history.slice(0, 100);
    writeJson(STORAGE_KEYS.showHistory, trimmed);
    return trimmed;
  }

  function getLastShowReport() {
    return readJson(STORAGE_KEYS.lastShowReport, null);
  }

  function setLastShowReport(report) {
    return writeJson(STORAGE_KEYS.lastShowReport, report || {});
  }

  function getLastFallout() {
    return readJson(STORAGE_KEYS.lastFallout, null);
  }

  function setLastFallout(fallout) {
    return writeJson(STORAGE_KEYS.lastFallout, fallout || {});
  }

  function getLastRosterChanges() {
    const changes = readJson(STORAGE_KEYS.lastRosterChanges, []);
    return Array.isArray(changes) ? changes : [];
  }

  function setLastRosterChanges(changes) {
    return writeJson(STORAGE_KEYS.lastRosterChanges, Array.isArray(changes) ? changes : []);
  }

  function getStaffSetup() {
    return {
      broadcastTeam: readJson(STORAGE_KEYS.broadcastTeam, null),
      refereeAssignment: readJson(STORAGE_KEYS.refereeAssignment, null),
      productionSetup: readJson(STORAGE_KEYS.productionSetup, null)
    };
  }

  function getPreShowIntel() {
    return readJson(STORAGE_KEYS.preShowIntel, null);
  }

  function setPreShowIntel(intel) {
    return writeJson(STORAGE_KEYS.preShowIntel, intel || {});
  }

  function clearPreShowIntel() {
    remove(STORAGE_KEYS.preShowIntel);
  }

  function exportPrototypeSave() {
    const payload = {
      version: 1,
      exportedAt: new Date().toISOString(),
      keys: {}
    };
    Object.values(STORAGE_KEYS).forEach((key) => {
      payload.keys[key] = readJson(key, null);
    });
    return payload;
  }

  function importPrototypeSave(payload) {
    if (!payload || typeof payload !== 'object' || !payload.keys) {
      throw new Error('Invalid Rookie Quest: Ringmaster prototype save payload.');
    }
    Object.values(STORAGE_KEYS).forEach((key) => {
      if (Object.prototype.hasOwnProperty.call(payload.keys, key)) {
        writeJson(key, payload.keys[key]);
      }
    });
    return true;
  }

  window.RingmasterState = Object.freeze({
    STORAGE_KEYS,
    DEFAULT_CAMPAIGN_STATE,
    DEFAULT_ROSTER: clone(DEFAULT_ROSTER),
    readJson,
    writeJson,
    remove,
    clamp,
    getWeek,
    setWeek,
    advanceWeek,
    getBrandProfile,
    setBrandProfile,
    hasCampaign,
    getCampaignState,
    setCampaignState,
    applyFallout,
    getBookingCard,
    setBookingCard,
    clearBookingCard,
    getRoster,
    setRoster,
    resetRoster,
    getShowHistory,
    addShowHistoryEntry,
    getLastShowReport,
    setLastShowReport,
    getLastFallout,
    setLastFallout,
    getLastRosterChanges,
    setLastRosterChanges,
    getStaffSetup,
    getPreShowIntel,
    setPreShowIntel,
    clearPreShowIntel,
    exportPrototypeSave,
    importPrototypeSave
  });
})();
