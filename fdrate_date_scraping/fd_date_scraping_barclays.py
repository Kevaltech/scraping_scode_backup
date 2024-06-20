import requests
import datefinder
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

url = "https://www.barclays.in/personal-banking/accounts-deposits/term-deposits-account/#interestrates"
bcode = 400
def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        info = soup.find("div", id="multi-tab0")
        content = info.find_all("a")
        cn = content[-1].get("href")
        # print(cn)
        dates = datefinder.find_dates(cn[-17:])
        redate = ""
        driver.close()
        for date in dates:
            redate += date.strftime("%d-%b-%y")
        return redate , bcode
        
        
    except:
        return "", bcode
    
# print(get_date())