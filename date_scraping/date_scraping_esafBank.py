from bs4 import BeautifulSoup 
import requests
import datefinder
import html2text
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.esafbank.com/interest-rates/"
bcode = 303

def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table_info = soup.find("div", class_="panel-body")
        # print(table_info)
        info = table_info.find_all('strong')
        # print(info)
        information =""
        for i in info[4]:
            information += i.text 
        dates = datefinder.find_dates(information)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")

        driver.quit()
        return redate, bcode
    except:
        return "", bcode
    
# print(get_date())