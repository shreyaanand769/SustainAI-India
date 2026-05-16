# BharatSustain AI

BharatSustain AI is a full-stack prototype for India's adaptive sustainability intelligence and risk prediction operating system. It combines a futuristic Next.js command dashboard, FastAPI multi-agent backend, demo ML training pipeline, event-driven recalculation reference, deployment manifests, architecture documentation, and sample policy reports.

## Product capabilities

- National, state, district, and local-cluster risk intelligence.
- Live risk radar for heat, AQI, water scarcity, flood threat, agriculture stress, population pressure, and resource depletion.
- District digital twins with sustainability scores and future risk horizons.
- Root-cause dependency graphs for primary, secondary, and hidden systemic causes.
- Scenario simulation for population growth, rainfall decline, EV adoption, solar expansion, and groundwater extraction.
- Intervention marketplace with impact, cost, difficulty, ROI, carbon reduction, scalability, and feasibility.
- Execution planner with phased roadmap, agencies, manpower, milestones, dependencies, and KPIs.
- Adaptive intelligence loop that ingests new events and recalculates risks, recommendations, and plans.

## Monorepo layout

```text
apps/web          Next.js, TypeScript, Tailwind, Framer Motion, Recharts dashboard
apps/api          FastAPI multi-agent API and demo regional data
apps/ml           Scikit-learn demo model training pipeline
pipelines         Streaming/event-loop reference scripts
infra/k8s         Kubernetes deployment and services
docs              Architecture diagram and technical notes
sample-reports    Example generated policy report content
```

## Quick start

### Backend

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd apps/web
npm install
npm run dev
```

Open `http://localhost:3000` for the dashboard and `http://localhost:8000/docs` for interactive API documentation.

## API examples

```bash
curl -X POST 'http://localhost:8000/risk?horizon=1_year' \
  -H 'Content-Type: application/json' \
  -d '{"district":"Bengaluru Urban","state":"Karnataka"}'
```

```bash
curl -X POST 'http://localhost:8000/ingest' \
  -H 'Content-Type: application/json' \
  -d '{"source":"demo.imd","region_id":"KA-BLRU","metric":"water","value":96,"unit":"risk_index","observed_at":"2026-05-16T00:00:00Z"}'
```

## Deployment

Run locally with Docker Compose:

```bash
docker compose up --build
```

Deploy to Kubernetes after publishing images:

```bash
kubectl apply -f infra/k8s/bharatsustain.yaml
```

## ML pipeline

```bash
cd apps/ml
pip install -r requirements.txt
python train_risk_model.py
```

## Data and ML roadmap

The checked-in demo data is synthetic for safe local prototyping. Production adapters should connect to ISRO/Bhuvan satellite products, CPCB AQI, IMD weather, Census India, India water-resource datasets, OpenStreetMap, World Bank indicators, state budget/scheme systems, and citizen-reporting channels. The serving API is designed so those streams can update risk vectors through the `/ingest` contract.

## Governance and explainability

BharatSustain AI is designed for human-in-the-loop planning. Every risk includes drivers and confidence, every root-cause answer includes causal graph weights, every intervention exposes cost/ROI/carbon assumptions, and every execution plan lists agencies and KPIs for auditability.
