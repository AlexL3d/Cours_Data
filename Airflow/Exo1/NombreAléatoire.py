# Declaration par constructeur

# import des librairies
from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from random import random
from airflow.operators.python_operator import PythonOperator


#fonction de creation du nombre aléatoire
def nb_aléa():
    # génération du nombre aléatoire
    Nb_aléa = random()


def save_infile(file,**context):
    #génération de la date du jour
    daytime = context['execution_date'].strftime('%Y-%m-%d')
    #création du fichier texte avec le nom du jour et du nombre aléatoire
    with open(file, "a") as f :
        f.write(daytime + " : " + str(nb_aléa()) + '\n')


# declaration par constructeur
Dag_Nb_aléa = DAG(
    dag_id="Nombre_Aléatoire",
    start_date=datetime(2023, 7, 1),
    schedule="@daily"
)


# appel d'execution d'une tache dans mon DAG
def mon_Dag():
    #tâche 1 :
    créa = BashOperator(task_id="Task_création_fichier", bash_command="/opt/airflow/dags/script.sh")
    #tâche 2 :
    aléa = PythonOperator(task_id="Task_nb_aléa", dag=Dag_Nb_aléa, python_callable=save_infile("/opt/airflow/dags/file/Dag_Nb_aléa.txt"),provide_context=True)

# Task_création_fichier >> Task_nb_aléa
