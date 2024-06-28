import requests 
from bs4 import BeautifulSoup
import datefinder 
from urllib.request import urlopen
from selenium import webdriver
from datetime import datetime

driver = webdriver.Chrome()
url = "https://indianbank.in/departments/deposit-rates/"
bcode = 105

def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find("div", class_="wow zoomIn")
        # print(info)
        content = info.find_all("strong")
        print(content)
        cn = ""
        for i in content[2]:
            cn += i.text 
        
        dates = datefinder.find_dates(cn)
        redate = ""
        for  date in dates:
            date_val = date.strftime("%d/%m/%y")
            redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")

        driver.quit()
        return redate , bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)