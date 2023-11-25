import sys

# [START storage_create_bucket]
from google.cloud import storage


def create_bucket(bucket_name):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.create_bucket(bucket_name,location="EU")

    print(f"Bucket {bucket.name} created")


# [END storage_create_bucket]

if __name__ == "__main__":
    create_bucket(bucket_name=sys.argv[1])
