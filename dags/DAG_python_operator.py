from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'MinhThai',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

def greet(name, age):
    print(f"Hello everyone, my name is {name} i am {age} years olds.")

with DAG (
    dag_id = 'DAG_python_operator',
    default_args = default_args,
    description = 'This is direct acyclic graph python operator',
    start_date = datetime(2024, 7, 30, 2),
    schedule_interval = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'task1',
        python_callable = greet,
        op_kwargs = {'name':'Thai', 'age':20}
    )
    task1