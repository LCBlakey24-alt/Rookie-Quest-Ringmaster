from ringmaster.booking import BookingBoard, BookingSegment
from ringmaster.models import MatchOutcome, Segment


def test_booking_board_reorder_and_runtime() -> None:
    board = BookingBoard()
    board.add_segment(BookingSegment(Segment("Opener", 12, 65, 60), MatchOutcome.CLEAN))
    board.add_segment(BookingSegment(Segment("Main", 25, 85, 80), MatchOutcome.DIRTY))
    board.add_segment(BookingSegment(Segment("Semi", 22, 75, 70), MatchOutcome.CLEAN))

    assert board.total_minutes() == 59
    board.move_segment(2, 1)
    assert board.segments[1].segment.name == "Semi"


def test_booking_board_pacing_warnings() -> None:
    board = BookingBoard()
    board.add_segment(BookingSegment(Segment("Long A", 24, 70, 70), MatchOutcome.CLEAN))
    board.add_segment(BookingSegment(Segment("Long B", 21, 72, 71), MatchOutcome.CLEAN))
    board.add_segment(BookingSegment(Segment("Main", 140, 90, 88), MatchOutcome.CLEAN))

    warnings = board.pacing_warnings()
    assert any("back-to-back" in w for w in warnings)
    assert any("very long" in w for w in warnings)
