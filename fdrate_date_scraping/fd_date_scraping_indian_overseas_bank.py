import requests 
from bs4 import BeautifulSoup
import datefinder 
from urllib.request import urlopen 
from selenium import webdriver


driver = webdriver.Chrome()
url ='https://www.iob.in/Domestic_Rates'
bcode = 106

def get_date():
    try:

        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find('div', id='ctl00_ContentPlaceHolder1_extradiv')
        # print(info)
        content = info.find_all("td")
        # print(content)
        cn = ''
        cnt = 0
        for i in content[1]:
            cn += i.text 
        dates = datefinder.find_dates(cn)
        redate = ""
        for date in dates:
            if cnt==0:
                cnt += 1
                continue
            redate += date.strftime("%d-%b-%y")

        driver.quit()
        return redate , bcode
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)