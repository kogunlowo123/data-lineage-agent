# Data Lineage Agent Architecture

Data lineage tracking agent that maps data flow from source to consumption, traces column-level lineage, detects impact of schema changes, and visualizes data dependency graphs for root cause analysis.

## Domain Tools

- **trace_lineage**: Trace data lineage from a dataset back to its sources
- **analyze_impact**: Analyze downstream impact of a schema or data change
- **map_dependencies**: Map data dependencies for a dataset or pipeline
- **detect_broken_lineage**: Detect gaps or breaks in data lineage chains
- **generate_lineage_graph**: Generate a visual lineage graph for documentation