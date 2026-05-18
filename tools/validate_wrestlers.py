#!/usr/bin/env python3
"""Validate wrestler JSON files against the canonical schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    schema_path = repo_root / "data" / "schemas" / "wrestler.schema.json"
    samples_dir = repo_root / "data" / "samples"

    try:
        import jsonschema
    except ImportError:
        print("ERROR: jsonschema is not installed. Install with: pip install jsonschema")
        return 2

    schema = json.loads(schema_path.read_text())
    validator = jsonschema.Draft202012Validator(schema)

    wrestler_files = sorted(samples_dir.glob("wrestler.*.json"))
    if not wrestler_files:
        print("WARNING: No sample wrestler files found.")
        return 1

    failures = 0
    for file_path in wrestler_files:
        payload = json.loads(file_path.read_text())
        errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
        if errors:
            failures += 1
            print(f"FAIL {file_path.relative_to(repo_root)}")
            for error in errors:
                location = ".".join(str(p) for p in error.path) or "<root>"
                print(f"  - {location}: {error.message}")
        else:
            print(f"PASS {file_path.relative_to(repo_root)}")

    if failures:
        print(f"\nValidation failed for {failures} file(s).")
        return 1

    print("\nAll wrestler sample files passed schema validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
