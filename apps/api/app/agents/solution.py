from __future__ import annotations

from app.models import Intervention


class SolutionRecommendationAgent:
    def recommend(self, region: dict, budget_crore: float = 2500) -> list[Intervention]:
        catalog = [
            ("Managed aquifer recharge and lake revival", "Water", 94, 1100, 3.6, 300000),
            ("Urban cool-roof and heat shelter grid", "Heat", 91, 650, 2.8, 1100000),
            ("AI precision irrigation and crop diversification", "Agriculture", 83, 480, 4.1, 600000),
            ("Flood zoning and sponge-city corridors", "Flood", 88, 1400, 2.2, 900000),
            ("Ward-scale material recovery and waste-to-energy", "Waste", 79, 720, 2.5, 500000),
        ]
        ranked = []
        for name, domain, impact, cost, roi, carbon in catalog:
            feasibility = min(0.95, max(0.45, budget_crore / (cost * 2.4)))
            ranked.append(Intervention(
                name=f"{name} — {region['district']}",
                impact_score=impact,
                cost_crore=cost,
                difficulty="medium" if cost < 1000 else "high",
                scalability="state-wide" if domain in {"Water", "Heat", "Agriculture"} else "urban clusters",
                roi=roi,
                carbon_reduction_tonnes=carbon,
                feasibility=round(feasibility, 2),
                roadmap={
                    "phase_1": "90-day diagnostics, stakeholder alignment, priority wards/blocks, procurement plan",
                    "phase_2": "6-18 month deployment, civil works, sensors, community operating model",
                    "phase_3": "18-60 month scaling, outcome-linked finance, monitoring and adaptive optimization",
                    "kpis": ["risk score reduction", "beneficiaries covered", "₹ per unit resilience gain", "CO2e avoided"],
                },
            ))
        return sorted(ranked, key=lambda intervention: intervention.impact_score * intervention.feasibility, reverse=True)
