This project a a demonstration of a rudimentary pipeline. 

Steps:
1. Job Data is scrapped from linkedin using the search query "Data Analyst" on a dialy basis using cron
2. Once the function is run another function combines the daily output into a single file
3. gcp.py runs loads data into the Google Cloud Storage Platform
4. bigquery.py is ran automatically five minues after the completion of gcp.py to transfer the csv file from Google Cloud Storage to Big Query
5. The Data can then be viewed in aggregated form through Google Data Studo (Coming Soon...)