from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agents.execution import ExecutionPlannerAgent
from app.agents.ingestion import DataIngestionAgent
from app.agents.risk_prediction import RiskPredictionAgent
from app.agents.root_cause import RootCauseIntelligenceAgent
from app.agents.scenario import ScenarioSimulationAgent, sustainability_score
from app.agents.solution import SolutionRecommendationAgent
from app.models import Horizon, IngestionEvent, RegionRequest, ScenarioInput
from app.services.store import SustainabilityStore

app = FastAPI(title="BharatSustain AI API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

store = SustainabilityStore()
risk_agent = RiskPredictionAgent()
root_agent = RootCauseIntelligenceAgent()
scenario_agent = ScenarioSimulationAgent()
solution_agent = SolutionRecommendationAgent()
execution_agent = ExecutionPlannerAgent()
ingestion_agent = DataIngestionAgent(store)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "system": "BharatSustain AI", "mode": "adaptive"}


@app.get("/regions")
def regions() -> list[dict]:
    return store.regions()


@app.post("/risk")
def risk(request: RegionRequest, horizon: Horizon = Horizon.one_year) -> dict:
    region = store.get_region(request.state, request.district)
    scores = risk_agent.predict(region, horizon)
    return {"region": region, "sustainability_score": sustainability_score(region), "risks": scores}


@app.post("/root-cause")
def root_cause(request: RegionRequest, issue: str = "Water Scarcity") -> dict:
    return root_agent.explain(store.get_region(request.state, request.district), issue)


@app.post("/simulate")
def simulate(scenario: ScenarioInput) -> dict:
    baseline = store.get_region(scenario.region.state, scenario.region.district)
    return scenario_agent.simulate(baseline, scenario)


@app.post("/solutions")
def solutions(request: RegionRequest, budget_crore: float = 2500) -> dict:
    region = store.get_region(request.state, request.district)
    ranked = solution_agent.recommend(region, budget_crore)
    return {"region": region, "solutions": ranked}


@app.post("/execution-plan")
def execution_plan(request: RegionRequest, budget_crore: float = 2500) -> dict:
    region = store.get_region(request.state, request.district)
    top_solution = solution_agent.recommend(region, budget_crore)[0]
    return execution_agent.plan(top_solution, region)


@app.post("/ingest")
def ingest(event: IngestionEvent) -> dict:
    update = ingestion_agent.ingest(event)
    if update["accepted"]:
        update["new_risks"] = risk_agent.predict(update["updated_region"], Horizon.one_year)
    return update


@app.get("/events")
def events() -> list[dict]:
    return store.recent_events()
