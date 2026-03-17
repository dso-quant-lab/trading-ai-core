# Migration map

Scaffolding for future moves from trading-ai-core into trading-ai-data and trading-ai-infrastructure.

| Old path | Purpose | Target repo | Target folder | Status | Notes |
|----------|---------|-------------|---------------|--------|-------|
| `src/data/` | Data ingest, connectors | trading-ai-data | `src/` or `connectors/` | pending | Keep in core until data repo ready |
| `config/` | Config files | trading-ai-infrastructure | `config/` | pending | Env-specific |
| `dashboards/` | Dashboards | trading-ai-infrastructure | `dashboards/` | pending | |
| `scripts/` | CLI / batch scripts | trading-ai-infrastructure | `scripts/` | pending | Or stay in core if logic-heavy |
| `src/models/` | Model code | trading-ai-core | `src/models/` | stays | |
| `src/execution/` | Execution | trading-ai-core | `src/execution/` | stays | |
| `src/risk/` | Risk | trading-ai-core | `src/risk/` | stays | |
| `src/sentiment/` | Sentiment | trading-ai-core | `src/sentiment/` | stays | |
| `src/features/` | Feature engineering | trading-ai-core | `src/features/` | stays | |
| `src/pipelines/` | Pipelines | trading-ai-core | `src/pipelines/` | stays | |
| `src/portfolio/` | Portfolio | trading-ai-core | `src/portfolio/` | stays | |
| `src/utils/` | Shared utils | trading-ai-core | `src/utils/` | stays | May split later |
