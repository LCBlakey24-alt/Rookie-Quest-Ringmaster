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
    for (let i = 0; i < source.length; i += 1) {
      hash = (hash * 31 + source.charCodeAt(i)) % 100000;
    }
    return min + (hash % (max - min + 1));
  }

  function clamp(value, min = 0, max = 100) {
    const number = Number(value);
    if (Number.isNaN(number)) return min;
    return Math.max(min, Math.min(max, Math.round(number)));
  }

  function splitParticipants(text) {
    return String(text || '')
      .split(/\s+vs\.?\s+|,|&/i)
      .map((entry) => entry.trim())
      .filter((entry) => entry && entry !== '—');
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

  function wrestlerPreference(name) {
    return ['bigFight', 'showbiz', 'sports', 'plain'][seededValue(name, 0, 3)];
  }

  function preferenceLabel(preference) {
    return {
      bigFight: 'big-fight introductions',
      showbiz: 'theatrical showbiz hype',
      sports: 'clean sports-style announcing',
      plain: 'low-key no-nonsense intros'
    }[preference] || 'neutral introductions';
  }

  function baseSegmentScore(segment, index, cardLength) {
    const base = segment.type === 'Match' ? 62 : segment.type === 'Promo' ? 56 : segment.type === 'Angle' ? 52 : 48;
    const lengthBonus = Math.min(12, Math.max(-8, Number(segment.mins || 0) - 8));
    const nameBonus = seededValue(`${segment.name}${segment.participants}`, -7, 12);
    const cardPositionBonus = index === cardLength - 1 ? 8 : index === 0 ? 3 : 0;
    const latePenalty = segment.lateChange ? -2 : 0;
    return base + lengthBonus + nameBonus + cardPositionBonus + latePenalty;
  }

  function announcerEffect(segment, announcerProfile) {
    const announcer = announcerProfile || {
      name: 'Default Announcer',
      style: 'House voice',
      hype: 60,
      clarity: 60,
      professionalism: 60
    };

    if (segment.type !== 'Match') {
      return { boost: 0, audience: 0, notes: ['No direct wrestler intro effect on this non-match segment.'], annoyed: [] };
    }

    const style = styleBucket(announcer.style);
    let boost = 0;
    let audience = 0;
    const notes = [];
    const annoyed = [];

    splitParticipants(segment.participants).forEach((name) => {
      const preference = wrestlerPreference(name);
      if (preference === style) {
        boost += 3;
        audience += 2;
        notes.push(`${name} prefers ${preferenceLabel(preference)} and looked more fired up.`);
      } else if (announcer.clarity < 55) {
        boost -= 3;
        audience -= 1;
        annoyed.push(name);
        notes.push(`${name} looked annoyed after a muddled introduction.`);
      } else if (announcer.hype < 45 && preference === 'bigFight') {
        boost -= 2;
        audience -= 2;
        annoyed.push(name);
        notes.push(`${name} wanted a grander big-fight intro and came out flat.`);
      } else {
        audience += 1;
        notes.push(`${name}'s intro was acceptable, but not a perfect style match.`);
      }
    });

    return { boost, audience, notes, annoyed: [...new Set(annoyed)] };
  }

  function refereeEffect(segment, index, refereeProfile) {
    const referee = refereeProfile || { name: 'Default Referee', control: 60, accuracy: 60, toughness: 60, drama: 50, quirk: 'Calls the match mostly down the middle.' };
    if (segment.type !== 'Match') {
      return { score: 0, clarity: 0, notes: ['No referee impact on this non-match segment.'], badCall: false, refBump: false, wrongWinner: false, injury: false, annoyed: [] };
    }

    const chaos = seededValue(`${referee.name}-${segment.name}-${index}`, 0, 100);
    let score = 0;
    let clarity = 0;
    const notes = [];
    let badCall = false;
    let refBump = false;
    let wrongWinner = false;
    let injury = false;
    let annoyed = [];

    if (referee.control >= 80) {
      score += 2;
      clarity += 3;
      notes.push(`${referee.name} kept the pace controlled and the finish credible.`);
    }
    if (referee.accuracy < 50 && chaos > 52) {
      score -= 5;
      clarity -= 6;
      badCall = true;
      annoyed = splitParticipants(segment.participants);
      notes.push(`${referee.name} missed a key rope break and the crowd argued with the finish.`);
    }
    if (referee.accuracy < 45 && chaos > 78) {
      score -= 8;
      clarity -= 10;
      wrongWinner = true;
      badCall = true;
      annoyed = splitParticipants(segment.participants);
      notes.push(`${referee.name} appeared to count the wrong winner. Production had to scramble to explain it.`);
    }
    if (referee.drama > 80 && chaos > 60) {
      score += 3;
      clarity -= 4;
      refBump = true;
      notes.push(`${referee.name} took a dramatic ref bump, which spiked chaos but muddied the finish.`);
    }
    if (referee.toughness < 45 && refBump && chaos > 72) {
      score -= 4;
      clarity -= 5;
      injury = true;
      notes.push(`${referee.name} stayed down after the bump and a backup official was needed.`);
    }
    return { score, clarity, notes, badCall, refBump, wrongWinner, injury, annoyed: [...new Set(annoyed)] };
  }

  function intelEffect(segment, preShowIntel) {
    if (!preShowIntel) return { boost: 0, audience: 0, notes: [] };
    const mentions = String(segment.participants || '').toLowerCase().includes(String(preShowIntel.name || '').toLowerCase());
    if (!mentions) return { boost: 0, audience: 0, notes: [] };
    if (preShowIntel.reacted || segment.intelReaction) {
      return { boost: 2, audience: Number(preShowIntel.fanBonus || 8), notes: [`${preShowIntel.source || 'Pre-show intel'} was addressed. Fans reacted strongly to seeing ${preShowIntel.name}.`] };
    }
    return { boost: 0, audience: 0, notes: [] };
  }

  function productionSegmentEffect(segment, index, productionSetup) {
    const setup = productionSetup || {};
    const crew = setup.crew || { name: 'Default Crew', camera: 60, timing: 60, director: 60, chaos: 50, cost: 0, quirk: 'Basic production support.' };
    const equipment = setup.equipment || { name: 'Default Equipment', safety: 60, visuals: 60, reliability: 60, cost: 0, quirk: 'Basic reliable setup.' };
    const seed = `${crew.name}-${equipment.name}-${segment.name}-${index}`;
    const roll = seededValue(seed, 0, 100);
    let score = 0;
    let audience = 0;
    let safety = 0;
    const notes = [];
    let missedShot = false;
    let equipmentIssue = false;
    let stageSave = false;

    if (crew.camera >= 80 && segment.type === 'Match') {
      score += 2;
      audience += 1;
      notes.push(`${crew.name} caught the important reactions and made the action feel bigger.`);
    } else if (crew.camera < 55 && segment.type === 'Match' && roll > 55) {
      score -= 4;
      audience -= 2;
      missedShot = true;
      notes.push(`${crew.name} missed a key camera shot, flattening the crowd reaction on broadcast.`);
    }

    if (equipment.visuals >= 85 && (segment.type === 'Video' || segment.type === 'Promo' || index === 0)) {
      score += 3;
      audience += 2;
      stageSave = true;
      notes.push(`${equipment.name} made the presentation feel like a bigger event.`);
    }

    if ((equipment.safety < 55 || equipment.reliability < 55) && segment.type === 'Match' && roll > 65) {
      score -= 5;
      safety -= 5;
      equipmentIssue = true;
      notes.push(`${equipment.name} caused a ringside/equipment scare that distracted from the match.`);
    }

    if (crew.director >= 80 && (segment.type === 'Angle' || segment.type === 'Promo')) {
      score += 2;
      notes.push(`${crew.name}'s director helped the segment land cleanly.`);
    }

    return { score, audience, safety, notes, missedShot, equipmentIssue, stageSave };
  }

  function productionShowEffects(card, productionSetup) {
    const setup = productionSetup || {};
    const crew = setup.crew || { name: 'Default Crew', timing: 60, cost: 0, chaos: 50 };
    const sponsor = setup.sponsor || { name: 'No Major Sponsor', money: 0, pressure: 0, mentions: 0, fine: 0 };
    const equipment = setup.equipment || { name: 'Default Equipment', cost: 0, reliability: 60, safety: 60 };
    const timing = setup.timing || { name: 'Flexible Slot', hardOut: 25, fineRisk: 10, overtimeFine: 0 };
    const totalMinutes = (Array.isArray(card) ? card : []).reduce((sum, segment) => sum + Number(segment.mins || 0), 0);
    const targetMinutes = 150;
    const overrunMinutes = Math.max(0, totalMinutes - targetMinutes);
    const sponsorMentionsNeeded = Number(sponsor.mentions || 0);
    const sponsorSegments = (Array.isArray(card) ? card : []).filter((segment) => String(segment.name || '').toLowerCase().includes('sponsor') || String(segment.type || '').toLowerCase().includes('sponsor')).length;
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
    const announcer = context.announcerProfile;
    const referee = context.refereeProfile;
    const intel = context.preShowIntel;
    const production = context.productionSetup;

    return safeCard.map((segment, index) => {
      const announcerResult = announcerEffect(segment, announcer);
      const refereeResult = refereeEffect(segment, index, referee);
      const intelResult = intelEffect(segment, intel);
      const productionResult = productionSegmentEffect(segment, index, production);
      const base = baseSegmentScore(segment, index, safeCard.length);
      const score = clamp(
        base + announcerResult.boost + announcerResult.audience + refereeResult.score + refereeResult.clarity + intelResult.boost + intelResult.audience + productionResult.score + productionResult.audience + productionResult.safety,
        1,
        99
      );

      return { segment, index, base, score, grade: grade(score), announcerEffect: announcerResult, refereeEffect: refereeResult, intelEffect: intelResult, productionEffect: productionResult };
    });
  }

  function averageScore(results, predicate = null) {
    const filtered = predicate ? results.filter((result) => predicate(result.segment, result)) : results;
    if (!filtered.length) return 0;
    return Math.round(filtered.reduce((sum, result) => sum + Number(result.score || 0), 0) / filtered.length);
  }

  function buildFallout({ overall = 0, commentary = 60, announcer = 60, referee = 60, preShowIntel = null, lateChanges = 0, annoyedNames = [], badCalls = 0, refInjuries = 0, productionShow = null, productionIncidents = 0, equipmentIncidents = 0 } = {}) {
    const fallout = { fanTrust: 0, popularity: 0, morale: 0, storyClarity: 0, cash: 0, notes: [] };

    if (overall >= 75) {
      fallout.fanTrust += 4; fallout.popularity += 3; fallout.cash += 18000; fallout.notes.push('Strong show lifted fan trust and ticket demand.');
    } else if (overall < 55) {
      fallout.fanTrust -= 5; fallout.popularity -= 2; fallout.cash -= 9000; fallout.notes.push('Weak show hurt fan trust.');
    } else {
      fallout.fanTrust += 1; fallout.cash += 4000; fallout.notes.push('Steady show kept the company moving.');
    }

    if (commentary < 50) { fallout.storyClarity -= 4; fallout.notes.push('Poor commentary damaged story clarity.'); }
    else if (commentary >= 80) { fallout.storyClarity += 3; fallout.notes.push('Strong commentary made the stories clearer.'); }

    if (referee < 50) { fallout.storyClarity -= 3; fallout.fanTrust -= 2; fallout.notes.push('Poor refereeing damaged finish credibility.'); }
    else if (referee >= 80) { fallout.storyClarity += 2; fallout.notes.push('Strong refereeing protected match finishes.'); }

    if (badCalls) { fallout.fanTrust -= badCalls * 2; fallout.morale -= badCalls * 2; fallout.notes.push('Bad referee calls caused backstage complaints.'); }
    if (refInjuries) { fallout.cash -= 5000; fallout.notes.push('Referee injury created medical and production costs.'); }
    if (announcer < 50) { fallout.fanTrust -= 1; fallout.notes.push('Weak announcing made the show feel smaller.'); }
    if (annoyedNames.length) { fallout.morale -= annoyedNames.length * 2; fallout.notes.push('Staff mistakes annoyed talent backstage.'); }

    if (preShowIntel && preShowIntel.reacted) {
      fallout.fanTrust += 2; fallout.popularity += 1; fallout.morale -= Number(preShowIntel.changeRisk || 4); fallout.cash += Number(preShowIntel.fanBonus || 8) * 700; fallout.notes.push('Reacting to pre-show intel excited fans but created last-minute booking pressure.');
    }
    if (preShowIntel && preShowIntel.ignored) { fallout.fanTrust -= 2; fallout.notes.push('Ignoring pre-show intel kept the show stable but cooled some fan buzz.'); }
    if (lateChanges > 1) { fallout.morale -= 2; fallout.notes.push('Multiple late changes created backstage friction.'); }

    if (productionShow) {
      fallout.cash += Number(productionShow.sponsorRevenue || 0) - Number(productionShow.productionCost || 0) - Number(productionShow.overrunFine || 0) - Number(productionShow.sponsorPenalty || 0);
      fallout.notes.push(...(productionShow.notes || []));
      if (productionShow.overrunFine > 0) { fallout.fanTrust -= 1; fallout.storyClarity -= 1; }
      if (productionShow.sponsorPenalty > 0) { fallout.cash -= 0; fallout.notes.push('Sponsor relationship damaged by missed obligations.'); }
    }
    if (productionIncidents) { fallout.storyClarity -= productionIncidents; fallout.notes.push('Production incidents reduced broadcast clarity.'); }
    if (equipmentIncidents) { fallout.morale -= equipmentIncidents * 2; fallout.cash -= equipmentIncidents * 2500; fallout.notes.push('Equipment issues created safety concerns and repair costs.'); }

    return fallout;
  }

  window.RingmasterSim = Object.freeze({
    seededValue, clamp, splitParticipants, grade, momentumState, styleBucket, wrestlerPreference, preferenceLabel,
    baseSegmentScore, announcerEffect, refereeEffect, intelEffect, productionSegmentEffect, productionShowEffects,
    scoreCard, averageScore, buildFallout
  });
})();
