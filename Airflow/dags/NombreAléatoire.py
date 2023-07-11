# Declaration par constructeur

# import des librairies
from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from random import random
from airflow.operators.python_operator import PythonOperator

#fonction de creation du nombre aléatoire
def nb_aléa(**context):
    # génération du nombre aléatoire
    Nb_aléa = random()
    #génération de la date du jour
    daytime = context['execution_date'].strftime('%Y-%m-%d')
    # Définir le chemin du dossier spécifique
    file_path = f'/opt/airflow/dags/Dag_Nb_aléa.txt'
    #création du fichier texte avec le nom du jour et du nombre aléatoire
    with open(file_path, "a") as file :
        file.write(daytime + " : " + str(Nb_aléa) + '\n')

# declaration par constructeur
Dag_Nb_aléa = DAG(
    dag_id="Nombre_Aléatoire",
    start_date=datetime(2023, 7, 1),
    schedule_interval="@daily"
)

# appel d'execution d'une tache dans mon DAG
aléa = PythonOperator(task_id="Task_nb_aléa", dag=Dag_Nb_aléa, python_callable=nb_aléa, provide_context=True)
