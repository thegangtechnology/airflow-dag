import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="example-dags",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,  # Prevents running past dates
)

EmptyOperator(task_id="task", dag=my_dag)
