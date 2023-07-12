from airflow.decorators import dag, task
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Création d'une tâche réutilisable
@task
def addition(x,y):
    print(f'Addition de {x} et {y} = {x+y}')
    return x+y

# définition du DAG
@dag(
    dag_id='reusable_task',
    start_date=datetime(2023, 7, 12),
    schedule_interval='@daily',
)
def reusable_dag():
    # premier appel de la tâche addition
    debut = addition.override(task_id='debut')(1,2)
    #boucle d'appel de la tâche addition
    for i in range(10):
        debut >> addition.override(task_id=f'addition_{i}')(debut,i)

# appel de mon dag
reusable_dag()