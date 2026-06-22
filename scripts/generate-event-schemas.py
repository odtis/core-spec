#!/usr/bin/env python3
"""Generate per-event JSON Schema stubs from registry/events.yaml."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / "registry/events.yaml"
SCHEMAS = ROOT / "registry/events/schemas"


def parse_events(text: str) -> list[dict]:
    events: list[dict] = []
    block: dict | None = None
    in_reqs = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("- id:"):
            if block:
                events.append(block)
            block = {"id": s.split(":", 1)[1].strip()}
            in_reqs = False
        elif block and s.startswith("status:"):
            block["status"] = s.split(":", 1)[1].strip()
        elif block and s.startswith("description:"):
            block["description"] = s.split(":", 1)[1].strip()
        elif block and s.startswith("odtis_requirements:"):
            block["odtis_requirements"] = []
            in_reqs = True
        elif block and in_reqs and s.startswith("- ODTIS-"):
            block["odtis_requirements"].append(s[2:].strip())
        elif block and in_reqs and not s.startswith("- "):
            in_reqs = False
    if block:
        events.append(block)
    return events


def main() -> int:
    if not SCHEMAS.is_dir():
        SCHEMAS.mkdir(parents=True)
    events = parse_events(EVENTS.read_text(encoding="utf-8"))
    for ev in events:
        eid = ev["id"]
        safe = eid.replace(".", "-")
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": f"https://digitaltrustinfrastructure.org/odtis/events/{safe}.schema.json",
            "title": eid,
            "description": ev.get("description", ""),
            "allOf": [
                {"$ref": "envelope.schema.json"},
                {
                    "type": "object",
                    "properties": {
                        "event_type": {"const": eid},
                        "payload": {
                            "type": "object",
                            "additionalProperties": True,
                        },
                    },
                },
            ],
        }
        out = SCHEMAS / f"{safe}.schema.json"
        out.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(events)} event schemas to {SCHEMAS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
