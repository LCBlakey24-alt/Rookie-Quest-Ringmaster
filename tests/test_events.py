from ringmaster.events import EventEngine


def test_event_engine_generates_risk_events() -> None:
    events = EventEngine().generate(fan_trust_delta=-4.0, entrance_morale_delta=-1.5)
    titles = [e.title for e in events]
    assert "Fan Fatigue Concerns" in titles
    assert "Top Star Entrance Dispute" in titles


def test_event_engine_generates_stable_event() -> None:
    events = EventEngine().generate(fan_trust_delta=0.0, entrance_morale_delta=0.0)
    assert len(events) == 1
    assert events[0].title == "Locker Room Stable"
