# Pipelineer

🚀 **Pipelineer** es una herramienta avanzada para la **automatización de flujos de datos**, permitiendo la generación eficiente de esquemas y la orquestación de procesos ETL en entornos de BigQuery y Oracle.

## ✨ Características Principales

- 🔹 **Generación Automática de Esquemas** en formatos Avro, JSON y SQL.
- 🔹 **Creación de Tablas en BigQuery** con soporte para particiones, clustering y etiquetas.
- 🔹 **Extracción de Datos desde Oracle** utilizando **Google Dataflow**.
- 🔹 **Automatización de Flujos** con Apache Airflow.
- 🔹 **Integración con Terraform y GitLab** para despliegue eficiente.
- 🔹 **Soporte para pipelines escalables** en entornos de datos en la nube.

## 🛠 Tecnologías Utilizadas

Pipelineer se integra con las siguientes tecnologías:
- **Google Cloud Platform (GCP)** ☁️
- **BigQuery** 📊
- **Google Dataflow** ⚡
- **Terraform** 📜
- **GitLab CI/CD** 🔄
- **Apache Airflow** 🏗
- **Python** 🐍

## 📥 Instalación

### Opción 1: Instalación desde PyPI
```bash
pip install pipelineer
```

### Opción 2: Instalación desde el código fuente
```bash
git clone https://github.com/tu-repo/pipelineer.git
cd pipelineer
pip install -r requirements.txt
```

## 🚀 Uso

Pipelineer se ejecuta a través de su **interfaz de línea de comandos (CLI)**:

### 🔹 Generar esquemas desde Oracle
```bash
pipelineer make ingest_schemas --input-folder schemas/oracle --avro-output-folder schemas/avsc --json-output-folder schemas/json --sql-output-folder sql/oracle --date-format datetime
```

### 🔹 Generar esquemas desde API (JSON)
```bash
pipelineer make ingest_schemas --api --avro-output-folder schemas/avsc --json-output-folder schemas/json
```

### 🔹 Generar scripts de tablas en BigQuery
```bash
pipelineer make bq_tables --config-folder sql/bigquery/config/ --output-folder sql/bigquery/scripts/create_table --schema-folder schemas/oracle
```

### 🔹 Generar procedimientos almacenados en BigQuery
```bash
pipelineer make bq_store_procedures --output-folder sql/bigquery/scripts/store_procedure/ --schema-folder schemas/oracle
```

### 🔹 Extraer esquemas desde Oracle
```bash
pipelineer make oracle_schemas --output-folder schemas/oracle
```

### 🔹 Generar archivo de procesamiento de tablas
```bash
pipelineer make tables_to_process
```

### 🔹 Generar templates para DAGs de Airflow
```bash
pipelineer make template --type oracle
```

## 📌 Flujo de Trabajo

1️⃣ **Oracle DB** → 2️⃣ **Extracción con Dataflow** → 3️⃣ **Almacenamiento en GCS** → 4️⃣ **Transformación con Airflow** → 5️⃣ **Carga en BigQuery**

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Contacto

📧 **Email:** sebastian.aguilar.sanhueza@gmail.com  


---

🚀 ¡Optimiza tus flujos de datos con **Pipelineer** y lleva la automatización al siguiente nivel!

