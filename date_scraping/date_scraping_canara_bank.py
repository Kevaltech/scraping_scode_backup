import requests
from bs4 import BeautifulSoup
import datefinder

url = "https://canarabank.com/pages/deposit-interest-rates"
bcode = 103


def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403", bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="col-lg-12 text-sec")
            content = cn.find_all("p")

            info = ""
            for i in content[0]:
                info += i.text
            # print(info)
            dates = datefinder.find_dates(info)
            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            return redate, bcode

        else:
            return "", bcode
    except:
        return "", bcode