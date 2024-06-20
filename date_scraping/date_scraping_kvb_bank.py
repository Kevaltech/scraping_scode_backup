from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import datefinder

driver = webdriver.Chrome() 
url = "https://www.kvb.co.in/interest-rates/interest-rate-for-saving-account/"
bcode = 214
def get_date():
    try:
        response = requests.get("https://www.kvb.co.in/interest-rates/interest-rate-for-saving-account/")
        if response.status_code==403:
            return "403",  bcode
        driver.get("https://www.kvb.co.in/interest-rates/interest-rate-for-saving-account/")
        soup = BeautifulSoup(driver.page_source, "lxml")
        cn = soup.find("div", class_="col-xs-12")
        content = cn.find_all("p", {"class": "interest-rate-savings-description"})
        # print(content)
        info = ""
        for i in content:
            info += i.text

        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            # print(date)
            redate += date.strftime("%d-%b-%y")
        driver.close()
        return redate,  bcode
    except:
        return "",  bcode

# val = get_date()
# print(val)