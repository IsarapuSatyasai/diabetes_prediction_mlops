from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'diabetes_model_training',
    default_args=default_args,
    description='A simple DAG to train diabetes model',
    schedule_interval='@daily',
)

def run_preprocessing():
    subprocess.run(['python', '../scripts/data_preprocessing.py'])

def run_training():
    subprocess.run(['python', '../scripts/model_training.py'])

preprocessing_task = PythonOperator(
    task_id='data_preprocessing',
    python_callable=run_preprocessing,
    dag=dag,
)

training_task = PythonOperator(
    task_id='model_training',
    python_callable=run_training,
    dag=dag,
)

preprocessing_task >> training_task