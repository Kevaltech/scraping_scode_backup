import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datefinder 

url = "https://sbi.co.in/web/interest-rates/deposit-rates/retail-domestic-term-deposits"
bcode = 109
def get_date():
    try:

        res = requests.get(url)
        # print(res)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find('div', id="menu_0")
            # print(info)
            content = info.find_all('th')
            # print(content)
            cn = ""

            for i in content[5]:
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