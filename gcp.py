#loads data in to google cloud storage
from google.cloud import storage
from datetime import datetime

getdate = datetime.now().strftime("%Y-%m-%d")
sourceFile = str(f"/home/julius/Documents/programming/python/projects/linkedin_database/export/{getdate}-export.csv")

def upload_blob(bucket_name, source_file_name, destination_blob_name):

    

    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client.from_service_account_json(json_credentials_path='/home/julius/Documents/programming/python/projects/linkedin_database/dev/linkedin-jobs.json')

    #storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

upload_blob("dataanalyst",sourceFile,"linkedin-export.csv")