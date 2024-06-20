import requests 
from bs4 import BeautifulSoup 
import datefinder 
from selenium import webdriver

url = "https://www.csb.co.in/interest-rates"
bcode = 203
driver = webdriver.Chrome()

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
                date_val += date.strftime("%d-%b-%y")
            i+= 1
            # print(date)
        driver.close()
        return date_val, bcode
        # else:
        #     return ""
    except:
        return "", bcode
    
# val = get_date()
# print(val)