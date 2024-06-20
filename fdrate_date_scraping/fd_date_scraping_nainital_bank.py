import requests
from bs4 import BeautifulSoup
import datefinder

from urllib.request import urlopen

url = "https://www.nainitalbank.co.in/english/interest_rate.aspx"
bcode=216
def get_date():
    try:
        res = requests.get(url)

        if res.status_code==200:

            soup = BeautifulSoup(res.content, "html.parser")
            # info = soup.find('table', class_="table table-bordered")
            # print(info)
            content = soup.find_all("span", {"style":"COLOR: #ffffff"})
            # print(content)
            cn = ""
            for i in content[0]:
                cn += i.text
            inf = ""
            i=0
            while i<len(cn):
                if cn[i]=='6':
                    inf += '6'
                    i+=2
                    continue
                inf += cn[i]
                i+=1
            dates = datefinder.find_dates(inf)

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