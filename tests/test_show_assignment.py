from ringmaster.show_assignment import ShowAssignmentEngine
from ringmaster.talent import TalentProfile


def _t(i: str, align: str, style: str, draw: int, crowd: int) -> TalentProfile:
    return TalentProfile(
        id=i,
        ring_name=i,
        alignment=align,
        style=style,
        age=28,
        draw=draw,
        crowd_reaction=crowd,
        dangerous=40,
        injury_prone=30,
        injures_others_risk=20,
        promo=60,
        finisher_name="X",
        finisher_popularity=55,
        technical=60,
        psychology=60,
        stamina=60,
        athleticism=60,
        safety=60,
    )


def test_show_assignment_reports_metrics() -> None:
    roster = [
        _t("a", "face", "technical", 70, 72),
        _t("b", "heel", "technical", 66, 68),
        _t("c", "face", "powerhouse", 62, 60),
        _t("d", "heel", "high_flyer", 58, 64),
    ]
    report = ShowAssignmentEngine().assign_show("weekly_a", roster, target_size=4)
    assert len(report.assigned_ids) == 4
    assert report.draw_score > 0
    assert 0 <= report.heel_face_balance <= 100
