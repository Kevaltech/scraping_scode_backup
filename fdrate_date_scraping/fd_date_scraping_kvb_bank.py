from bs4 import BeautifulSoup
from selenium import webdriver
import datefinder

driver = webdriver.Chrome()
bcode = 214
def get_date():
    try:
        driver.get("https://www.kvb.co.in/interest-rates/resident-nro-deposits/")
        soup = BeautifulSoup(driver.page_source, "lxml")
        cn = soup.find("div", class_="col-xs-12")
        content = cn.find_all("p", {"class": "nro-content-above-table"})
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
        return redate, bcode
    except:
        return "", bcode

# val = get_date()
# print(val)