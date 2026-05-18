from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DialogueContext:
    sender: str
    topic: str
    relationship: int  # 0-100
    urgency: int  # 0-100


@dataclass(frozen=True)
class DialogueOutcome:
    reply: str
    relationship_delta: int
    stress_delta: int


class DialogueEngine:
    """Prototype text-intent responder for freeform player replies."""

    def respond(self, context: DialogueContext, player_text: str) -> DialogueOutcome:
        text = player_text.lower().strip()

        positive = any(k in text for k in ["thanks", "appreciate", "great", "happy", "yes", "agree"])
        negative = any(k in text for k in ["no", "never", "useless", "hate", "angry", "ridiculous"])
        respectful = any(k in text for k in ["please", "understand", "sorry", "respect"])
        demanding = any(k in text for k in ["must", "immediately", "do it", "now"])

        relationship_delta = 0
        stress_delta = 0

        if positive:
            relationship_delta += 4
            stress_delta -= 1
        if respectful:
            relationship_delta += 2
        if negative:
            relationship_delta -= 5
            stress_delta += 2
        if demanding:
            relationship_delta -= 2
            stress_delta += 2

        if context.urgency > 70 and "later" in text:
            relationship_delta -= 3
            stress_delta += 2

        tone = "professional"
        if relationship_delta >= 4:
            tone = "supportive"
        elif relationship_delta <= -4:
            tone = "defensive"

        reply = self._build_reply(context, tone)

        return DialogueOutcome(
            reply=reply,
            relationship_delta=max(-10, min(10, relationship_delta)),
            stress_delta=max(-5, min(8, stress_delta)),
        )

    def _build_reply(self, context: DialogueContext, tone: str) -> str:
        if tone == "supportive":
            return f"{context.sender}: I hear you. We'll align on {context.topic} and move forward together."
        if tone == "defensive":
            return f"{context.sender}: I don't like how this is being handled. We need to revisit {context.topic}."
        return f"{context.sender}: Understood. I'll proceed with the current plan on {context.topic}."
