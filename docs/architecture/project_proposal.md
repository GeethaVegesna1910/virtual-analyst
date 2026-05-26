# Project Proposal

## Virtual Data Analyst Agent
**Author:** Geetha Vegesna
**Supervisor:** [Supervisor Name]
**Institution:** [University / Department]
**Start Date:** [Month Year]
**Duration:** 24 months | 4 evaluation periods

---

## 1. Problem Statement

Business analysts spend an estimated 60–80% of their time on data wrangling and report generation rather than insight generation. Non-technical stakeholders are unable to access data warehouses directly, creating bottlenecks around data teams.

This project builds an AI agent that bridges this gap: a system that takes a natural language business question and returns a data-backed, narrative answer with supporting visualizations — autonomously.

---

## 2. Research Questions

1. Can a fine-tuned LLM achieve ≥80% accuracy on complex multi-table SQL generation over business schemas?
2. Does combining RAG with structured query results improve the factual accuracy of generated insights versus SQL alone?
3. How does a multi-step agentic approach compare to single-shot LLM responses on complex analytical tasks?
4. What hallucination mitigation strategies are most effective for LLM-generated data analysis?

---

## 3. Objectives

- **Module 1:** Build a robust natural language to SQL pipeline with a working chatbot interface
- **Module 2:** Add forecasting, anomaly detection, and RAG-augmented document context
- **Module 3:** Implement a multi-step reasoning agent capable of autonomous report generation
- **Module 4:** Deploy as a secure, multi-tenant SaaS with full MLOps infrastructure

---

## 4. Methodology

### 4.1 Data
- Primary dataset: [Describe business dataset — e.g., e-commerce transactions, financial records]
- Document corpus: internal reports, policy documents for RAG
- Synthetic benchmarks: 50 NL→SQL pairs per complexity tier (simple, medium, complex)

### 4.2 Evaluation Metrics
| Component | Metric |
|-----------|--------|
| Text-to-SQL | Execution accuracy, exact match accuracy |
| RAG | RAGAS: faithfulness, answer relevance, context recall |
| Forecasting | MAPE, RMSE, coverage |
| Anomaly detection | Precision, recall, F1 on labelled anomalies |
| End-to-end | Task completion rate, latency (P50/P95), user satisfaction (5-point scale) |

### 4.3 Baseline Comparisons
- GPT-4o zero-shot vs fine-tuned vs RAG-augmented
- Prophet vs LSTM vs statistical baselines (ARIMA)
- Single-shot LLM vs multi-step agent on complex tasks

---

## 5. Expected Contributions

1. A publicly released, open-source Virtual Analyst codebase
2. A benchmark dataset of 500+ NL→SQL pairs for business analytics (CC-BY licensed)
3. A peer-reviewed paper on hallucination mitigation in LLM-driven data analysis
4. Empirical comparison of agentic vs single-shot architectures for analytical tasks

---

## 6. Timeline Summary

| Period | Months | Milestone |
|--------|--------|-----------|
| Module 1 | 1–6 | Evaluation 1: MVP chatbot (v1.0) |
| Module 2 | 7–12 | Evaluation 2: Full analyst with ML (v2.0) |
| Module 3 | 13–18 | Evaluation 3: Agentic system (v3.0) |
| Module 4 | 19–24 | Evaluation 4: Production + dissertation (v4.0) |

---

## 7. Resources Required

- Cloud compute: AWS EC2 (p3.2xlarge for GPU training, t3.medium for API)
- LLM API budget: ~$200/month (OpenAI GPT-4o)
- Storage: S3 for data lake, RDS PostgreSQL
- Estimated total compute cost: $3,000–$5,000 over 24 months

---

## 8. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| LLM API cost overrun | Medium | Medium | Switch to open-source Mistral for non-critical paths |
| Dataset quality issues | Low | High | Data quality checks in dbt; manual annotation for benchmarks |
| Scope creep | High | Medium | Strict module boundaries; weekly scope review with supervisor |
| Hallucinations in production | Medium | High | Grounding checks, SQL validation, confidence thresholds |
