import requests
import datefinder
from bs4 import BeautifulSoup

url = "https://www.hsbc.co.in/accounts/products/fixed-deposits/"
bcode = 404

def get_date():
    try:

        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find('div', id="pp_main_basicTable_1")
            dates = datefinder.find_dates(info.text)
            # print(dates)
            redate = ""
            cnt = 0
            for date in dates:
                redate += date.strftime("%d-%b-%y")
                break
            return redate, bcode  
        else:
            return "", bcode
    except:
        return "", bcode
    
# print(get_date())