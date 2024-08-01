from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'MinhThai',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_infor', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_infor', key='last_name')
    age = ti.xcom_pull(task_ids='get_infor', key='age')
    print(f"Hello everyone, my name is {first_name} {last_name} i am {age} years olds.")

def get_infor(ti):
    ti.xcom_push(key='first_name', value='Thai')
    ti.xcom_push(key='last_name', value='Pham')
    ti.xcom_push(key='age', value=20)

def get_name():
    return 'Thai'

def get_age():
    return 20

with DAG (
    dag_id = 'DAG_python_operator_v_xcom_v02',
    default_args = default_args,
    description = 'This is direct acyclic graph python operator',
    start_date = datetime(2024, 7, 30, 2),
    schedule_interval = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'get_infor',
        python_callable = get_infor
    )

    task2 = PythonOperator(
        task_id = 'greet',
        python_callable = greet
    )

    task1 >> task2