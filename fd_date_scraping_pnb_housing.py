import requests
from bs4 import BeautifulSoup
from datetime import date
from urllib.request import urlopen
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.pnbhousing.com/fixed-deposit/interests-rates"

page = requests.get(url)
bcode = 504
def get_date():

    try:
        driver.get(url)
        # res = requests.get(url)
        # if res.status_code==200:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find("div", class_="lfr-layout-structure-item-27d8d0d2-823b-d018-9d68-d32e980f05e3")
        content = info.find_all("td")
        cn = ""
        for i in content:
            cn += i.text
        update=False
        redate = ""
        with open("pnb.txt", "r") as f:
            file_content = f.read()
            if file_content != cn:
                today = date.today()
                redate += today.strftime("%d-%b-%y")
                update=True
            else:
                return "", bcode
        if update:
            with open("pnb.txt", "w") as f:
                f.write(cn)
            
        return redate, bcode

        # else:
        #     return ""
        
    except:
        return "", bcode
    
# val = get_date()
# print(val)