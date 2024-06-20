from bs4 import BeautifulSoup 
import requests
import datefinder 
from selenium import webdriver


driver = webdriver.Chrome()
url = "https://www.idfcfirstbank.com/personal-banking/accounts/savings-account/interest-rate#Interest"
bcode =210

def get_date():
    try:
        driver.get(url)
         
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find("div", class_="idfcrte aem-GridColumn aem-GridColumn--default--12")
        content = cn.find_all("b")
        # print(cn, content)
        # print(cn, content)
        info = ""
        for i in content[2]:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")

        driver.quit()
        return redate, bcode
    except:
        return "", bcode
    
# print(get_date())