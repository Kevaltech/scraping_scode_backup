import requests
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome()

url = "https://indianbank.in/departments/deposit-rates/#!"
bcode = 105

def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find("div", class_='wow zoomIn')
        content = cn.find_all('p')
        info = ""
        for i in content[-6]:
            info += i.text 
        dates = datefinder.find_dates(info)

        redate = ""
        for date in dates:
            date_val = date.strftime("%d/%m/%y")
            redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
        driver.quit()
        return redate, bcode

    except:
        return "", bcode
     
# print(get_date())