import requests 
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen
from datetime import datetime

url = 'https://www.unionbankofindia.co.in/english/interest-rate.aspx'
bcode = 111

def get_date():

    try:
        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", id="fa-tab9")
            content = info.find_all("td", {"class":"fontfamilyarial font12 text"})

            cn = ""
            # print(content)
            for i in content[1]:
                cn += i.text 

            dates = datefinder.find_dates(cn)

            redate = ""
            for date in dates:
                redate += date.strftime("%d-%b-%y")

            return redate ,  bcode
        else:
            return "",  bcode
        
    except:
        return "",  bcode
    
# ans = get_date()
# print(ans)