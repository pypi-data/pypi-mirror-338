

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.http.operators.http import HttpOperator
from airflow.utils.task_group import TaskGroup
from utils.notifications import google_chat_notification
from utils.success_log import success_log
from utils.load_tables import download_file_from_gcs, load_tables_to_process
from airflow.models import Variable
from datetime import datetime, timedelta
import google.oauth2.id_token
import google.auth.transport.requests
import requests 



# Obtención de variables de Airflow para configuración del DAG y de los jobs de Dataflow
CONFIG_VARS = {
    'output_bucket_ingest': Variable.get('OUTPUT_BUCKET_INGEST'),                 # Bucket de salida para la capa de ingest
    'output_bucket_raw': Variable.get('OUTPUT_BUCKET_RAW'),                       # Bucket de salida para la capa raw
    'base_path_dataflow_templates': Variable.get('TEMPLATES_PATH'),               # Ruta base donde se encuentran los templates de Dataflow
    'dataflow_workspace_bucket': Variable.get('BUCKET_DF_BATCH'),                 # Bucket de trabajo para Dataflow
    'data_ingest_service_account': Variable.get('SERVICE_ACCOUNT_DATA_INGEST'),   # Service Account utilizada para los jobs de Dataflow
    'subnetwork': Variable.get('SUBNETWORK'),                                     # Subred utilizada por Dataflow
    'network': Variable.get('NETWORK'),                                           # Red utilizada por Dataflow
    'data_ingest_project_id': Variable.get('DATA_INGEST_PROJECT_ID'),             # ID del proyecto donde se ejecuta la ingestión de datos
    'datagov_project_id': Variable.get('DATAGOV_PROJECT_ID'),                     # ID del proyecto Data Governance
    'location': Variable.get('LOCATION'),                                         # Ubicación (región) donde se ejecutan los jobs
    'lakehouse_andes_analitico_project_id': Variable.get('PROJECT_LAKEHOUSE_ID'),           # ID del proyecto Lakehouse Andes
    'lakehouse_andes_ops_project_id': Variable.get('LAKEHOUSE_ANDES_OPS_PROJECT_ID'),
    'env': Variable.get('ENV'),                                                   # Entorno (dev, qa, prd)
    'bucket_schemas_avro': f"schemas_avro_{Variable.get('ENV')}"                        # Bucket donde se almacenan los esquemas Avro
}

# --- Configuración de rutas y constantes específicas ---

# Nombre del DAG (debe ser el mismo nombre del archivo .py)
DAG_NAME = "<NOMBRE_DAG>"  # Reemplazar con el nombre del archivo .py (sin la extensión)

# Fecha de procesamiento (en formato YYYYMMDD)
PROCESS_DATE = datetime.now().strftime('%Y%m%d')


# Programación del DAG (vacío en producción para ejecutar inmediatamente, None en otros entornos para no programar)
SCHEDULE = '' if CONFIG_VARS['env'] == 'prd' else None


# Configuración de rutas y buckets
GCS_BUCKET_NAME = f"resources_config_dag_{CONFIG_VARS['env']}"
GCS_OBJECT_NAME = "path/to/tables_to_process.py"  # Ruta del archivo en el bucket
LOCAL_FILE_PATH = "/tmp/tables_to_process.py"  # Ruta temporal en el sistema local

# Cargar la variable TABLES_TO_PROCESS
download_file_from_gcs(GCS_BUCKET_NAME, GCS_OBJECT_NAME, LOCAL_FILE_PATH)
TABLES_TO_PROCESS = load_tables_to_process(LOCAL_FILE_PATH)





# Argumentos por defecto para el DAG
DEFAULT_ARGS = {
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    "retries": 0,
}



# Definición del DAG de Airflow
with DAG(
    DAG_NAME,                         # Nombre del DAG
    default_args=DEFAULT_ARGS,        # Argumentos por defecto
    schedule_interval=SCHEDULE,       # Programación del DAG
    catchup=False,                    # No ejecutar tareas atrasadas
    tags=[CONFIG_VARS['env'], "api"]         # Etiquetas (tags) del DAG (por ejemplo, el entorno)
) as dag:

    # Tarea inicial (DummyOperator)
    start = DummyOperator(
        task_id='start'
    )

    # Tarea final (DummyOperator)
    end = DummyOperator(
        task_id='end'
    )

    groups = []
    for table in TABLES_TO_PROCESS:
        with TaskGroup(group_id=f"api_to_bq_{table['bigquery_table'].lower()}") as group:

            entorno = table['entorno']
            # Definicion de proyecto de bigquery
            if entorno == 'analitico':
                bigquery_project_id = CONFIG_VARS['lakehouse_andes_analitico_project_id']
                staging_dataset = "staging_dataset"
            elif entorno == 'operacional':
                bigquery_project_id = CONFIG_VARS['lakehouse_andes_ops_project_id']
                staging_dataset = "staging"

            #Variables resources config
            table_name = table['bigquery_table']
            dominio = table['dominio']
            subdominio = table['subdominio']
            producto = table['producto'].replace("/","-")
            origen = table['origen']
            raw_file_path = f"{table['gcs_raw_path']}/{PROCESS_DATE}/{table_name}.avro"
            raw_destination_path = f"{table['gcs_raw_path']}/{PROCESS_DATE}/"
            tabla_staging = f"{bigquery_project_id}.{staging_dataset}.stg_{table_name}"
            tabla_destino = f"{bigquery_project_id}.{table['dataset_destino']}.dep_{table_name}"

            #Autentificacion CloudFunction
            cloudfunction_name = f"cf-{dominio}-{subdominio}-{producto}-{origen}"
            request = google.auth.transport.requests.Request()
            audience = f"https://{CONFIG_VARS['location']}-{CONFIG_VARS['data_ingest_project_id']}.cloudfunctions.net/{cloudfunction_name}"
            TOKEN = google.oauth2.id_token.fetch_id_token(request, audience)

            # Tarea de ingestión (ejecuta cloudfunction que pasa la data de api a GCS en formato Avro)
            ingest = HttpOperator(
                task_id= 'ingest',
                method='POST',
                http_conn_id='http_cloud_function',
                endpoint=cloudfunction_name,
                execution_timeout=timedelta(seconds=90),
                headers={'Authorization': f"Bearer {TOKEN}", "Content-Type": "application/json"},
                on_failure_callback=google_chat_notification,
            )


            # Tarea de copia del archivo Avro de la capa ingest a la capa raw
            raw = GCSToGCSOperator(
                task_id=f"raw_{table_name}",
                source_bucket=CONFIG_VARS['output_bucket_ingest'],  # Bucket de origen (capa ingest)
                source_object=f"{table['gcs_ingest_path']}/{table_name}.avro",  # Objeto (archivo Avro) de origen
                destination_bucket=CONFIG_VARS['output_bucket_raw'],  # Bucket de destino (capa raw)
                destination_object=raw_destination_path,  # Objeto (ruta) de destino
                move_object=False,  # No mover el objeto, solo copiarlo
                on_failure_callback=google_chat_notification  # Notificación en caso de falla
            )
            if table['load_mode'] == "full":
                truncate_table = BigQueryInsertJobOperator(
                        task_id='truncate_table',
                        configuration={
                            "query": {
                                "query": f"""
                                    DELETE FROM `{bigquery_project_id}.{table["dataset_destino"]}.dep_{table["bigquery_table"]}`
                                    WHERE TRUE
                                    """,
                                "useLegacySql": False,  # Siempre usar SQL estándar
                            }
                        },
                        location= CONFIG_VARS['location'],  # Cambia a la región de tu BigQuery si es necesario
                        on_failure_callback=google_chat_notification  # Notificación en caso de falla
                )

            # Tarea de depuración (ejecuta el job de Dataflow para cargar datos desde GCS a BigQuery)
            insert_to_bq = BigQueryInsertJobOperator(
                task_id=f'avro_to_bq_{table_name}',
                configuration={
                    "load": {
                        "sourceUris": [f"gs://{CONFIG_VARS['output_bucket_raw']}/{raw_file_path}"],
                        "destinationTable": {
                            "projectId": bigquery_project_id,
                            "datasetId": staging_dataset,
                            "tableId": f"stg_{table_name}",
                        },
                        "sourceFormat": "AVRO",
                        "writeDisposition": "WRITE_TRUNCATE"
                    }
                },
                location=CONFIG_VARS['location'],
                on_failure_callback=google_chat_notification  # Notificación en caso de falla
            )

             # Tarea para realizar el upsert en caso de aplicar 
            merge_table = BigQueryInsertJobOperator(
                task_id=f"merge_table_{table_name}",  # ID de la tarea, dinámicamente generado
                configuration={
                    "query": {
                        "query": f"CALL `{bigquery_project_id}.{table['dataset_destino']}.{table['store_procedure']}`()",  # Llamada al procedimiento almacenado
                        "useLegacySql": False,  # Usar SQL estándar en lugar de Legacy SQL
                        "priority": "BATCH",  # Prioridad del trabajo en BigQuery
                    }
                },
                location=CONFIG_VARS['location'],  # Ubicación geográfica de BigQuery
                on_failure_callback=google_chat_notification,  # Callback en caso de fallo de la tarea
                on_success_callback=success_log # Callback en caso de exito de la tarea
            )



            audit_merge = BigQueryInsertJobOperator(
                    task_id=f"audit_merge_{table_name}",  # ID de la tarea, dinámicamente generado
                    configuration={
                        "query": {
                            "query": f"""
                                CALL `{bigquery_project_id}.monitoreo.sp_calcular_auditoria`(
                                    '{{{{ task_instance.xcom_pull(task_ids="api_to_bq_{table_name}.merge_table_{table_name}", key="return_value") }}}}',
                                    '{table_name}', 
                                    '{tabla_destino}',
                                    '{tabla_staging}'
                                )
                            """,  # Llamada al procedimiento almacenado
                            "useLegacySql": False,  # Usar SQL estándar en lugar de Legacy SQL
                            "priority": "BATCH",  # Prioridad del trabajo en BigQuery
                        }
                    },
                    location=CONFIG_VARS['location'],  # Ubicación geográfica de BigQuery
                    on_failure_callback=google_chat_notification  # Callback en caso de fallo de la tarea
            )
            
            if table['load_mode'] == "full":
                start >> ingest >> raw >> truncate_table >> insert_to_bq >> merge_table >> audit_merge >> end
               
            else:
                start >> ingest >> raw >> insert_to_bq >> merge_table >> audit_merge >> end

            

    groups.append(group)
