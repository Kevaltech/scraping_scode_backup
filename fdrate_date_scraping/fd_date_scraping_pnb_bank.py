import requests
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen
from datetime import datetime

url = "https://www.pnbindia.in/Interest-Rates-Deposit.html"
bcode = 108
def get_date():
    try:
        res = requests.get(url=url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", id="fa-tab13")
            content = info.find_all("h3", {"class": "tab_btn_sec"})

            # print(content)
            cn = ""
            for i in content[0]:
                cn += i.text 
            
            dates = datefinder.find_dates(cn)

            redate = ""

            cnt = 0
            for date in dates:
                if cnt ==0:
                    cnt +=1 
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