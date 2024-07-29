from airflow.decorators import dag, task
from my_functions.taskflow_api import greet

from datetime import timedelta, datetime

default_args = {
    'owner': 'MinhThai',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id = 'dag_with_taskflow_api_v2',
    default_args=default_args,
    start_date = datetime(2024, 7, 18, 2),
    schedule_interval = '@daily'
)

def hello_world_etl():

    @task()
    def get_name():
        return 'Jerrry'
    
    @task()
    def get_age():
        return 15
    
    greet_task = task()(greet)
    
    name = get_name()
    age = get_age()

    greet_task(name=name, age=age)

greet_dag = hello_world_etl()

