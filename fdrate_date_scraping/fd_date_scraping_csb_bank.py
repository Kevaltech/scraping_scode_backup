import requests 
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver
from urllib.request import urlopen
from datetime import datetime
driver = webdriver.Chrome()

url = "https://www.csb.co.in/interest-rates"
bcode = 203

def get_date():

    try:
        driver.get(url)
        res = requests.get(url)
        # if res.status_code==200:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find('div', id="node-158")
        content = info.find_all('th', {"colspan":"3"})
        # print(content)
        cn = ""
        for i in content[1]:
            cn += i.text
        dates = datefinder.find_dates(cn)
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")

        driver.quit()
        return redate, bcode
        # else:
        #     return ""
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)