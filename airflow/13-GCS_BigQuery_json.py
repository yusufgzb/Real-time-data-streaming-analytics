from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator


PROJE_AD = "steadfast-wares-388305"
DB_AD = "analytics"

with DAG(
    dag_id="bigquery_data_load",
    schedule_interval="@hourly",
    catchup=False,
    start_date=days_ago(1)
) as dag:

    load_data = GCSToBigQueryOperator(
        task_id ="load_data",
        bucket = "airflow11/{{ ds }}",
        source_objects=["*.json"],
        source_format="NEWLINE_DELIMITED_JSON",
        destination_project_dataset_table= f"{PROJE_AD}.{DB_AD}.butunveri",
        create_disposition = "CREATE_IF_NEEDED",
        write_disposition="WRITE_APPEND",
        # WRITE_TRUNCATE
        # WRITE_EMPTY
        gcp_conn_id="gcp_test"
    )
    load_data
