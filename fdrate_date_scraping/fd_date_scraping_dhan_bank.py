import requests 
from bs4 import BeautifulSoup
import datefinder 
from urllib.request import urlopen
import urllib3 
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.dhanbank.com/interest-rates/"
bcode = 205

def get_date():
    try:

        res = requests.get(url, verify=False)

        if res.status_code==200:

            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", class_="tabsThree_service_list___KEhw")
            content = info.find_all('strong')
            # print(content)
            cn = ""
            for i in content[14]:
                cn += i.text
            # print(cn)
            dates = datefinder.find_dates(cn)

            redate = ""
            for date in dates:
                date_val = date.strftime("%d/%m/%y")
                redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")

            return redate, bcode
        
        else:
            return "", bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)