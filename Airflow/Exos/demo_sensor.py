from airflow import DAG
from datetime import datetime
from airflow.sensors.filesystem import FileSensor
from airflow.exceptions import AirflowSensorTimeout
from airflow.operators.python import PythonOperator

# fonction de callback
def _failure_callback(context):
    if isinstance(context['exception'], AirflowSensorTimeout):
        print(context)
        print("sensor timeout")


def _store():
    pass


def _process():
    pass


# déclaration par contexte
with DAG(
    dag_id="demo_sensor",
    schedule_interval="@daily",
    catchup=False,
    start_date=datetime(2023, 7, 12)
) as dag:
    # tâches
    check_parteners = [FileSensor(
        task_id=f'sensor_{partener}',
        filepath=f'partner_{partener}.txt',
        on_failure_callback=_failure_callback,
        poke_interval=120,  # temps entre chaque requête en seconde
        timeout=120,
        mode='reschedule',
        fs_conn_id='partner_data_path'
    ) for partener in ['Jean', 'Jacqueline', 'Karen']]

    # tâche 2
    process = PythonOperator(
        task_id='process',
        python_callable=_process
    )

    # tâche 3
    store = PythonOperator(
        task_id='store',
        python_callable=_store
    )

# appel des tâches
check_parteners >> process >> store
