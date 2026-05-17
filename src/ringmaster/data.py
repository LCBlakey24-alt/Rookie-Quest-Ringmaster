from __future__ import annotations

import json
from pathlib import Path

from .models import Wrestler


def _score(value: int) -> int:
    return max(1, min(100, int(value)))


def load_wrestler_from_file(path: Path) -> Wrestler:
    payload = json.loads(path.read_text())
    return Wrestler(
        id=payload["id"],
        ring_name=payload["ringName"],
        technique=_score(payload["attributes"]["technique"]),
        psychology=_score(payload["attributes"]["psychology"]),
        stamina=_score(payload["attributes"]["stamina"]),
        athleticism=_score(payload["attributes"]["athleticism"]),
        safety=_score(payload["attributes"]["safety"]),
        charisma=_score(payload["promo"]["charisma"]),
        popularity=_score(payload["popularity"]["national"]),
        fatigue=max(0, min(100, int(payload["health"]["fatigue"]))),
    )


def load_sample_wrestlers(repo_root: Path) -> list[Wrestler]:
    samples_dir = repo_root / "data" / "samples"
    files = sorted(samples_dir.glob("wrestler.*.json"))
    return [load_wrestler_from_file(file_path) for file_path in files]
