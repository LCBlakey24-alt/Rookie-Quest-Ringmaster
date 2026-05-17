from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from .campaign import CampaignSnapshot
from .world import Brand


SAVE_VERSION = 1


@dataclass(frozen=True)
class SaveGame:
    version: int
    player_brand_id: str
    week: int
    brands: list[Brand]
    last_snapshot: CampaignSnapshot | None = None


def create_save(player_brand_id: str, week: int, brands: list[Brand], snapshot: CampaignSnapshot | None = None) -> SaveGame:
    return SaveGame(
        version=SAVE_VERSION,
        player_brand_id=player_brand_id,
        week=week,
        brands=brands,
        last_snapshot=snapshot,
    )


def save_to_file(save: SaveGame, path: Path) -> None:
    payload = {
        "version": save.version,
        "player_brand_id": save.player_brand_id,
        "week": save.week,
        "brands": [asdict(b) for b in save.brands],
        "last_snapshot": asdict(save.last_snapshot) if save.last_snapshot else None,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2))


def load_from_file(path: Path) -> SaveGame:
    payload = json.loads(path.read_text())
    version = int(payload.get("version", 0))
    if version != SAVE_VERSION:
        raise ValueError(f"Unsupported save version: {version}")

    brands = [Brand(**item) for item in payload.get("brands", [])]
    raw_snapshot = payload.get("last_snapshot")
    snapshot = CampaignSnapshot(**raw_snapshot) if raw_snapshot else None

    return SaveGame(
        version=version,
        player_brand_id=payload["player_brand_id"],
        week=int(payload["week"]),
        brands=brands,
        last_snapshot=snapshot,
    )
