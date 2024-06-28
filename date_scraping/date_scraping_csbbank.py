import requests 
from bs4 import BeautifulSoup 
import datefinder 
from selenium import webdriver
from datetime import datetime

url = "https://www.csb.co.in/interest-rates"
bcode = 203
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
from selenium.webdriver.chrome.service import Service as ChromeService
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

def get_date():
    try:
        response = requests.get(url)
        driver.get(url)
        # if response.status_code==200:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find('div', class_="tab_content")
        content = cn.find_all("thead")
        info = ""
        for i in content:
            info += i.text 
        # print(info)
        dates = datefinder.find_dates(info)
        i = 0
        date_val = ""
        for date in dates:
            if i==0:
                redate = date.strftime("%d/%m/%y")
                date_val += datetime.strptime(redate, '%m/%d/%y').strftime("%d-%b-%y")
            i+= 1
            # print(date)
        driver.quit()
        return date_val, bcode
        # else:
        #     return ""
    except:
        return "", bcode
    
# val = get_date()
# print(val)