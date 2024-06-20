import requests 
from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import datefinder 

url = "https://www.janabank.com/interest-rates/#retail-fixed-deposits-for-domestic-nro-nre-customers"
bcode = 305

def get_date():
    res=requests.get(url)
    try:
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find('div', id="retail-fixed-deposits-for-domestic-nro-nre-customers")
            content = info.find_all('p')

            cn = ""
            for i in content:
                cn+=i.text 
            
            dates = datefinder.find_dates(cn)

            redate = ""

            for date in dates:
                redate += date.strftime("%d-%b-%y")

            return redate , bcode
        else:
            return "", bcode
    
    except:

        return "", bcode
    
# ans = get_date()
# print(ans)