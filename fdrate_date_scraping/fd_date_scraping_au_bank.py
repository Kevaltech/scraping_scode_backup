from bs4 import BeautifulSoup
import requests 
import datefinder 
from selenium import webdriver

url = 'https://www.aubank.in/interest-rates/fixed-deposit-interest-rates'
bcode = 300
driver = webdriver.Chrome()
def get_date():
    
    try:
        res = requests.get(url)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        info = soup.find('div', class_="container ratesTable")
        content = info.find_all('strong')
        # print(content)
        val = ""
        for i in content[0]:
            val+= i.text 

        dates = datefinder.find_dates(val) 
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")
        driver.close()
        return redate,bcode
    except:
        return "",bcode

# ans = get_date()
# print(ans)