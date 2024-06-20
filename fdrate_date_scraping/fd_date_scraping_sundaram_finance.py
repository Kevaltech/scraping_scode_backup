import requests
import datefinder
from bs4 import BeautifulSoup

from urllib.request import urlopen

url = "https://www.sundaramfinance.in/deposits"
bcode=506
def get_date():

    try:
        res = requests.get(url)

        if res.status_code==200:

            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", class_="col-lg-6 pt-2 pt-md-5")
            content = info.find_all("h3", {"class":'page-title text-title'})
            cn = ""
            for i in content[0]:
                cn += i.text
            dates = datefinder.find_dates(cn)
            redate = ""
            for date in dates:
                redate += date.strftime("%d-%b-%y")
            return redate, bcode
        
        else:
            return "", bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)