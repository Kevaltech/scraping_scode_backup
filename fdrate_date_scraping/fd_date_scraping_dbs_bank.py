import requests
import datefinder
from bs4 import BeautifulSoup


url = "https://www.dbs.com/digibank/in/deposit/deposit-type/fixed-deposit"
bcode = 401
def get_date():
    try:
        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, 'html.parser')
            info = soup.find('div', id="DBSBanFixDep_4")

            content = info.find_all('strong')
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
    
# print(get_date())