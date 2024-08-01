from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'MinhThai',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG (
    dag_id = "DAG_postgres_operator_v_insert",
    default_args = default_args,
    description = "This is direct acyclic graph with postgres operator in airflow",
    start_date = datetime(2024, 7, 30, 2),
    schedule_interval = '@daily'
) as dag:
    # task1 = PostgresOperator(
    #     task_id = "create_postgres_table",
    #     postgres_conn_id = "airflow_postgres",
    #     sql = """
    #         CREATE TABLE IF NOT EXISTS employees (
    #         id SERIAL PRIMARY KEY,
    #         first_name VARCHAR(50) NOT NULL,
    #         last_name VARCHAR(50) NOT NULL,
    #         email VARCHAR(100) UNIQUE NOT NULL,
    #         hire_date DATE
    #     );
    #     """
    # )

    task1 = PostgresOperator(
        task_id = "insert_thai",
        postgres_conn_id = "airflow_postgres",
        sql = """
            INSERT INTO employees (first_name, last_name, email, hire_date) VALUES
            ('Thai', 'Pham', 'thai.doe@example.com', '2024-01-01')
        """
    )

    task2 = PostgresOperator(
        task_id = "insert_an",
        postgres_conn_id = "airflow_postgres",
        sql = """
            INSERT INTO employees (first_name, last_name, email, hire_date) VALUES
            ('An', 'Pham', 'an.doe@example.com', '2024-01-01')
        """
    )

    task1 >> task2