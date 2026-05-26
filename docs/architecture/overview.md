# Architecture Overview

## System Design — Virtual Data Analyst Agent

### High-Level Flow

```
User (Natural Language Query)
         │
         ▼
  [React Frontend]
         │  HTTP / WebSocket
         ▼
  [FastAPI Gateway]
         │
    ┌────┴────┐
    │  Auth   │  JWT / OAuth2
    └────┬────┘
         │
  [LangChain Agent Executor]
         │
    ┌────┴──────────────────────────────┐
    │          Tool Registry            │
    │  ┌──────────┐  ┌───────────────┐ │
    │  │ SQL Tool │  │ Forecast Tool │ │
    │  └──────────┘  └───────────────┘ │
    │  ┌──────────┐  ┌───────────────┐ │
    │  │ RAG Tool │  │ Anomaly Tool  │ │
    │  └──────────┘  └───────────────┘ │
    └────────────────────────────────┬─┘
                                     │
         ┌───────────────────────────┼──────────────────────┐
         │                           │                      │
   [PostgreSQL]               [Vector DB]           [ML Models]
   (Structured data)          (Pinecone/Weaviate)   (Prophet, LSTM,
                              (Document RAG)         IsolationForest)
```

---

## Components

### 1. Frontend (React + TypeScript)
- Natural language query bar
- Real-time streaming responses via WebSocket
- Charting: Chart.js for time series, Plotly for exploratory visuals
- Auth: JWT stored in HttpOnly cookies

### 2. FastAPI Backend
- Async endpoints for `/query`, `/forecast`, `/anomalies`, `/report`
- LangChain Agent Executor orchestrates multi-step tool calls
- Redis for task queuing on long-running analyses

### 3. Text-to-SQL Module
- LLM receives schema context (table names, columns, sample rows)
- Generates SQL → validates syntax → executes → formats result
- Self-correction loop: on SQL error, re-prompts with error message (max 3 retries)

### 4. RAG Pipeline
- Ingestion: PDF/CSV docs → chunked → embedded → stored in Pinecone
- Retrieval: top-k semantic search → injected into LLM context
- Used to answer questions requiring policy docs, reports, or institutional knowledge

### 5. ML Models
- **Forecasting**: Prophet for trend+seasonality, LSTM for complex patterns
- **Anomaly Detection**: Isolation Forest on key business metrics
- All trained models tracked in MLflow with experiment IDs

### 6. Data Pipeline
- Apache Airflow DAGs for daily ingestion
- dbt for transformation: staging → intermediate → mart layers
- S3 as raw data lake; PostgreSQL as analytics warehouse

### 7. MLOps
- MLflow: experiment tracking, model registry, artifact storage
- Docker Compose for local dev; Kubernetes for production
- GitHub Actions: lint → test → build → deploy on merge to main

---

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| LLM provider | GPT-4o (primary), Mistral (fallback) | Cost/accuracy balance; open-source fallback |
| Vector DB | Pinecone | Managed, low-latency, Python SDK |
| Forecasting | Prophet + LSTM | Prophet for business seasonality, LSTM for complex nonlinear |
| Agent framework | LangChain | Mature ecosystem, tool abstraction |
| DB | PostgreSQL | ACID compliance, strong JSON support |

---

## Security Considerations

- All LLM outputs validated before SQL execution (parameterized queries only)
- PII detection before sending data to external LLM APIs
- RBAC: users only query their tenant's data
- Rate limiting on `/query` endpoint (10 req/min per user)
