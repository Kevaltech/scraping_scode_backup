import requests
from bs4 import BeautifulSoup
import datefinder

url = "https://tmb.in/pages/Deposit-Interest-Rates"
bcode = 219

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find('div', class_="main-contentz")

            content = cn.find_all("li")
            info=""
            for i in content[0]:
                info += i.text 
            # print(info, content)
            dates =datefinder.find_dates(info)


        #year is misleading in the module of this bank..
            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
                break
            # print(redate)
            return redate,  bcode

        else:
            return "",  bcode
    except:
        return "",  bcode