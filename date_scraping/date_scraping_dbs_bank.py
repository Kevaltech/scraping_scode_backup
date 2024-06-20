import requests
from bs4 import BeautifulSoup
import datefinder

url = 'https://www.dbs.com/digibank/in/rates-and-fees.page'
bcode = 401
def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403", bcode
        soup = BeautifulSoup(response.content, "html.parser")
        cn = soup.find('ol', class_="footNote")
        content = cn.find_all('li')
        info = ""
        for i in content[0]:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        return redate, bcode
    
    except:
        return "", bcode
    
# val = get_date()
# print(val)