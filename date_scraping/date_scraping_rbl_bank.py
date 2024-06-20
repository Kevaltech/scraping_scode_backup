import requests 
from bs4 import BeautifulSoup 
import datefinder 

url = "https://www.rblbank.com/interest-rates"
bcode = 217

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("p", class_="p18 text-level1 mb20 text-center")
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