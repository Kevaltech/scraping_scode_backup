import requests 
from bs4 import BeautifulSoup
import datefinder 
from selenium import webdriver
from urllib.request import urlopen 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
driver = webdriver.Chrome()
url = "https://www.ujjivansfb.in/support-interest-rates#saving-inter"
bcode = 309
def get_date():

    try:
        # res = requests.get(url, verify=False)
        driver.get(url)
        # if res.status_code==200:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find("div", id = "tabone")
        content = info.find_all('p')
        # print(content)
        cn = ""
        for i in content:
            cn += i.text 
        
        dates = datefinder.find_dates(cn)
        readate = ""
        for date in dates:
            readate = date.strftime("%d-%b-%y")
        driver.quit()
        return readate , bcode

        # else:
        #     return ""
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)