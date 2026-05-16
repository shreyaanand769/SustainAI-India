from __future__ import annotations

from app.models import Intervention


class ExecutionPlannerAgent:
    def plan(self, intervention: Intervention, region: dict) -> dict:
        return {
            "region": f"{region['district']}, {region['state']}",
            "intervention": intervention.name,
            "timeline": [
                {"phase": "Phase 1", "duration": "0-90 days", "actions": ["mission cell", "baseline survey", "risk zoning", "budget sanction"], "budget_crore": round(intervention.cost_crore * 0.12, 2)},
                {"phase": "Phase 2", "duration": "3-18 months", "actions": ["procurement", "deployment", "public dashboard", "training"], "budget_crore": round(intervention.cost_crore * 0.58, 2)},
                {"phase": "Phase 3", "duration": "18-60 months", "actions": ["scale-up", "maintenance contracts", "model monitoring", "impact audit"], "budget_crore": round(intervention.cost_crore * 0.30, 2)},
            ],
            "agencies": ["State planning department", "District collectorate", "ULB/Panchayats", "CPCB/SPCB", "IMD/ISRO data partners", "NGO implementation partners"],
            "dependencies": ["data sharing MoU", "land/asset access", "procurement clearance", "community adoption"],
            "manpower": {"program_managers": 4, "field_engineers": 28, "data_analysts": 6, "community_facilitators": 40},
            "monitoring_metrics": intervention.roadmap["kpis"],
        }
