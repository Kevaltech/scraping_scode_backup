import requests
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen 

url = "https://punjabandsindbank.co.in/content/interestdom"
bcode = 107
def get_date():
    try:

        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", class_='middle-content')

            content = info.find_all('th', {"colspan":"2"})

            # print(content)

            cn = ""

            for i in content:
                cn += i.text 
            
            dates = datefinder.find_dates(cn)

            redate = ""

            for date in dates:
                redate += date.strftime("%d-%b-%y")

            return redate,bcode
        else:
            return "",bcode
        
    except:
        return "",bcode
    
# ans = get_date()
# print(ans)