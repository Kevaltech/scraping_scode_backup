import requests 
from bs4 import BeautifulSoup 
import datefinder 
from urllib.request import urlopen 
from selenium import webdriver 

driver = webdriver.Chrome()

url = "https://www.esafbank.com/interest-rates/"
bcode = 303
def get_date():

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # print(soup)
        info = soup.find('div', class_="panel-group invest-accordion")
        # print(info)
        content = info.find_all('th')
        # print(content)
        val = ""
        for i in content[3]:
            val+= i.text 
        dates = datefinder.find_dates(val) 
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")

        driver.quit()
        return redate , bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)