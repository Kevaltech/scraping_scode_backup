import requests
from bs4 import BeautifulSoup
import datefinder

url = "https://www.nainitalbank.co.in/english/interest_rate.aspx"
bcode = 216

def get_date():
    try:
        response= requests.get(url, timeout=10)
        if response.status_code==403:
            return "403",bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="heading")
            info = cn.get_text()
            dates = datefinder.find_dates(info)

            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            return redate,  bcode

        else:
            return "",  bcode
    except:
        return "",  bcode