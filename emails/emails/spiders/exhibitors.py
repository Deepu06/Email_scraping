
from bs4 import BeautifulSoup
import requests
import xlsxwriter as xs

import os

class Main:
    url = "https://www.interphex.com/en-us/show-info/exhibitor-list.html"

    

    def request(url):
        os.chdir('C:/Users/Faizan/Desktop/FAIZAN/PROJECTS')
        abs_paths = requests.get(url).text
        soup = BeautifulSoup(abs_paths, 'html.parser')
        list_w=soup.find_all('div',class_="list-wrapper")
        print(list_w)

           
            
        
            
    request(url)
