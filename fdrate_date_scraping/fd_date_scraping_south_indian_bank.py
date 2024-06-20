import requests 
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver
import datefinder

driver = webdriver.Chrome()
url = "https://www.southindianbank.com/interestrate/interestratelist.aspx"
bcode = 218

def get_date():
    try:
        driver.get(url)
        # if response.status_code==200:
        soup= BeautifulSoup(driver.page_source, "lxml")
        # print(soup)
        cn = soup.find_all("span", class_="table-title")
        # print(cn)
        info = ""
        for i in cn[0]:
            info+=i.text
        dates = datefinder.find_dates(info)

        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        # print(redate)
        driver.close()
        return redate, bcode
                
        # else:
            # return ""

    except:
        return "", bcode

# res = get_date()
# print(res)