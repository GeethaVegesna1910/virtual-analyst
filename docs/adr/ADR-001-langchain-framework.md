# ADR-001: Use LangChain as the Agent Framework

**Date:** 2024-01
**Status:** Accepted
**Author:** Geetha Vegesna

## Context

The Virtual Analyst requires a framework to orchestrate LLM calls, manage tools (SQL, RAG, forecast), handle memory, and support multi-step reasoning. Several options were evaluated.

## Options Considered

| Option | Pros | Cons |
|--------|------|------|
| **LangChain** | Mature, large ecosystem, native tool abstraction, LangSmith tracing | Can be verbose; some abstraction overhead |
| **LlamaIndex** | Excellent RAG primitives | Less mature agent/tool layer |
| **Bare OpenAI API** | Full control, minimal overhead | Must re-implement tool calling, memory, retry logic from scratch |
| **AutoGen** | Strong multi-agent patterns | Complex setup; overkill for single-agent v1 |

## Decision

**LangChain** for the core agent executor and tool registry.
**LlamaIndex** for the RAG ingestion pipeline (complementary, not competing).

## Consequences

- Team must stay current with LangChain's rapid release cycle
- LangSmith provides free experiment tracing during development
- Switching cost if LangChain becomes unsuitable is moderate (tool interfaces are well-abstracted)

## Review Date

End of Module 1 (Month 6). If accuracy targets are not met, re-evaluate bare API approach.
