from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/kotte/TrainingsSept/septgcppractice-bq-sa-new-2211.json"

your_fully_qualified_table_id = "septgcppractice.test_gcpsetpt2023_ptdatahub.test-sept2023-ptdatahub-sal"

client = bigquery.Client()

schema = [
    bigquery.SchemaField("eid", "INTEGER"),
    bigquery.SchemaField("salary", "INTEGER"),
    bigquery.SchemaField("desg", "STRING"),
    ]

table = bigquery.Table(your_fully_qualified_table_id, schema=schema)

table = client.create_table(table)

print(
    f"Created table {table.project}.{table.dataset_id}.{table.table_id} "
    )