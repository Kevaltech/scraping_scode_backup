import requests
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver
from urllib.request import urlopen

url = "https://www.icicibank.com/personal-banking/deposits/fixed-deposit/fd-interest-rates?ITM=nli_cms_IR_service_charges_fd_premature"
bcode = 208
driver = webdriver.Chrome()

def get_date():

    try:

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find('div', id="container-3b174ca6f9")
        # print(info)
        content = info.find_all('h4')
        # print(content)
        cn = ""
        for i in content[5]:
            cn += i.text
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
