import requests
import datefinder
from bs4 import BeautifulSoup

url = "https://www.sc.com/in/deposits/interest-rates/"
bcode = 405

def get_date():
    try:
        page = requests.get(url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            info = soup.find('div', id="table-content-26925-1")
            content = info.find_all('p')
            cn  = ""
            for i in content[0]:
                cn += i.text 
            dates = datefinder.find_dates(cn)
            redate = ""

            for date in dates:
                redate = date.strftime("%d-%b-%y")
            return redate, bcode 
        else:
            return "", bcode
    except:
        return "", bcode
    
# print(get_date())