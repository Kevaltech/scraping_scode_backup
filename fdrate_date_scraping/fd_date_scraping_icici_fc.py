import requests
from bs4 import BeautifulSoup
import datefinder  

from urllib.request import urlopen

url = "https://www.icicihfc.com/fixed-deposit"
bcode = 502
def get_date():
    try:
        res = requests.get(url)

        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find('div', class_="rteTable")
            content = info.find_all('td', {"colspan":"5","style":"text-align: center;"})
            # print(content)
            cn = ""
            for i in content:
                cn+=i.text 
            # print(cn)
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