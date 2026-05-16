from __future__ import annotations

from app.models import ScenarioInput


class ScenarioSimulationAgent:
    def simulate(self, baseline: dict, scenario: ScenarioInput) -> dict:
        water_delta = scenario.rainfall_change_pct * -0.45 + scenario.groundwater_extraction_change_pct * 0.55
        heat_delta = scenario.population_growth_pct * 0.22 - scenario.solar_infra_change_pct * 0.08
        aqi_delta = scenario.population_growth_pct * 0.18 - scenario.ev_adoption_change_pct * 0.25
        projected = baseline.copy()
        projected["water"] = clamp(projected["water"] + water_delta)
        projected["heat"] = clamp(projected["heat"] + heat_delta)
        projected["aqi"] = clamp(projected["aqi"] + aqi_delta)
        projected["population"] = clamp(projected["population"] + scenario.population_growth_pct * 0.35)
        score_before = sustainability_score(baseline)
        score_after = sustainability_score(projected)
        return {
            "baseline_score": score_before,
            "projected_score": score_after,
            "score_change": round(score_after - score_before, 2),
            "projected_conditions": projected,
            "economic_impact_crore": round((score_before - score_after) * 42 + max(0, scenario.population_growth_pct) * 18, 2),
            "environmental_tradeoffs": ["water stress rises when rainfall drops or extraction continues", "EV adoption improves AQI but requires grid readiness", "solar infrastructure reduces heat and carbon exposure"],
        }


def clamp(value: float) -> float:
    return max(0, min(100, round(value, 2)))


def sustainability_score(region: dict) -> float:
    risk_average = (region["heat"] + region["water"] + region["aqi"] + region["flood"] + region["agriculture"] + region["population"]) / 6
    return round(100 - risk_average * 0.72 + region["governance"] * 0.18, 2)
