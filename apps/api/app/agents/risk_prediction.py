from __future__ import annotations

from app.models import Horizon, RiskScore

HORIZON_MULTIPLIER = {
    Horizon.one_month: 1.0,
    Horizon.six_months: 1.06,
    Horizon.one_year: 1.12,
    Horizon.five_years: 1.28,
    Horizon.ten_years: 1.42,
}


class RiskPredictionAgent:
    """Hybrid rules + ML placeholder for serving time-series/geospatial risk inference."""

    def predict(self, region: dict, horizon: Horizon = Horizon.one_year) -> list[RiskScore]:
        multiplier = HORIZON_MULTIPLIER[horizon]
        specs = {
            "Heatwave": (region["heat"] * 0.7 + region["population"] * 0.2 + region["infra"] * 0.1, ["urban heat island", "tree cover loss", "construction density"]),
            "Water Scarcity": (region["water"] * 0.75 + region["population"] * 0.15 + (100 - region["governance"]) * 0.1, ["groundwater extraction", "rainfall volatility", "lake degradation"]),
            "AQI Crisis": (region["aqi"] * 0.8 + region["infra"] * 0.1 + region["population"] * 0.1, ["transport emissions", "construction dust", "industrial clusters"]),
            "Flooding": (region["flood"] * 0.78 + region["infra"] * 0.12 + region["population"] * 0.1, ["drainage capacity gap", "wetland loss", "extreme rainfall"]),
            "Agricultural Decline": (region["agriculture"] * 0.65 + region["water"] * 0.25 + region["heat"] * 0.1, ["soil stress", "irrigation dependency", "crop heat exposure"]),
        }
        output: list[RiskScore] = []
        for name, (base, drivers) in specs.items():
            severity = int(max(0, min(100, base * multiplier)))
            urgency = "critical" if severity >= 85 else "high" if severity >= 70 else "watch"
            output.append(RiskScore(risk=name, severity=severity, urgency=urgency, impact_radius_km=10 + severity * 1.8, confidence=round(0.72 + min(severity, 95) / 500, 2), horizon=horizon, drivers=drivers))
        return sorted(output, key=lambda score: score.severity, reverse=True)
