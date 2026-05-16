from __future__ import annotations


class RootCauseIntelligenceAgent:
    def explain(self, region: dict, issue: str) -> dict:
        templates = {
            "water": [
                ("groundwater over-extraction", "primary", 0.92),
                ("concretization and low recharge", "secondary", 0.84),
                ("lake/wetland degradation", "hidden systemic", 0.79),
                ("rainfall mismanagement", "secondary", 0.73),
            ],
            "heat": [
                ("urban sprawl", "primary", 0.88),
                ("tree-cover decline", "primary", 0.82),
                ("high construction density", "secondary", 0.78),
                ("low cool-roof adoption", "hidden systemic", 0.64),
            ],
            "aqi": [
                ("transport emissions", "primary", 0.86),
                ("construction dust", "secondary", 0.76),
                ("industrial cluster emissions", "secondary", 0.69),
                ("weak enforcement capacity", "hidden systemic", 0.62),
            ],
        }
        key = "water" if "water" in issue.lower() else "heat" if "heat" in issue.lower() else "aqi"
        causes = templates[key]
        return {
            "region": f"{region['district']}, {region['state']}",
            "issue": issue,
            "primary_causes": [c for c in causes if c[1] == "primary"],
            "secondary_causes": [c for c in causes if c[1] == "secondary"],
            "hidden_systemic_causes": [c for c in causes if c[1] == "hidden systemic"],
            "graph": [{"from": c[0], "to": issue, "weight": c[2], "type": c[1]} for c in causes],
        }
