import requests 
from bs4 import BeautifulSoup
import datefinder

url = "https://www.pnbindia.in/Interest-Rates-Deposit.html"
bcode = 108

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="detail-page")
            content = cn.find_all("strong")
            # print(content)
            info = ""
            for i in content[1]:
                info += i.text
            
            dates = datefinder.find_dates(info)

            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            return redate,  bcode

        else:
            return "",  bcode
    except:
        return "",  bcode