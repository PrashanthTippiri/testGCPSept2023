from google.cloud import bigquery

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/kotte/TrainingsSept/septgcppractice-bq-sa-new-2211.json"

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "test_gcpsetpt2023_ptdatahub.test-sept2023-ptdatahub-dept"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("deptName", "STRING"),
        bigquery.SchemaField("deptId", "Integer"),
        bigquery.SchemaField("Location", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://pt-datahub-technologies-sept-staging/dept_24112023.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))