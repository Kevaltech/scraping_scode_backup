from bs4 import BeautifulSoup 
import requests
import datefinder
from selenium import webdriver
url = "https://nesfb.com/Interest_Rates"
bcode = 306


driver = webdriver.Chrome()
def get_date():
    # try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table_info  = soup.find("div", class_="acc_head")
        content = table_info.find_all("p")
        # print(content)
        # print(content)
        info = ""
        for i in content[0]:
            info += i.text 
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")

        driver.close()
        return redate,  bcode
    


    # except:
    #     return "",  bcode
    
# print(get_date())