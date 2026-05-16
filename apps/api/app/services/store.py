from __future__ import annotations

import json
from pathlib import Path
from threading import Lock
from typing import Any

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "demo_regions.json"


class SustainabilityStore:
    """Small in-memory store that mimics the serving layer fed by streams/TimescaleDB."""

    def __init__(self) -> None:
        self._lock = Lock()
        self._regions: list[dict[str, Any]] = json.loads(DATA_FILE.read_text())
        self._events: list[dict[str, Any]] = []

    def regions(self) -> list[dict[str, Any]]:
        with self._lock:
            return [region.copy() for region in self._regions]

    def get_region(self, state: str | None = None, district: str | None = None) -> dict[str, Any]:
        with self._lock:
            for region in self._regions:
                if district and region["district"].lower() == district.lower():
                    return region.copy()
                if state and region["state"].lower() == state.lower():
                    return region.copy()
            return self._regions[0].copy()

    def apply_event(self, event: dict[str, Any]) -> dict[str, Any]:
        metric = event["metric"]
        with self._lock:
            self._events.append(event)
            for region in self._regions:
                if region["region_id"] == event["region_id"] and metric in region:
                    region[metric] = max(0, min(100, float(event["value"])))
                    return region.copy()
        return {}

    def recent_events(self) -> list[dict[str, Any]]:
        with self._lock:
            return self._events[-25:]
