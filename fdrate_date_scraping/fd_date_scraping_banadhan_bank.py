import requests 
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen 

url = "https://bandhanbank.com/rates-charges"
bcode = 201
def get_date():

    try:

        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", id="rccollapseOne3")
            content = info.find_all("p")
            # print(content)
            cn = ""
            for i in content[0]:
                cn += i.text

            dates = datefinder.find_dates(cn)

            redate = ""
            for date in dates:
                redate += date.strftime("%d-%b-%y")

            return redate,bcode
        else:
            return "",bcode
    except:
        return "",bcode
    
# ans = get_date()
# print(ans)