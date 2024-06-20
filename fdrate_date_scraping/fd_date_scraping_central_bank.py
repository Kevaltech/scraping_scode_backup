import requests 
from bs4 import BeautifulSoup
import datefinder 
from urllib.request import urlopen
from datetime import datetime

url = "https://www.centralbankofindia.co.in/en/interest-rates-on-deposit"
bcode = 104
def get_date():
    try:

        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", class_="node__content clearfix")
            content = info.find_all('u')
            # print(content)
            cn = ""
            for i in content[0]:
                cn += i.text 

            dates = datefinder.find_dates(cn)

            redate = ""
            for date in dates:
                date_val = date.strftime("%d/%m/%y")
                redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")

            return redate , bcode
        else:
            return "", bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)