# import des librairies 
from airflow.decorators import dag, task
from datetime import timedelta,datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from requests import get
import json
import pandas as pd

# définition de mon dag
@dag(
    dag_id="import_data",
    schedule_interval="@once",
    start_date=datetime(2023, 7, 11),
    catchup=False,
    dagrun_timeout=timedelta(minutes=10)
)
def extract_to_postgres():
    #tâche 1 creation de la table
    create_drivers_table = PostgresOperator(
        task_id="create_drivers_table",
        postgres_conn_id="tuto_Postgre_connection",
        sql="sql/drivers_table.sql"
    )

    #tâche 2 récupérer des datas via une API
    @task(task_id="get_data_to_local")
    def get_data_to_local():
        #url de la requéte API
        url = "https://data.cityofnewyork.us/resource/4tqt-y424.json"
        response = get(url)
        #récupération des données
        data_json = json.loads(response.content)
        #conversion en dataframe
        df = pd.DataFrame(data_json)
        #enregistrement des données dans un fichier csv
        df.to_csv("/opt/airflow/dags/file/drivers_data.csv", sep=";", escapechar="\\", encoding='utf-8', quoting=1)

    #relation entre mes tâches
    create_drivers_table >> get_data_to_local()

#Appel
extract_to_postgres()

