import requests
from bs4 import BeautifulSoup
import datefinder 
from selenium import webdriver
from urllib.request import urlopen

driver = webdriver.Chrome()

url = "https://www.idfcfirstbank.com/interest-rate"
bcode=210

def get_date():

    try:

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find('div', class_="tabs-data op1")
        content = info.get_text()
        # print(content, "*****")
        cn = ""
        for i in content[140:167]:
            cn += i
        # print(cn)
        dates = datefinder.find_dates(cn)
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")

        driver.quit()
        return redate, bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)