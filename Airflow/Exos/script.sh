if [[ ! -e /opt/airflow/dags/file/Dag_Nb_aléa.txt ]]; then
    mkdir -p "$AIRFLOW_HOME/dags/file"
    touch "$AIRFLOW_HOME/dags/file/Dag_Nb_aléa.txt"
fi