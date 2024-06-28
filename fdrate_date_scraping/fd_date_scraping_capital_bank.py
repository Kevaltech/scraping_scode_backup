from selenium import webdriver
import datefinder
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
from selenium.webdriver.chrome.service import Service as ChromeService
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

url = "https://www.capitalbank.co.in/interest-rates/callable-domestic-term-deposit"
bcode = 301

def get_date():

    try:
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "/html/body/section[6]/div/div/div[1]")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # cn = soup.find("div", class_="col-md-12 wow fadeInUp animated animated")
        content = soup.find_all("h3")
        # print(content)
        info = ""
        for i in content[1]:
            info += i.text
        # print(info)
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")
        return redate, bcode

    except:
        return "", bcode    
    
# print(get_date())
