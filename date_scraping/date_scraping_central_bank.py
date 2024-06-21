import requests
from bs4 import BeautifulSoup
import datefinder
import urllib3 
from selenium import webdriver

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

driver = webdriver.Chrome()
payload="Branding=BLUELIGHT&SearchFilter.BrandingCode=BLUELIGHT&CpvContainer.CpvIds=&CpvContainer.CpvIds=&SearchFilter.PagingInfo.PageNumber=2&SearchFilter.PagingInfo.PageSize=25"
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



url ="https://www.centralbankofindia.co.in/en/interest-rates-on-deposit"
bcode = 104

# print(response)
def get_date():
    try:
        response = requests.get(url, headers=headers, data=payload, verify=False)
        # if response.status_code==403:
        #     return "403"
        driver.get(url)
        # if response.status_code==200:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find("div", class_="table-parent")
        # print(cn, soup)
        content = soup.find_all("b")
        info = ""
        for i in content[3]:
            info += i.text 
        # print(content)
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            # print(date)
            redate+= date.strftime("%d-%b-%y")
        # print(redate)
        # if redate=="":
        #     return "15-Mar-23"
        driver.quit()
        return redate, bcode


        # else:
        #     return ""
    except:
        return "", bcode

# val = get_date()
# print(val)