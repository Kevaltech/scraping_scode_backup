import requests 
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datefinder 
from selenium import webdriver

url = "https://www.hsbc.co.in/accounts/products/savings/#:~:text=Manage%20and%20transact%20on%20your,effective%20from%2013%20September%202021."
bcode = 404

driver = webdriver.Chrome()
def get_date():
    try:
        res = Request(url=url, headers={'User-Agen':'Mozilla/5.0'})
        response = urlopen(res).read()
        # if response.status_code==403:
        #     return "403"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html5lib")
        cn = soup.find("div", class_='sm-12 md-12 lg-8')
        content = cn.find_all("div")
        # print(cn)
        # print(content)
        info = ""
        for i in content[-1]:
            info += i.text
        # print(info)
        dates = datefinder.find_dates(info)

        redate = ""
        inc = 0
        for date in dates:
            if inc==2:
                redate += date.strftime("%d-%b-%y")
            inc+=1
        driver.quit()
        return redate , bcode
    
    except:
        return "", bcode
    
# val = get_date()
# print(val)