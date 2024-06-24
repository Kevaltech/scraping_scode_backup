import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib.request import Request
import ssl
import datefinder
from selenium import webdriver

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
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
from selenium.webdriver.chrome.service import Service as ChromeService
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

url ="https://www.ujjivansfb.in/support-interest-rates#saving-inter"
bcode = 309

# print(response)
def get_date():
        try:
            ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            ctx.options |= 0x4
            # response = requests.get(url, headers=headers, data=payload)
            # if response.status_code==403:
            #     return "403"
            # req = Request(url)
            # print(req)
            # req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
            # response = urlopen(url, context=ctx).read()
            # if response.status_code==200:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html5lib")
            # print(soup)
            # print(soup)
            cn = soup.find("div", id="tabseven")
            content = cn.find_all('p')
            info = ""
            for i in content[0]:
                info += i.text 
            # print(content)
            dates = datefinder.find_dates(info)
            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            # print(redate)
            driver.quit()
            return redate,  bcode
        except:
            return "",  bcode

# val = get_date()
# print(val)