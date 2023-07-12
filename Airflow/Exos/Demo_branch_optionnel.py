from airflow import DAG
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from random import randint

#arguments par défaut
default_args = {
    "start_date": datetime(2023, 7, 12),
    "retries": 1
}

#fonction
def mon_eval_model():
    accuracy = randint(0,100)
    print ("accuracy = ", accuracy)
    if accuracy > 85:
        return ["super_accurate", "accurate"]
    elif accuracy > 50:
        return "accurate"
    else :
        return "not_accurate"

#Declaration de mon DAG par contexte
with DAG(
    dag_id="demo_branch_optionnelle",
    schedule="@once",
    catchup=False,
    default_args=default_args
) as dag:
    #tâche 1 : simulation de la création du model
    t1  = DummyOperator(
        task_id="create_model"
    )
    #tâche 2 : branchement sur son évaluation
    choose_best = BranchPythonOperator(
        task_id="choose_best",
        python_callable=mon_eval_model
    )
    #tâche 3 : choix "super accurate" du modèle
    super_accurate = DummyOperator(
        task_id="super_accurate"
        )
    #tâche 4 : choix "accurate" du modèle
    accurate = DummyOperator(
        task_id="accurate"
        )
    #tâche 5 : choix "not accurate" du modèle
    not_accurate = DummyOperator(
        task_id="not_accurate"
        )

    #ordre des tâches
    t1 >> choose_best >> [super_accurate, accurate, not_accurate]