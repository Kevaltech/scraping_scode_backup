import requests
import datefinder
from bs4 import BeautifulSoup

url = 'https://www.deutschebank.co.in/en/advantage-banking/fixed-deposit-overview/resident-fixed-deposits.html#parsys-columncontrol_copy-columnControlCol1Parsys-accordion-accordionParsys-accordionentry_copy'
bcode  = 402

def get_date():
    try:
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            info = soup.find('div', id='ae-parsys-columncontrol_copy-columnControlCol1Parsys-accordion-accordionParsys-accordionentry_copy')
            content = info.find_all('p')
            cn = ''
            for i in content[0]:
                cn += i.text
            dates = datefinder.find_dates(cn)

            redate = ''
            for date in dates:
                redate += date.strftime('%d-%b-%y')
            return redate, bcode
        else:
            return "", bcode
        
    except:
        return "", bcode
    
# print(get_date())