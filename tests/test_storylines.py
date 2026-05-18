from ringmaster.storylines import Storyline, StorylineEngine


def test_storyline_progression_increases_heat_on_good_segment() -> None:
    s = Storyline("f1", "Blood Feud", "a", "b", heat=60, weeks_running=3)
    updated = StorylineEngine().progress(s, segment_rating=82.0, clean_finish=True)
    assert updated.heat > s.heat
    assert updated.weeks_running == 4
