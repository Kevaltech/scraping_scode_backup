import requests
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen
from datetime import datetime

url = "https://www.cityunionbank.com/deposit-interest-rate"
bcode = 202
def get_date():

    try:

        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", class_="col-sm-10 payments p-0")
            content = info.find_all('h2')
            # print(content)
            cn = ""
            for i in content[0]:
                cn += i.text

            dates = datefinder.find_dates(cn)

            redate = ""
            for date in dates:
                date_val = date.strftime("%d/%m/%y")
                redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")

            return redate, bcode
        else:
            return "", bcode
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)