import os
import sys
from airflow.models import Variable

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# from scripts import (
#     upload_to_s3,
#     download_to_mongo
# )

config_vars = Variable.get('config_vars', deserialize_json=True)
S3_BUCKET_NAME = config_vars['S3_BUCKET_NAME']

def upload_amplitude_data():
    # upload_to_s3()
    pass

def download_s3_data():
    # download_to_mongo()
    pass

default_args = {
    'owner': 'Lydia',
    'start_date': datetime(2021, 5, 7),
    'email': 'some@mail.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=20)
}

data_transfer_dag = DAG(
    dag_id='prepare_data_dag',
    default_args=default_args,
    schedule_interval='@daily'
)

t1 = BashOperator(
    task_id='t1',
    bash_command=f'echo {config_vars}',
    dag=data_transfer_dag
)

t2 = BashOperator(
    task_id='t2',
    bash_command='echo {{var.json.config_vars.S3_BUCKET_NAME}}',
    dag=data_transfer_dag
)

t1 >> t2

# upload_amplitude_data_task = PythonOperator(
#     task_id='upload_amplitude_data',
#     python_callable=upload_amplitude_data,
#     dag=data_transfer_dag
# )

# download_s3_data_task = PythonOperator(
#     task_id='download_s3_data',
#     python_callable=download_s3_data,
#     dag=data_transfer_dag
# )

# upload_amplitude_data_task >> download_s3_data_task
