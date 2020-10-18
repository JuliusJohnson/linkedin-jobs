#loads data from google cloud storage to bigquery
from google.cloud import bigquery

# Construct a BigQuery client object.
#client_old = bigquery.Client()
client = bigquery.Client.from_service_account_json(json_credentials_path='/home/julius/Documents/programming/python/projects/linkedin_database/dev/linkedin-jobs.json')

# TODO(developer): Set table_id to the ID of the table to create. --done
table_id = "LinkedInJobs.jobs3"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("dailyindex", "INTEGER"),
        bigquery.SchemaField("scrapped_date", "STRING"),
        bigquery.SchemaField("job_title", "STRING"),
        bigquery.SchemaField("company", "STRING"),
        bigquery.SchemaField("location", "STRING"),
        bigquery.SchemaField("datetime", "DATE"),
        bigquery.SchemaField("url", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://dataanalyst/linkedin-export.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))