import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import datefinder 
from selenium import webdriver
url = "https://nesfb.com/Interest_Rates"
bcode = 306
driver = webdriver.Chrome()


def get_date():
    
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find("div", class_="acc_head")
        # print(info)
        content = info.find_all("p")
        # print(content)
        cn = ""
        for i in content[0]:
            cn += i.text
        dates = datefinder.find_dates(cn)
        redate = ""
        for date in dates:
            redate = date.strftime("%d-%b-%y")

        driver.quit()
        return redate , bcode
    except:
        return "", bcode

# ans = get_date()
# print(ans)