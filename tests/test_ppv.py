from ringmaster.ppv import PPVScheduler


def test_ppv_schedule_customization() -> None:
    events = PPVScheduler().build_monthly_schedule(
        ["Neon Collision", "Empire Fall"],
        ["Ladder", "Steel Cage"],
    )
    assert len(events) == 2
    assert events[0].theme == "Ladder"
    assert events[1].week_of_month == 2
