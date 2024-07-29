from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v3',  # Đảm bảo dag_id chỉ chứa các ký tự hợp lệ
    description='This is our third DAG that we write', 
    default_args=default_args,
    start_date=datetime(2024, 7, 16, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hello world, this is the second task, it will run after first task'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hello world, this is the third task, it will run after first task and at the same time task 2'
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)
