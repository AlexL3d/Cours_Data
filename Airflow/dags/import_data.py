# import des librairies 
from airflow.decorators import dag
from datetime import timedelta,datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

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

#Appel
extract_to_postgres()

