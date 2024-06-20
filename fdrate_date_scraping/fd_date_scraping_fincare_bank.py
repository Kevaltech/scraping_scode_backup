import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datefinder 

url = "https://fincarebank.com/interest-rate"
bcode = 304
def get_date():

    try:
        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info= soup.find('table', class_="rates-and-charges-table accordion-third")
            # print(info)
            content = info.find_all("th", {"scope": "col"})
            # print(content)
            cn = ""
            for i in content[1]:
                cn+=i.text  
            
            dates  = datefinder.find_dates(cn)

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