# ETL Data Pipeline (Python)

A simple end-to-end ETL pipeline that demonstrates how raw data can be extracted, cleaned, transformed, and loaded into analytics-ready tables.

## What this pipeline does
- **Extract** raw CSV files
- **Transform** data using Pandas (cleaning, type fixes, derived columns)
- **Load** clean outputs as CSV files in data/output/

## Repo Structure
- `data/raw/` – raw input CSV files  
- `data/output/` – cleaned outputs (generated)  
- `etl/` – pipeline scripts (extract, transform, load)  
- `run_pipeline.py` – runs the full pipeline end-to-end

## Data Engineering Context
This pipeline mirrors a simplified batch ETL workflow commonly used to prepare event-level data for downstream analytics, dashboards, and SQL-based product analysis.

## How to run
```bash
pip install -r requirements.txt
python run_pipeline.py

