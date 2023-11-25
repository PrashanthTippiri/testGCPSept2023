import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/kotte/TrainingsSept/septgcppractice-bq-sa.json"

client = bigquery.Client()

sql_query = """
SELECT * FROM `septgcppractice.test_gcpsetpt2023_ptdatahub.test-sept2023-ptdatahub-mkr1` 
LIMIT 50
"""

query_job = client.query(query=sql_query)

for row in query_job.result():
    print(row[0])