import requests
from bs4 import BeautifulSoup
import datefinder

url = "https://bankofmaharashtra.in/interest-rates"
bcode = 102

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="inner_post_content")

            content = cn.find_all("strong")

            info = ""
            for i in content:
                info += i.text 

            dates = datefinder.find_dates(info)
            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            return redate, bcode

        else:
            return "", bcode
    except:
        return "", bcode