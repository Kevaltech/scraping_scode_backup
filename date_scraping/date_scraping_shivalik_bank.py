import requests
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://shivalikbank.com/interest-rate#savings-account"
bcode = 307


def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find("div", class_="card-body table_sec")
        content = cn.find_all("h3")
        info = ""
        for i in content:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        driver.quit()
        return redate,  bcode

    except:
        return "",  bcode
    
# print(get_date())