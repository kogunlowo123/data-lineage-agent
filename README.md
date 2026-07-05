# Data Lineage Agent

[![CI](https://github.com/kogunlowo123/data-lineage-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/data-lineage-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Data Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Data lineage tracking agent that maps data flow from source to consumption, traces column-level lineage, detects impact of schema changes, and visualizes data dependency graphs for root cause analysis.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `trace_lineage` | Trace data lineage from a dataset back to its sources |
| `analyze_impact` | Analyze downstream impact of a schema or data change |
| `map_dependencies` | Map data dependencies for a dataset or pipeline |
| `detect_broken_lineage` | Detect gaps or breaks in data lineage chains |
| `generate_lineage_graph` | Generate a visual lineage graph for documentation |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/lineage/trace` | Trace data lineage |
| `POST` | `/api/v1/lineage/impact` | Analyze change impact |
| `GET` | `/api/v1/lineage/dependencies` | Map dependencies |
| `GET` | `/api/v1/lineage/broken` | Detect broken lineage |
| `POST` | `/api/v1/lineage/graph` | Generate lineage graph |

## Features

- Flow Mapping
- Column Lineage
- Impact Analysis
- Dependency Graphs
- Root Cause Tracing

## Integrations

- Openlineage
- Datahub
- Marquez
- Dbt Lineage
- Apache Atlas

## Architecture

```
data-lineage-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── data_lineage_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**OpenLineage + DataHub + dbt Lineage + Marquez**

---

Built as part of the Enterprise AI Agent Platform.
