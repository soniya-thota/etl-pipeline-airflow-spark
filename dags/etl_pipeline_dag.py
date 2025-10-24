from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_to_s3

def etl():
    df = extract_data()
    df = transform_data(df)
    load_to_s3(df, 'my-demo-bucket', 'output/final.csv')

with DAG('etl_pipeline_dag',
         start_date=datetime(2025,10,1),
         schedule_interval='@daily',
         catchup=False) as dag:
    run_etl = PythonOperator(task_id='run_etl', python_callable=etl)
