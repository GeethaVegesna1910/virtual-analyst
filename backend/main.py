"""
Virtual Analyst — FastAPI Backend
Main application entry point.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title="Virtual Data Analyst API",
    description="Natural language analytics powered by LLMs and ML",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str
    session_id: Optional[str] = None
    include_chart: bool = True


class QueryResponse(BaseModel):
    answer: str
    sql: Optional[str] = None
    data: Optional[list] = None
    chart_spec: Optional[dict] = None
    confidence: float


@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """
    Accept a natural language business question and return a data-backed answer.
    Module 1: Basic Text-to-SQL only.
    Module 2+: RAG + forecasting + anomaly detection.
    """
    # TODO: Module 1 — wire up LangChain text-to-SQL agent
    raise HTTPException(status_code=501, detail="Agent not yet implemented — Module 1 in progress")


@app.get("/")
async def root():
    return {
        "message": "Virtual Data Analyst API",
        "docs": "/docs",
        "status": "Module 1 — In Development",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
