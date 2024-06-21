import requests
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver

driver = webdriver.Chrome()

from urllib.request import urlopen

url = "https://www.hdfcbank.com/personal/save/deposits/fixed-deposit-interest-rate"
bcode = 207

def get_date():

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find('div', class_="rates-body")
        content = info.find_all('h3')
        # print(content)
        cn = ""
        for i in content:
            cn += i.text
        dates = datefinder.find_dates(cn)
        redate = ""
        cnt = 0
        for date in dates:
            if cnt==0:
                redate += date.strftime("%d-%b-%y")
                cnt +=1

        driver.quit()
        return redate, bcode
        
        
    except:
        return "", bcode

# ans = get_date()
# print(ans)