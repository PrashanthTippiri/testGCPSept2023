from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/kotte/TrainingsSept/septgcppractice-bq-sa-new-2211.json"

bq_query = """
SELECT * FROM `septgcppractice.test_gcpsetpt2023_ptdatahub.test-sept2023-ptdatahub-mkr1` 
LIMIT 1000
"""

client = bigquery.Client()
final_result = client.query(query=bq_query).result().to_dataframe()

#for row in final_result:
#    print(row[0])

print(final_result)