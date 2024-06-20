import requests 
from bs4 import BeautifulSoup
import datefinder 

url = 'https://www.barclays.in/home/schedule-of-charges-interest-rates/'
bcode = 400
def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403", bcode
        soup = BeautifulSoup(response.content, "html.parser")
        cn = soup.find('div', class_="m-accordion-item__body-content aem-accordion-item__body-content")
        # print(cn)
        content = cn.find_all('u')
        # print(content)
        info = ""
        for i in content[0]:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        redate = ""
        
        for date in dates:
            redate += date.strftime("%d-%b-%y")
        
        return redate , bcode
    except:
        return "", bcode
    
# val = get_date()
# print(val)