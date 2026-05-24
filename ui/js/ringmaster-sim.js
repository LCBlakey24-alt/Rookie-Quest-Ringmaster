/*
  Rookie Quest: Ringmaster
  Shared prototype simulation helpers.

  These helpers are intentionally plain JavaScript so the current HTML prototype
  can use them immediately. Later, this logic should move into the real game
  runtime/simulation layer.
*/

(function () {
  function seededValue(text, min, max) {
    let hash = 0;
    const source = String(text ?? '');
    for (let i = 0; i < source.length; i += 1) hash = (hash * 31 + source.charCodeAt(i)) % 100000;
    return min + (hash % (max - min + 1));
  }

  function clamp(value, min = 0, max = 100) {
    const number = Number(value);
    if (Number.isNaN(number)) return min;
    return Math.max(min, Math.min(max, Math.round(number)));
  }

  function splitParticipants(text) {
    return String(text || '').split(/\s+vs\.?\s+|,|&/i).map((entry) => entry.trim()).filter((entry) => entry && entry !== '—');
  }

  function grade(score) {
    if (score >= 85) return { label: 'Excellent', tone: 'good' };
    if (score >= 70) return { label: 'Strong', tone: 'good' };
    if (score >= 55) return { label: 'Mixed', tone: 'warn' };
    return { label: 'Weak', tone: 'bad' };
  }

  function momentumState(momentum) {
    if (momentum >= 85) return 'Red Hot';
    if (momentum >= 70) return 'Hot';
    if (momentum >= 58) return 'Rising';
    if (momentum >= 40) return 'Stable';
    return 'Cold';
  }

  function styleBucket(style) {
    const lower = String(style || '').toLowerCase();
    if (lower.includes('big-event')) return 'bigFight';
    if (lower.includes('showbiz')) return 'showbiz';
    if (lower.includes('sports') || lower.includes('official') || lower.includes('house')) return 'sports';
    if (lower.includes('nervous')) return 'plain';
    return 'neutral';
  }

  function wrestlerPreference(name) { return ['bigFight', 'showbiz', 'sports', 'plain'][seededValue(name, 0, 3)]; }
  function preferenceLabel(preference) {
    return { bigFight: 'big-fight introductions', showbiz: 'theatrical showbiz hype', sports: 'clean sports-style announcing', plain: 'low-key no-nonsense intros' }[preference] || 'neutral introductions';
  }

  function baseSegmentScore(segment, index, cardLength) {
    const base = segment.type === 'Match' ? 62 : segment.type === 'Promo' ? 56 : segment.type === 'Angle' ? 52 : 48;
    const lengthBonus = Math.min(12, Math.max(-8, Number(segment.mins || 0) - 8));
    const nameBonus = seededValue(`${segment.name}${segment.participants}`, -7, 12);
    const cardPositionBonus = index === cardLength - 1 ? 8 : index === 0 ? 3 : 0;
    const latePenalty = segment.lateChange ? -2 : 0;
    return base + lengthBonus + nameBonus + cardPositionBonus + latePenalty;
  }

  function matchTypeEffect(segment) {
    const type = String(segment.matchType || 'Singles Match');
    const notes = [];
    let score = 0, audience = 0, fatigue = 0, injuryRisk = 0, clarity = 0, momentum = 0;
    let risky = false, spectacle = false;
    if (segment.type !== 'Match') return { score, audience, fatigue, injuryRisk, clarity, momentum, risky, spectacle, notes: [] };

    if (type === 'Singles Match') {
      clarity += 2; fatigue += 2; notes.push('A standard singles match gave the card a clear competitive base.');
    } else if (type === 'Tag Team Match') {
      audience += 2; fatigue += 2; clarity -= 1; notes.push('The tag format added energy, though the moving parts made the story slightly busier.');
    } else if (type === 'Triple Threat') {
      audience += 3; fatigue += 3; clarity -= 2; risky = true; notes.push('The triple threat raised chaos and crowd energy, but made the finish harder to read.');
    } else if (type === 'Fatal Four Way') {
      audience += 4; fatigue += 4; clarity -= 3; risky = true; notes.push('The four-way packed the ring with action, at the cost of clarity and fatigue.');
    } else if (type === 'Ladder Match') {
      score += 3; audience += 6; fatigue += 7; injuryRisk += 5; clarity -= 2; momentum += 2; risky = true; spectacle = true; notes.push('The ladder match gave the show a spectacle spike, but added serious fatigue and injury risk.');
    } else if (type === 'Cage Match') {
      score += 2; audience += 5; fatigue += 6; injuryRisk += 4; clarity += 1; momentum += 2; risky = true; spectacle = true; notes.push('The cage match made the feud feel important and boosted the big-fight atmosphere.');
    } else if (type === 'Hardcore Match') {
      audience += 6; fatigue += 8; injuryRisk += 6; clarity -= 3; momentum += 2; risky = true; spectacle = true; notes.push('The hardcore stipulation created wild crowd energy, but the safety risk was obvious.');
    } else if (type === 'Iron Match') {
      score += 3; audience += 3; fatigue += 8; clarity += 3; momentum += 3; notes.push('The iron match rewarded stamina and made the result feel definitive.');
    } else if (type === 'Battle Royal') {
      audience += 5; fatigue += 4; injuryRisk += 2; clarity -= 4; risky = true; spectacle = true; notes.push('The battle royal felt like a big attraction, but individual stories were harder to follow.');
    } else if (type === 'Squash Match') {
      score -= 1; audience += 1; fatigue += 1; clarity += 3; momentum += 1; notes.push('The squash match clearly highlighted the winner, but offered limited in-ring drama.');
    }
    return { score, audience, fatigue, injuryRisk, clarity, momentum, risky, spectacle, notes };
  }

  function finishEffect(segment) {
    const finish = String(segment.finish || '').toLowerCase();
    const isMatch = segment.type === 'Match';
    const notes = [];
    let score = 0, audience = 0, clarity = 0, morale = 0, winnerMomentum = 0, loserMomentum = 0;
    let dirty = false, unclear = false;
    const protectedLoser = Boolean(segment.protectLoser);
    const titleBoost = Boolean(segment.titleMatch) ? 3 : 0;
    if (!isMatch) {
      if (finish.includes('promo win') || finish.includes('story beat')) { score += 1; clarity += 1; notes.push(`${segment.finish || 'Story Beat'} gave the non-match segment a clearer purpose.`); }
      return { score, audience, clarity, morale, winnerMomentum, loserMomentum, dirty, unclear, protectedLoser, titleBoost: 0, notes };
    }
    if (finish.includes('clean pinfall') || finish.includes('clean submission')) {
      score += 4; clarity += 4; audience += 2; winnerMomentum += 3; loserMomentum -= protectedLoser ? 0 : 2; notes.push(`${segment.winner || 'The winner'} got a clean finish, improving credibility and giving the crowd a clear result.`);
    } else if (finish.includes('dirty')) {
      score += 1; clarity -= 1; audience += 3; winnerMomentum += 2; loserMomentum += protectedLoser ? 1 : -1; dirty = true; notes.push(`${segment.winner || 'The winner'} stole the result with a dirty finish. Heat increased, but clarity took a small hit.`);
    } else if (finish.includes('interference')) {
      score += 2; clarity -= 3; audience += 4; winnerMomentum += 2; loserMomentum += protectedLoser ? 2 : -1; dirty = true; unclear = true; notes.push('Interference protected the loser and created story heat, but the finish was less satisfying.');
    } else if (finish.includes('dq') || finish.includes('count-out')) {
      score -= 2; clarity -= 4; audience -= 1; loserMomentum += protectedLoser ? 1 : -2; unclear = true; notes.push(`${segment.finish} kept the story moving but risked frustrating fans who wanted a real result.`);
    } else if (finish.includes('ref mistake')) {
      score -= 4; clarity -= 6; audience += 1; morale -= 2; unclear = true; notes.push('The booked ref mistake made the result controversial and may annoy the wrestlers involved.');
    } else if (finish.includes('time limit') || finish.includes('no contest')) {
      score -= 1; clarity -= 3; audience += 1; loserMomentum += 1; unclear = true; notes.push(`${segment.finish} avoided a decisive loss, but the crowd needed a stronger reason to accept it.`);
    }
    if (segment.titleMatch) { score += titleBoost; audience += 2; notes.push('Title stakes lifted the importance of the match.'); }
    if (protectedLoser && !finish.includes('clean')) { morale += 1; notes.push('The loser was protected, reducing morale damage while keeping the story open.'); }
    return { score, audience, clarity, morale, winnerMomentum, loserMomentum, dirty, unclear, protectedLoser, titleBoost, notes };
  }

  function announcerEffect(segment, announcerProfile) {
    const announcer = announcerProfile || { name: 'Default Announcer', style: 'House voice', hype: 60, clarity: 60, professionalism: 60 };
    if (segment.type !== 'Match') return { boost: 0, audience: 0, notes: ['No direct wrestler intro effect on this non-match segment.'], annoyed: [] };
    const style = styleBucket(announcer.style);
    let boost = 0, audience = 0; const notes = [], annoyed = [];
    splitParticipants(segment.participants).forEach((name) => {
      const preference = wrestlerPreference(name);
      if (preference === style) { boost += 3; audience += 2; notes.push(`${name} prefers ${preferenceLabel(preference)} and looked more fired up.`); }
      else if (announcer.clarity < 55) { boost -= 3; audience -= 1; annoyed.push(name); notes.push(`${name} looked annoyed after a muddled introduction.`); }
      else if (announcer.hype < 45 && preference === 'bigFight') { boost -= 2; audience -= 2; annoyed.push(name); notes.push(`${name} wanted a grander big-fight intro and came out flat.`); }
      else { audience += 1; notes.push(`${name}'s intro was acceptable, but not a perfect style match.`); }
    });
    return { boost, audience, notes, annoyed: [...new Set(annoyed)] };
  }

  function refereeEffect(segment, index, refereeProfile) {
    const referee = refereeProfile || { name: 'Default Referee', control: 60, accuracy: 60, toughness: 60, drama: 50, quirk: 'Calls the match mostly down the middle.' };
    if (segment.type !== 'Match') return { score: 0, clarity: 0, notes: ['No referee impact on this non-match segment.'], badCall: false, refBump: false, wrongWinner: false, injury: false, annoyed: [] };
    const chaos = seededValue(`${referee.name}-${segment.name}-${index}`, 0, 100);
    let score = 0, clarity = 0; const notes = []; let badCall = false, refBump = false, wrongWinner = false, injury = false, annoyed = [];
    if (referee.control >= 80) { score += 2; clarity += 3; notes.push(`${referee.name} kept the pace controlled and the finish credible.`); }
    if (referee.accuracy < 50 && chaos > 52) { score -= 5; clarity -= 6; badCall = true; annoyed = splitParticipants(segment.participants); notes.push(`${referee.name} missed a key rope break and the crowd argued with the finish.`); }
    if (referee.accuracy < 45 && chaos > 78) { score -= 8; clarity -= 10; wrongWinner = true; badCall = true; annoyed = splitParticipants(segment.participants); notes.push(`${referee.name} appeared to count the wrong winner. Production had to scramble to explain it.`); }
    if (referee.drama > 80 && chaos > 60) { score += 3; clarity -= 4; refBump = true; notes.push(`${referee.name} took a dramatic ref bump, which spiked chaos but muddied the finish.`); }
    if (referee.toughness < 45 && refBump && chaos > 72) { score -= 4; clarity -= 5; injury = true; notes.push(`${referee.name} stayed down after the bump and a backup official was needed.`); }
    return { score, clarity, notes, badCall, refBump, wrongWinner, injury, annoyed: [...new Set(annoyed)] };
  }

  function intelEffect(segment, preShowIntel) {
    if (!preShowIntel) return { boost: 0, audience: 0, notes: [] };
    const mentions = String(segment.participants || '').toLowerCase().includes(String(preShowIntel.name || '').toLowerCase());
    if (!mentions) return { boost: 0, audience: 0, notes: [] };
    if (preShowIntel.reacted || segment.intelReaction) return { boost: 2, audience: Number(preShowIntel.fanBonus || 8), notes: [`${preShowIntel.source || 'Pre-show intel'} was addressed. Fans reacted strongly to seeing ${preShowIntel.name}.`] };
    return { boost: 0, audience: 0, notes: [] };
  }

  function productionSegmentEffect(segment, index, productionSetup) {
    const setup = productionSetup || {};
    const crew = setup.crew || { name: 'Default Crew', camera: 60, timing: 60, director: 60, chaos: 50, cost: 0, quirk: 'Basic production support.' };
    const equipment = setup.equipment || { name: 'Default Equipment', safety: 60, visuals: 60, reliability: 60, cost: 0, quirk: 'Basic reliable setup.' };
    const roll = seededValue(`${crew.name}-${equipment.name}-${segment.name}-${index}`, 0, 100);
    let score = 0, audience = 0, safety = 0; const notes = []; let missedShot = false, equipmentIssue = false, stageSave = false;
    if (crew.camera >= 80 && segment.type === 'Match') { score += 2; audience += 1; notes.push(`${crew.name} caught the important reactions and made the action feel bigger.`); }
    else if (crew.camera < 55 && segment.type === 'Match' && roll > 55) { score -= 4; audience -= 2; missedShot = true; notes.push(`${crew.name} missed a key camera shot, flattening the crowd reaction on broadcast.`); }
    if (equipment.visuals >= 85 && (segment.type === 'Video' || segment.type === 'Promo' || index === 0)) { score += 3; audience += 2; stageSave = true; notes.push(`${equipment.name} made the presentation feel like a bigger event.`); }
    if ((equipment.safety < 55 || equipment.reliability < 55) && segment.type === 'Match' && roll > 65) { score -= 5; safety -= 5; equipmentIssue = true; notes.push(`${equipment.name} caused a ringside/equipment scare that distracted from the match.`); }
    if (crew.director >= 80 && (segment.type === 'Angle' || segment.type === 'Promo')) { score += 2; notes.push(`${crew.name}'s director helped the segment land cleanly.`); }
    return { score, audience, safety, notes, missedShot, equipmentIssue, stageSave };
  }

  function productionShowEffects(card, productionSetup) {
    const setup = productionSetup || {};
    const crew = setup.crew || { name: 'Default Crew', timing: 60, cost: 0, chaos: 50 };
    const sponsor = setup.sponsor || { name: 'No Major Sponsor', money: 0, pressure: 0, mentions: 0, fine: 0 };
    const equipment = setup.equipment || { name: 'Default Equipment', cost: 0, reliability: 60, safety: 60 };
    const timing = setup.timing || { name: 'Flexible Slot', hardOut: 25, fineRisk: 10, overtimeFine: 0 };
    const safeCard = Array.isArray(card) ? card : [];
    const totalMinutes = safeCard.reduce((sum, segment) => sum + Number(segment.mins || 0), 0);
    const targetMinutes = 150;
    const overrunMinutes = Math.max(0, totalMinutes - targetMinutes);
    const sponsorMentionsNeeded = Number(sponsor.mentions || 0);
    const sponsorSegments = safeCard.filter((segment) => String(segment.name || '').toLowerCase().includes('sponsor') || String(segment.type || '').toLowerCase().includes('sponsor')).length;
    const sponsorMentionsMissed = Math.max(0, sponsorMentionsNeeded - sponsorSegments);
    const overrunFine = overrunMinutes > 0 && Number(timing.fineRisk || 0) > 40 ? Math.round(Number(timing.overtimeFine || 0) * Math.min(2, overrunMinutes / 15)) : 0;
    const sponsorPenalty = sponsorMentionsMissed > 0 ? Math.round(Number(sponsor.fine || 0) * Math.min(1, sponsorMentionsMissed / Math.max(1, sponsorMentionsNeeded))) : 0;
    const productionCost = Number(crew.cost || 0) + Number(equipment.cost || 0);
    const sponsorRevenue = Number(sponsor.money || 0);
    const notes = [];
    if (overrunMinutes > 0) notes.push(`${timing.name} was pushed ${overrunMinutes} minute(s) over target.`);
    if (overrunFine > 0) notes.push(`Broadcast timing triggered an overrun fine of $${overrunFine.toLocaleString()}.`);
    if (sponsorMentionsMissed > 0) notes.push(`${sponsor.name} expected ${sponsorMentionsNeeded} sponsor mention(s), but ${sponsorMentionsMissed} were missed.`);
    if (sponsorPenalty > 0) notes.push(`Sponsor penalty applied: $${sponsorPenalty.toLocaleString()}.`);
    if (productionCost > 0) notes.push(`Production and equipment cost $${productionCost.toLocaleString()}.`);
    if (sponsorRevenue > 0) notes.push(`${sponsor.name} contributed $${sponsorRevenue.toLocaleString()} in sponsor revenue.`);
    return { totalMinutes, targetMinutes, overrunMinutes, overrunFine, sponsorMentionsNeeded, sponsorSegments, sponsorMentionsMissed, sponsorPenalty, productionCost, sponsorRevenue, notes };
  }

  function scoreCard(card, context = {}) {
    const safeCard = Array.isArray(card) && card.length ? card : [];
    return safeCard.map((segment, index) => {
      const announcerResult = announcerEffect(segment, context.announcerProfile);
      const refereeResult = refereeEffect(segment, index, context.refereeProfile);
      const intelResult = intelEffect(segment, context.preShowIntel);
      const productionResult = productionSegmentEffect(segment, index, context.productionSetup);
      const finishResult = finishEffect(segment);
      const matchTypeResult = matchTypeEffect(segment);
      const base = baseSegmentScore(segment, index, safeCard.length);
      const score = clamp(base + announcerResult.boost + announcerResult.audience + refereeResult.score + refereeResult.clarity + intelResult.boost + intelResult.audience + productionResult.score + productionResult.audience + productionResult.safety + finishResult.score + finishResult.audience + finishResult.clarity + matchTypeResult.score + matchTypeResult.audience + matchTypeResult.clarity, 1, 99);
      return { segment, index, base, score, grade: grade(score), announcerEffect: announcerResult, refereeEffect: refereeResult, intelEffect: intelResult, productionEffect: productionResult, finishEffect: finishResult, matchTypeEffect: matchTypeResult };
    });
  }

  function averageScore(results, predicate = null) {
    const filtered = predicate ? results.filter((result) => predicate(result.segment, result)) : results;
    if (!filtered.length) return 0;
    return Math.round(filtered.reduce((sum, result) => sum + Number(result.score || 0), 0) / filtered.length);
  }

  function buildFallout({ overall = 0, commentary = 60, announcer = 60, referee = 60, preShowIntel = null, lateChanges = 0, annoyedNames = [], badCalls = 0, refInjuries = 0, productionShow = null, productionIncidents = 0, equipmentIncidents = 0, unclearFinishes = 0, dirtyFinishes = 0, riskyMatches = 0, injuryRiskTotal = 0 } = {}) {
    const fallout = { fanTrust: 0, popularity: 0, morale: 0, storyClarity: 0, cash: 0, notes: [] };
    if (overall >= 75) { fallout.fanTrust += 4; fallout.popularity += 3; fallout.cash += 18000; fallout.notes.push('Strong show lifted fan trust and ticket demand.'); }
    else if (overall < 55) { fallout.fanTrust -= 5; fallout.popularity -= 2; fallout.cash -= 9000; fallout.notes.push('Weak show hurt fan trust.'); }
    else { fallout.fanTrust += 1; fallout.cash += 4000; fallout.notes.push('Steady show kept the company moving.'); }
    if (commentary < 50) { fallout.storyClarity -= 4; fallout.notes.push('Poor commentary damaged story clarity.'); }
    else if (commentary >= 80) { fallout.storyClarity += 3; fallout.notes.push('Strong commentary made the stories clearer.'); }
    if (referee < 50) { fallout.storyClarity -= 3; fallout.fanTrust -= 2; fallout.notes.push('Poor refereeing damaged finish credibility.'); }
    else if (referee >= 80) { fallout.storyClarity += 2; fallout.notes.push('Strong refereeing protected match finishes.'); }
    if (badCalls) { fallout.fanTrust -= badCalls * 2; fallout.morale -= badCalls * 2; fallout.notes.push('Bad referee calls caused backstage complaints.'); }
    if (refInjuries) { fallout.cash -= 5000; fallout.notes.push('Referee injury created medical and production costs.'); }
    if (announcer < 50) { fallout.fanTrust -= 1; fallout.notes.push('Weak announcing made the show feel smaller.'); }
    if (annoyedNames.length) { fallout.morale -= annoyedNames.length * 2; fallout.notes.push('Staff mistakes annoyed talent backstage.'); }
    if (unclearFinishes) { fallout.fanTrust -= unclearFinishes; fallout.storyClarity -= unclearFinishes * 2; fallout.notes.push('Unclear finishes made the card harder for fans to understand.'); }
    if (dirtyFinishes >= 3) { fallout.fanTrust -= 2; fallout.notes.push('Too many dirty finishes made the show feel overbooked.'); }
    if (riskyMatches >= 3) { fallout.morale -= 2; fallout.notes.push('A risky match-heavy card raised locker-room fatigue concerns.'); }
    if (injuryRiskTotal >= 10) { fallout.cash -= 3500; fallout.notes.push('High-risk stipulations increased medical and insurance pressure.'); }
    if (preShowIntel && preShowIntel.reacted) { fallout.fanTrust += 2; fallout.popularity += 1; fallout.morale -= Number(preShowIntel.changeRisk || 4); fallout.cash += Number(preShowIntel.fanBonus || 8) * 700; fallout.notes.push('Reacting to pre-show intel excited fans but created last-minute booking pressure.'); }
    if (preShowIntel && preShowIntel.ignored) { fallout.fanTrust -= 2; fallout.notes.push('Ignoring pre-show intel kept the show stable but cooled some fan buzz.'); }
    if (lateChanges > 1) { fallout.morale -= 2; fallout.notes.push('Multiple late changes created backstage friction.'); }
    if (productionShow) {
      fallout.cash += Number(productionShow.sponsorRevenue || 0) - Number(productionShow.productionCost || 0) - Number(productionShow.overrunFine || 0) - Number(productionShow.sponsorPenalty || 0);
      fallout.notes.push(...(productionShow.notes || []));
      if (productionShow.overrunFine > 0) { fallout.fanTrust -= 1; fallout.storyClarity -= 1; }
      if (productionShow.sponsorPenalty > 0) fallout.notes.push('Sponsor relationship damaged by missed obligations.');
    }
    if (productionIncidents) { fallout.storyClarity -= productionIncidents; fallout.notes.push('Production incidents reduced broadcast clarity.'); }
    if (equipmentIncidents) { fallout.morale -= equipmentIncidents * 2; fallout.cash -= equipmentIncidents * 2500; fallout.notes.push('Equipment issues created safety concerns and repair costs.'); }
    return fallout;
  }

  window.RingmasterSim = Object.freeze({
    seededValue, clamp, splitParticipants, grade, momentumState, styleBucket, wrestlerPreference, preferenceLabel,
    baseSegmentScore, matchTypeEffect, finishEffect, announcerEffect, refereeEffect, intelEffect, productionSegmentEffect, productionShowEffects,
    scoreCard, averageScore, buildFallout
  });
})();
