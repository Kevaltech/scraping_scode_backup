import requests 
import datefinder 
from selenium import webdriver 
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
from bs4 import BeautifulSoup

driver = webdriver.Chrome(options=chrome_options)


url = "https://www.yesbank.in/personal-banking/yes-individual/savings-account/savings-account-interest-rate"
bcode = 220

def get_date():
    try:
        driver.maximize_window()
        driver.get(url)
        # time.sleep(5)
        soup=BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup)
        cn = soup.find("div", id="b556dcb1-a0d3-48d3-b839-176ffb306cefcustomComponentDiv")
        # print(content)
        content = cn.find_all("strong")
        # print(cn, content)
        info = ""
        for i in content:
            info += i.text
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            # print(date)
            redate += date.strftime("%d-%b-%y")
        driver.quit()
        return redate, bcode
    except:
        return "", bcode
    

# print(get_date())    
 
  
   
    
     