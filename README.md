# 🤖 Virtual Data Analyst Agent

> An end-to-end AI/ML system that accepts natural language business questions, queries structured databases, runs statistical and ML analysis, and returns narrative insights with charts.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-purple)](https://langchain.com)
[![MLflow](https://img.shields.io/badge/MLflow-2.13-orange)](https://mlflow.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📌 Project Overview

The **Virtual Data Analyst** is a 24-month, 4-module research and engineering capstone project. It combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), time-series forecasting, anomaly detection, and agentic reasoning into a single production-ready SaaS platform.

**Ask it:** _"What drove the Q3 revenue drop?"_ → It investigates, queries the DB, models the trend, and explains in plain English.

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────┐
│              Presentation Layer                      │
│   React + TypeScript  |  Chart.js  |  Auth (JWT)    │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│           API Gateway & Orchestration                │
│   FastAPI  |  LangChain Agent  |  Redis Queue        │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│                AI / ML Core                          │
│  LLM (GPT-4o/Mistral) | Text-to-SQL | RAG (Pinecone)│
│  Prophet/LSTM Forecasting | Anomaly (IsolationForest)│
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│                  Data Layer                          │
│   PostgreSQL  |  MongoDB  |  Airflow  |  dbt  |  S3 │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│              MLOps & Infrastructure                  │
│   MLflow  |  Docker/K8s  |  GitHub Actions  |  AWS   │
└─────────────────────────────────────────────────────┘
```

---

## 🗂 Repository Structure

```
virtual-analyst/
├── frontend/              # React + TypeScript dashboard
│   └── src/
├── backend/               # FastAPI application
│   ├── agents/            # LangChain agent tools & executor
│   ├── ml/                # Forecasting & anomaly detection
│   ├── sql_gen/           # Text-to-SQL module
│   └── api/               # Route handlers
├── data_pipelines/        # Airflow DAGs + dbt models
│   ├── dags/
│   └── dbt/
├── infra/                 # Docker, Kubernetes, Terraform
│   ├── docker/
│   └── k8s/
├── mlflow/                # Experiment configurations
├── notebooks/             # EDA & prototyping (Jupyter)
├── tests/                 # Unit + integration tests
│   ├── unit/
│   └── integration/
└── docs/                  # Architecture, API, runbooks
    ├── adr/               # Architecture Decision Records
    ├── runbooks/
    └── architecture/
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 20+
- Docker & Docker Compose
- PostgreSQL 15+

### Run with Docker Compose

```bash
git clone https://github.com/GeethaVegesna1910/virtual-analyst.git
cd virtual-analyst
cp .env.example .env          # Add your API keys
docker-compose up --build
```

Open `http://localhost:3000` for the dashboard, `http://localhost:8000/docs` for the API.

### Run locally (development)

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install && npm run dev
```

---

## 📅 Project Modules & Progress

| Module | Period | Focus | Status |
|--------|--------|-------|--------|
| **Module 1** | Months 1–6 | Foundation: Data pipeline + Text-to-SQL chatbot | 🔄 In Progress |
| **Module 2** | Months 7–12 | Intelligence: RAG + Forecasting + Anomaly detection | ⏳ Upcoming |
| **Module 3** | Months 13–18 | Agentic: Multi-step reasoning + Report generation | ⏳ Upcoming |
| **Module 4** | Months 19–24 | Production: MLOps + SaaS deployment + Dissertation | ⏳ Upcoming |

---

## 🎯 Evaluation Milestones

| Evaluation | Month | Release | Key Deliverable |
|------------|-------|---------|-----------------|
| Eval 1 | 6 | v1.0 | Working NL→SQL chatbot demo |
| Eval 2 | 12 | v2.0 | Full analyst with forecasting |
| Eval 3 | 18 | v3.0 | Autonomous agent + auto-reports |
| Eval 4 | 24 | v4.0 | Production SaaS + dissertation |

---

## 🛠 Tech Stack

| Layer | Technologies |
|-------|-------------|
| LLM & Agents | GPT-4o / Mistral, LangChain, LlamaIndex |
| ML Models | Prophet, LSTM, Isolation Forest, scikit-learn |
| Vector Store | Pinecone / Weaviate |
| Backend | FastAPI, SQLAlchemy, Pydantic, Redis |
| Frontend | React 18, TypeScript, Chart.js, Plotly |
| Data | PostgreSQL, MongoDB, Apache Airflow, dbt, S3 |
| MLOps | MLflow, Docker, Kubernetes, GitHub Actions |
| Cloud | AWS (SageMaker, RDS, S3) / GCP (Vertex AI) |

---

## 📊 Experiment Tracking

All ML experiments are logged in MLflow. To launch the MLflow UI:

```bash
mlflow ui --port 5000
```

---

## 📖 Documentation

Full documentation is in the [`/docs`](./docs/) folder:

- [Architecture Overview](./docs/architecture/overview.md)
- [API Reference](./docs/architecture/api.md)
- [Data Dictionary](./docs/architecture/data_dictionary.md)
- [ADR Log](./docs/adr/)
- [Runbooks](./docs/runbooks/)

---

## 🧪 Testing

```bash
pytest tests/ --cov=backend --cov-report=html
```

Target: ≥ 80% code coverage maintained throughout all modules.

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

## 👤 Author

**Geetha Vegesna**
- GitHub: [@GeethaVegesna1910](https://github.com/GeethaVegesna1910)
- Project Supervisor: [Supervisor Name, Institution]

---

> *"The goal is to turn data into information, and information into insight."* — Carly Fiorina
