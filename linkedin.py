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
            i=0
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')
                #job title
                job_links = soup.find_all('a', {'class':"result-card__full-card-link"})
                #company name
                find_company = soup.find_all('a', {'class':"result-card__subtitle-link job-result-card__subtitle-link"})
                #location
                location_soup = soup.find_all('span', {'class':"job-result-card__location"})
                #Datetime
                datetime_soup = soup.find_all('time')
                #url
                hyperlink_soup = soup.find_all('a', {'class':"result-card__full-card-link"})

                for i in range(len(job_links)):
                    data_dict['job_title'].append(job_links[i].getText())
                    try:
                        data_dict['company'].append(find_company[i].getText())
                    except:
                        data_dict['company'].append("N/A")
                    try:
                        data_dict['location'].append(location_soup[i].getText())
                    except:
                        data_dict['location'],append("N/A")
                    try:    
                        data_dict['datetime'].append(datetime_soup[i]['datetime'])
                    except:
                        data_dict['datetime'].append("N/A")
                    try:
                        data_dict['url'].append(hyperlink_soup[i].getText())
                    except:
                        data_dict['url'].append("N/A")
                    data_dict['scrapped_date'].append(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
                    i +=1
                
                return(data_dict)
            else:
                return "The link is not giving a 200 status code."