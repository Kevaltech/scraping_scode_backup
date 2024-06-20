import requests
from bs4 import BeautifulSoup
import datefinder 

url = "https://punjabandsindbank.co.in/content/interestdom"
bcode = 107

def get_date():
    try:
        response = requests.get(url, verify=False)
        if response.status_code==403:
            return "403",bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="responsive-table")
            content = cn.find_all("th")

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