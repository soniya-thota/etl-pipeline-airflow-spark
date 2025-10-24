#  ETL Pipeline – Airflow + Spark

## Overview
This project demonstrates a simple end-to-end ETL workflow:
Extract CSV → Transform with Pandas → Load to AWS S3 using Airflow.


## Stack
- Python, Airflow
- Pandas, Boto3
- AWS S3, Great Expectations (for quality checks)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start Airflow locally: `airflow standalone`
3. Check DAG `etl_pipeline_dag` and trigger manually.
