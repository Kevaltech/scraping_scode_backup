import requests 
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen 

url = "https://bankofmaharashtra.in/domestic-term-deposits" 
bcode = 102
def get_date():
    try:
        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content,"html.parser")
            info = soup.find("div", class_='inner_post_content')
            # print(info)
            content = info.find_all('h4')

            # print(content)
            cn = ""
            for i in content[0]:
                cn += i.text 
            
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