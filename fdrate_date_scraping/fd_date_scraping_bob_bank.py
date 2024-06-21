import requests 
from bs4 import BeautifulSoup 
import datefinder 
from urllib.request import urlopen 
from selenium import webdriver 
from datetime import datetime

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
from selenium.webdriver.chrome.service import Service as ChromeService
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

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
    