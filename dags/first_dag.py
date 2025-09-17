from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.empty import EmptyOperator

# Define DAG
with DAG(
    dag_id="testing_first_dag",
    start_date=datetime(2023, 1, 1),   # any past date
    schedule_interval="@daily",        # runs once a day
    catchup=False,                     # don't run for past dates
    tags=["example"],
) as dag:

    # Define a simple task
    hello_task = BashOperator(
        task_id="say_dag",
        bash_command='echo "Hello, Airflow!"')


    start = EmptyOperator(task_id="start")
    middle = EmptyOperator(task_id="middle")
    end = EmptyOperator(task_id="end")

    start>>hello_task>>middle>>end

