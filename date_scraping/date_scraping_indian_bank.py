import requests
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://indianbank.in/departments/deposit-rates/#!"
bcode = 105

def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find("div", class_='wow zoomIn')
        content = cn.find_all('strong')

        info = ""
        for i in content[3]:
            info += i.text 
        # print(info)
        dates = datefinder.find_dates(info)

        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        driver.quit()
        return redate, bcode

    except:
        return "", bcode
    
# print(get_date())