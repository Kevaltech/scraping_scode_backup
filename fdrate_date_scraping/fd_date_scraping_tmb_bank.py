import requests
from bs4 import BeautifulSoup
import datefinder 

from urllib.request import urlopen

url = "https://tmb.in/pages/Deposit-Interest-Rates"
bcode = 219

def get_date():

    try:

        res = requests.get(url)
        # print(res)
        if res.status_code==200:

            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", class_="container-inner")
            # print(info)
            content = info.find_all("strong")
            cn = ""
            # print(content)
            for i in content[4]:
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