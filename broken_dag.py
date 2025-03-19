from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 18),
    "retries": 1,
}

dag = DAG("broken_dag", default_args=default_args, schedule_interval="@daily")

start = DummyOperator(task_id="start", dag=dag)

print "This is a broken DAG"
