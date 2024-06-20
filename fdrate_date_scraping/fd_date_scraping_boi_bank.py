import requests 
from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import datefinder 
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
bcode = 101
url = "https://bankofindia.co.in/interest-rate/rupee-term-deposit-rate"
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

def get_date():
    try:
        res = requests.get(url, headers=headers, stream=True)
        # print(res)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            # print(soup)
            info = soup.find("div", class_="table-responsive mb-0")
            content = info.find_all("th", {"class":"th-exchange"})
            # print(content)
            cn = ""
            for i in content[1]:
                cn += i.text 
            
            dates = datefinder.find_dates(cn)

            redate = ""
            cnt = 0
            for date in dates:
                if cnt==0:
                    cnt+=1 
                    continue
                date_val = date.strftime("%d/%m/%y")
                redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
            
            return redate , bcode
        else:
            return "", bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)