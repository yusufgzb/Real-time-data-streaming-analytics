from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator

from airflow.utils.dates import days_ago


PROJE_AD = "eloquent-petal-379005"
DB_AD = "analiz"

with DAG(
    dag_id="bigquery_data_load",
    schedule_interval="@hourly",
    catchup=False,
    start_date=days_ago(1)
) as dag:
    load_data = GCSToBigQueryOperator(
        task_id ="load_data",
        bucket = "bigquery_json2/{{ ds }}",
        source_objects=["*"],
        source_format="NEWLINE_DELIMITED_JSON",
        destination_project_dataset_table= f"{PROJE_AD}.{DB_AD}.butunveri",
        create_disposition = "CREATE_IF_NEEDED",
        write_disposition="WRITE_APPEND",
        # WRITE_TRUNCATE
        # WRITE_EMPTY
        gcp_conn_id="gcp_test"
    )
    sorgu ="select * from eloquent-petal-379005.analiz.butunveri where sicaklik > 10"
    
    create_new_table = BigQueryExecuteQueryOperator(
        task_id = "create_new_table",
        sql=sorgu ,
        destination_dataset_table= f"{PROJE_AD}.{DB_AD}.analizli_tablo",
        write_disposition="WRITE_TRUNCATE",
        create_disposition = "CREATE_IF_NEEDED",
        use_legacy_sql=False, 
        gcp_conn_id="gcp_test"


    )
    load_data >> create_new_table