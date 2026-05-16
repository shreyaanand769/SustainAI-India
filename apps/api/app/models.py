from __future__ import annotations

from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class Horizon(str, Enum):
    one_month = "1_month"
    six_months = "6_months"
    one_year = "1_year"
    five_years = "5_years"
    ten_years = "10_years"


class RegionRequest(BaseModel):
    state: str | None = None
    district: str | None = None
    cluster: str | None = None


class RiskScore(BaseModel):
    risk: str
    severity: int = Field(ge=0, le=100)
    urgency: str
    impact_radius_km: float
    confidence: float = Field(ge=0, le=1)
    horizon: Horizon
    drivers: list[str]


class ScenarioInput(BaseModel):
    region: RegionRequest
    population_growth_pct: float = 0
    rainfall_change_pct: float = 0
    ev_adoption_change_pct: float = 0
    solar_infra_change_pct: float = 0
    groundwater_extraction_change_pct: float = 0
    budget_crore: float = 1000


class Intervention(BaseModel):
    name: str
    impact_score: int
    cost_crore: float
    difficulty: str
    scalability: str
    roi: float
    carbon_reduction_tonnes: float
    feasibility: float
    roadmap: dict[str, Any]


class IngestionEvent(BaseModel):
    source: str
    region_id: str
    metric: str
    value: float
    unit: str
    observed_at: str
