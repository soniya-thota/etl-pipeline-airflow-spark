# Batch ETL Pipeline with Airflow and Spark

## Overview
This project demonstrates an end-to-end batch ETL pipeline for processing structured data using Apache Airflow and Apache Spark. The pipeline extracts raw CSV data, applies transformations, validates data quality, and loads curated output into an S3-style data lake layout.

## Stack
- Python
- Apache Airflow
- Apache Spark
- Pandas
- Boto3
- AWS S3 / S3-style storage
- Great Expectations
- Docker

## Key Features
- Automated batch pipeline orchestration with Airflow DAGs
- Data transformation using Spark and Pandas
- Partitioned output layout for scalable downstream analytics
- Data quality validation using Great Expectations
- S3-style storage design for data lake workflows
- Modular ETL structure for repeatable local development

## Pipeline Flow
Raw CSV Data
→ Extract
→ Transform with Spark / Pandas
→ Validate with Great Expectations
→ Load to S3-style storage
→ Curated Analytics Dataset

## How to Run
1. Install dependencies:
   `pip install -r requirements.txt`

2. Start Airflow locally:
   `airflow standalone`

3. Open the Airflow UI.

4. Trigger the DAG:
   `etl_pipeline_dag`

## Resume Summary
Built a batch ETL pipeline using Airflow and Spark for partitioned data transformation, data quality validation, and scalable S3-style storage.
