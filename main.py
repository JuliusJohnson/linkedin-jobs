import time, glob, os, csv, pandas as pd
from datetime import datetime
import gcp, bigquery, linkedin

getdate = datetime.now().strftime("%Y-%m-%d")

def combine_csv():
    extension = 'csv'
    os.chdir("output")
    filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combine_csv = pd.concat([pd.read_csv(f) for f in filenames ])
    combine_csv.drop(['Unnamed: 0','Unnamed: 0'], axis=1, inplace = True)
    combine_csv.to_csv(f"/home/julius/Documents/programming/python/projects/linkedin_database/export/{getdate}-export.csv",index_label="daily_index")

def scraper():
    jobboard = linkedin.jobs("https://www.linkedin.com/jobs/data-analyst-jobs-atlanta-ga?position=1&pageNum=0&f_TP=1&distance=25&sortBy=DD")
    #print(jobboard.url)
    jobs = (jobboard.scrape_site())   
    positions = pd.DataFrame(data=jobs)
    positions.to_csv(f"/home/julius/Documents/programming/python/projects/linkedin_database/output/{getdate}-jobs.csv")

#runs program
print(f"#####{getdate}#####")
scraper()
combine_csv()
sourceFile = str(f"/home/julius/Documents/programming/python/projects/linkedin_database/export/{getdate}-export.csv")
gcp.upload_blob("dataanalyst",sourceFile,"linkedin-export.csv")
bigquery.transfer()