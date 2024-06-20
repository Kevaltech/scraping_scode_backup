import requests 
from bs4 import BeautifulSoup 
import datefinder 
from urllib.request import urlopen 
from selenium import webdriver 
import datetime

driver = webdriver.Chrome()

url = "https://www.bankofbaroda.in/interest-rate-and-service-charges/deposits-interest-rates"
bcode = 100
def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find("div", class_="field-heading")
        
        dates = datefinder.find_dates(info.get_text())
        redate = ""
        cnt = 0
        for date in dates:
            if cnt==0:
                cnt +=1
                continue
            date_val = date.strftime("%d/%m/%y")
            redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
        driver.quit()
        return redate ,bcode
    except:
        return "" ,bcode
    
# ans = get_date()
# print(ans)
    

