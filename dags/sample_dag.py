from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from sqls.etl import insert_customers

# Define DAG
with DAG(
    dag_id="sample_dag",
    start_date=datetime(2023, 1, 1),   # any past date
    schedule_interval="@daily",        # runs once a day
    catchup=False,                     # don't run for past dates
    tags=["example"],
) as dag:

    # Define a simple task
    hello_task = BashOperator(
        task_id="say_dag",
        bash_command='echo "Hello, Airflow!"')
    
    read_table = SQLExecuteQueryOperator(
        task_id="read_table",
        conn_id = "analytics",
        sql = "select * from users_customer"
        
    )
    
    insert_task = SQLExecuteQueryOperator(
        task_id="insert_task",
        conn_id = "analytics",
        sql = insert_customers
        
    )


    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    
    start>>hello_task>>read_table>>insert_task>>end

