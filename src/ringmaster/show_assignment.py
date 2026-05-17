from __future__ import annotations

from dataclasses import dataclass

from .talent import TalentProfile


@dataclass(frozen=True)
class ShowAssignment:
    show_id: str
    wrestler_id: str
    role: str


@dataclass(frozen=True)
class AssignmentReport:
    show_id: str
    assigned_ids: list[str]
    style_cohesion: float
    heel_face_balance: float
    draw_score: float


class ShowAssignmentEngine:
    def assign_show(self, show_id: str, roster: list[TalentProfile], target_size: int = 6) -> AssignmentReport:
        if not roster:
            return AssignmentReport(show_id, [], 0.0, 0.0, 0.0)

        # prioritize draw and crowd reaction for card spots
        ordered = sorted(roster, key=lambda t: (t.draw * 0.6 + t.crowd_reaction * 0.4), reverse=True)
        picked = ordered[: max(1, min(target_size, len(ordered)))]

        style_counts: dict[str, int] = {}
        align_counts = {"face": 0, "heel": 0, "tweener": 0}
        draw_total = 0.0
        for t in picked:
            style_counts[t.style] = style_counts.get(t.style, 0) + 1
            align_counts[t.alignment] = align_counts.get(t.alignment, 0) + 1
            draw_total += t.draw

        max_style = max(style_counts.values()) if style_counts else 0
        style_cohesion = round(max_style / len(picked) * 100, 2) if picked else 0.0

        face = align_counts["face"]
        heel = align_counts["heel"]
        heel_face_balance = round((1 - abs(face - heel) / max(1, len(picked))) * 100, 2)

        draw_score = round(draw_total / len(picked), 2)

        return AssignmentReport(
            show_id=show_id,
            assigned_ids=[t.id for t in picked],
            style_cohesion=style_cohesion,
            heel_face_balance=heel_face_balance,
            draw_score=draw_score,
        )
