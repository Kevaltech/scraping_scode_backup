import requests
from bs4 import BeautifulSoup
import datefinder 

url = "https://www.deutschebank.co.in/en/advantage-banking/regular-savings-account.html"
bcode = 402

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403", bcode
        soup = BeautifulSoup(response.content, "html.parser")
        cn = soup.find_all("span", class_='text__footnote')
        # print(cn)
        # content = cn.find_all('span')
        # print(cn)
        info = ""
        for i in cn[1]:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        inc = 0
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
            inc+=1 
            if inc>0:
                break 
        return redate , bcode
    except:
        return "", bcode
    
# val = get_date()
# print(val)