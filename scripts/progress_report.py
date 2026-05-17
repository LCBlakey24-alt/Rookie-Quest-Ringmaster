#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    todo = Path('docs/MASTER_TODO.md').read_text().splitlines()
    done = sum(1 for line in todo if line.strip().startswith('- [x]'))
    total = sum(1 for line in todo if line.strip().startswith('- ['))
    pct = (done / total * 100) if total else 0.0
    print(f"Completed: {done}/{total}")
    print(f"Progress: {pct:.1f}%")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
