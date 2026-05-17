from ringmaster.development import Prospect
from ringmaster.roster import DevelopmentRoster, MainRoster, RosterPipeline


def test_graduate_ready_and_loyal_prospects() -> None:
    dev = DevelopmentRoster(
        prospects=[
            Prospect("p1", "Rook Steel", potential=84, readiness=78, loyalty=60),
            Prospect("p2", "Sky Drift", potential=76, readiness=65, loyalty=70),
        ]
    )
    main = MainRoster(wrestlers=[])

    result = RosterPipeline().graduate_prospects(dev, main)

    assert "p1" in result.promoted_ids
    assert "p1" in main.wrestlers
    assert "p2" in result.stayed_ids


def test_release_unhappy_ready_prospect() -> None:
    dev = DevelopmentRoster(
        prospects=[Prospect("p9", "Volt Reign", potential=90, readiness=82, loyalty=20)]
    )
    main = MainRoster(wrestlers=[])

    result = RosterPipeline().graduate_prospects(dev, main)
    assert "p9" in result.released_ids
    assert "p9" not in main.wrestlers
