
from bs4 import BeautifulSoup
from selenium import webdriver
import datefinder
from selenium.webdriver.common.by import By
from datetime import datetime
driver = webdriver.Chrome()
bcode = 503
def get_date():
    try:
        driver.implicitly_wait(20)
        driver.get("https://www.lichousing.com/public-deposits")
        driver.find_element(By.CSS_SELECTOR, "div.sc-cnEclw")
        soup = BeautifulSoup(driver.page_source, "lxml")
        # print(soup)
        # cn = soup.find("div", class_="col-xs-12")
        # print(soup)
        content = soup.find_all("b")
        # print(content)
        info = ""
        for i in content[0]:
            info += i.text

        dates = datefinder.find_dates(info)
        redate = ""
        cnt = 0
        for date in dates:
            # print(date)
            if cnt==2:
                date_val = date.strftime("%d/%m/%y")
                redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
            cnt+=1
        # driver.close()
        driver.quit()
        return redate, bcode
    except:
        return "", bcode

# val = get_date()
# print(val)