# Repo structure (3-repo quant lab)

## Intended responsibilities

| Repo | Purpose |
|------|---------|
| **trading-ai-core** | Core Python code: models, execution, risk, sentiment, features, pipelines, portfolio logic. Business logic and strategy implementation. |
| **trading-ai-data** | Data ingest, storage, backfills. Market data connectors, APIs, caching, DuckDB/Parquet artifacts. |
| **trading-ai-infrastructure** | Deployment, config, dashboards, scripts. Docker/Compose, CI/CD, monitoring. |

## Separation rationale

- **core**: Pure trading logic, unit-testable, no infra coupling.
- **data**: Heavy I/O, versioned datasets, separate release cadence.
- **infrastructure**: Environment-specific config and tooling.
