from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def push_function(**kwargs):
    # Push giá trị vào XCom
    kwargs['ti'].xcom_push(key='message', value='Hello from push_function!')

def pull_function(**kwargs):
    # Pull giá trị từ XCom
    message = kwargs['ti'].xcom_pull(key='message', task_ids='push_task')
    print(f"Pulled message: {message}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'xcom_example_dag',
    default_args=default_args,
    schedule_interval='@daily',
)

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_function,
    provide_context=True,
    dag=dag,
)

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_function,
    provide_context=True,
    dag=dag,
)

push_task >> pull_task
