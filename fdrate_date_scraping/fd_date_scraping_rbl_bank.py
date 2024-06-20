import requests
from bs4 import BeautifulSoup
import datefinder

from urllib.request import urlopen

url = "https://www.rblbank.com/interest-rates"
bcode = 217

def get_date():

    try:

        res = requests.get(url)

        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", id="collapse584")
            content = info.find_all("strong")

            cn = ""

            for i in content:
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