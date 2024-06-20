import requests
from bs4 import BeautifulSoup
import datefinder
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json',
    'Connection': 'close'  # This header indicates that the connection should be closed after the response
}

bcode = 220
url = "https://www.yesbank.in/personal-banking/yes-individual/deposits/fixed-deposit"

def get_date():
    try:
        driver.get(url)
        # res.raise_for_status()
        driver.implicitly_wait(10)
        element = driver.find_element(By.ID, "ee36a5c6-88cd-470d-a306-7fa833ba35accustomComponentDiv")
        print(element.text)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        print(soup)
        info = soup.find("div", id="ee36a5c6-88cd-470d-a306-7fa833ba35accustomComponentDiv")
        content = info.find_all("strong")
        # print(content)
        cn = ""
        for i in content:
            cn += i.text 
        # print(cn)
        dates = datefinder.find_dates(cn)
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")

        # driver.quit()
        return redate , bcode
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)