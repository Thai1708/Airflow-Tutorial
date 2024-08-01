from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'MinhThai',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG (
    dag_id = "DAG_bash_operator",
    default_args = default_args,
    description = "This is direct acyclic graph with bash operator in airflow",
    start_date = datetime(2024, 7, 30, 2),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = "echo hello world this is task 1"
    )

    task2 = BashOperator (
        task_id = 'task2',
        bash_command = 'echo this is task2, it will be run after task1'
    )

    task3 = BashOperator (
        task_id = 'task3',
        bash_command = 'echo this is task3, it will be run after task1, at the same time task2'
    )

    task1 >> [task2, task3]