import pandas as pd 
from datetime import datetime, timedelta, date
from airflow import DAG
from desafioAirflow.scripts.teste import *
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.utils.edgemodifier import Label
from textwrap import dedent

default_args = {
	'owner':'airflow',
	'retries': 1,
	'retry_delay':timedelta(minutes=1)
}
    
def export_final_answer():
    import base64

    # Import count
    with open('dags/desafioAirflow/data/count.txt') as f:
        count = f.readlines()[0]

    my_email = Variable.get("my_email")
    message = my_email+count
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    with open("dags/desafioAirflow/data/final_output.txt", "w") as f:
        f.write(base64_message)
    return None




with DAG(
	'DesafioAirflow',
	default_args = default_args,
#	dag_id = 'DesafioAirflow',
	description = 'step1_techinical_challenge',
	start_date = datetime(2022, 7,13),
	schedule_interval = '@daily',
	catchup = False

) as dag:


# task que le a tabela Order do banco de dados
	task1 = PythonOperator(
		task_id = 'task1',
		python_callable = read_order,
		provide_context=True
)

#task que le a tabela OrderDetail do banco, realiza um join e soma as quantidades
	task2 = PythonOperator(
		task_id = 'task2',
		python_callable = read_orderDetail,
		provide_context=True
)

#task do email
	task3 = PythonOperator(
		task_id = 'task3',
		python_callable = export_final_answer,
		provide_context=True
)

#ordem das tasks
task1>>task2>>task3