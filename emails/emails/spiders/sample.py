
import scrapy
from scrapy.spiders import CrawlSpider,Request
import re
from googlesearch import search
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time
os.chdir('C:/Users/Faizan/Desktop/WEBSCRAPING-MINIPROJECT/emails/emails/spiders')
domain_names=pd.read_excel('texts.xlsx')
print("running1")
domains=domain_names['URL']
domain_list=[]
for dm in domains:
    domain_list.append(dm)
for dl in domain_list:
    print(dl)

    class email_extractor(CrawlSpider):
        name="sample3"
        def __init__(self, *args, **kwargs):
            super(email_extractor,self).__init__(*args, **kwargs)
            self.emaillist=[]
        def start_requests(self):
            for results in search(dl,num=10,stop=50,pause=2):
                yield SeleniumRequest(
                    url=results,
                    callback=self.parse,
                    wait_until=EC.text_to_be_present_in_element(
                        (By.TAG_NAME,"html")),
                    dont_filter=True
            )
        print("searching",dl)
        def parse(self,response):
            EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+',
            emails = re.finditer(EMAIL_REGEX, str(response.text))
            for email in emails:
                self.emaillist.append(email.group())
            for email in set(self.emaillist):
                yield{
                    "emails":email
                }
            self.emaillist.clear()  
    
            



