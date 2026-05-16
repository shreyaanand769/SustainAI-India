from __future__ import annotations

from app.models import IngestionEvent
from app.services.store import SustainabilityStore


class DataIngestionAgent:
    """Validates and applies streaming observations from weather, satellite, governance, and citizen feeds."""

    def __init__(self, store: SustainabilityStore) -> None:
        self.store = store

    def ingest(self, event: IngestionEvent) -> dict:
        updated = self.store.apply_event(event.model_dump())
        return {
            "accepted": bool(updated),
            "updated_region": updated,
            "adaptive_actions": [
                "risk vectors recalculated",
                "recommendation rankings refreshed",
                "execution plan KPIs reweighted",
                "alerts evaluated for escalation",
            ] if updated else [],
        }
