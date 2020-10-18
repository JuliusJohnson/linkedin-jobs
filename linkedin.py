from bs4 import BeautifulSoup
import json
import requests
from datetime import datetime

class jobs:
    def __init__(self,url):
        self.url = url #"https://www.linkedin.com/jobs/data-analyst-jobs-atlanta-ga?position=1&pageNum=0"
    
    def scrape_site(self):
        data_dict = {'scrapped_date':[], 'job_title':[], 'company':[], 'location': [], 'datetime':[], 'url':[]}
        r = requests.get(self.url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            #job title
            job_links = soup.find_all('a', {'class':"result-card__full-card-link"})
            data_dict['job_title'].extend([t.getText() for t in job_links])
            #company name
            find_company = soup.find_all('a', {'class':"result-card__subtitle-link job-result-card__subtitle-link"})
            data_dict['company'].extend([c.getText() for c in find_company])
            #location
            location_soup = soup.find_all('span', {'class':"job-result-card__location"})
            data_dict['location'].extend([c.getText() for c in location_soup])
            #Datetime
            i = 0
            datetime_soup = soup.find_all('time')
            for datetimes in datetime_soup:
                data_dict['datetime'].append(datetime_soup[i]['datetime'])
                i +=1
            #url
            i = 0
            hyperlink_soup = soup.find_all('a', {'class':"result-card__full-card-link"})
            for link in hyperlink_soup:
                data_dict['url'].append((hyperlink_soup[i]['href']))
                i +=1
            #scrapped_date
            for item in range(len(data_dict['job_title'])):
                data_dict['scrapped_date'].append(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
            return(data_dict)
        else:
            return "The link is not giving a 200 status code."