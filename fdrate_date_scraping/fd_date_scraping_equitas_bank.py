from bs4 import BeautifulSoup 
import requests 
import datefinder
from selenium import webdriver
import datefinder

driver = webdriver.Chrome()
from urllib.request import urlopen
from requests.adapters import Retry, HTTPAdapter

headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'Accept': '*/*',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'https://uk.eu-supply.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://uk.eu-supply.com/ctm/supplier/publictenders?B=BLUELIGHT',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': 'EUSSESSION=b18ce90d-32b9-429c-8d74-7151a997e8cd'
}


url = "https://www.equitasbank.com/fixed-deposit"
bcode = 302
def get_date():
    try:
        driver.get(url)
        
        res = requests.get(url, allow_redirects=False)
        # print(res.headers)
        soup = BeautifulSoup(driver.page_source, "lxml")
        # print(soup)
        info = soup.find('div', class_="block block-layout-builder block-field-blocknodesavings-salary-current-deposits-field-table-text-collapse")
        content = info.find_all('p')
        val = ""
        # print(content)
        for i in content[0]:
            val+= i.text 
        dates = datefinder.find_dates(val) 
        redate = ""
        cnt=0
        for date in dates:
            if cnt==0:
                cnt +=1
                continue
            redate += date.strftime("%d-%b-%y")

        driver.quit()
        return redate , bcode
    
    # else:
    #     return "Something went wrong"
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)