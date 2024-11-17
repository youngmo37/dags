from __future__ import annotations
from airflow import DAG
# import random
import sys
import tempfile
from pathlib import Path
import datetime

import pendulum

from airflow.operators.bash import  BashOperator
    
with DAG(
    dag_id="dags_bash_operator_ym",
    schedule="0 0 * * *",
    # schedule="@daily",
    start_date=pendulum.datetime(2024, 11, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2"],
    params={"example_key":"example_value"},
    orientation="TB",
) as dag:
        bash_t1 = BashOperator(
            task_id=" bash_t1",
            bash_command= "echo whoam i",
            # python_callable=lambda: f"branch_{random.choice(options)}",
        )
        bash_t2 = BashOperator(
            task_id=" bash_t2",
            bash_command= "echo $HOSTNAME",
            # python_callable=lambda: f"branch_{random.choice(options)}",
        )
        
        bash_t1 >> bash_t2