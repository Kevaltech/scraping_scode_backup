import requests 
from bs4 import BeautifulSoup 
import io 
import datefinder 
from urllib.request import urlopen 
from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://www.utkarsh.bank/personal/term-deposits/fixed-deposits"
bcode = 311
def get_date():
    
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        content = soup.find("div", id="interest-rate-tab")
        cn = content.find("p", class_="h5 TTNorms-400 p16")
        val = cn.find_all('a')
        # print(cn, val)
        link = val[0]['href']
        # print(link[67:71]+'-'+link[72:74]+'-'+link[75:79])
        dates = datefinder.find_dates(link[67:71]+'-'+link[72:74]+'-'+link[75:79])
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")
        driver.quit()
        return redate, bcode
    except:
        return "", bcode


# ans = get_date()
# print(ans)