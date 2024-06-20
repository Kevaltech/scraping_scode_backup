import requests
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen

url = "https://www.jkbank.com/others/common/intrates.php"
bcode = 212
def get_date():

    try:

        res = requests.get(url)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find('div', id="accordion1_1")
            # print(info)
            content = info.find_all('strong')
            # print(content)
            cn = ""
            for i in content[0]:
                cn += i.text
            dates = datefinder.find_dates(cn)
            redate = ""
            cnt = 0
            for date in dates:
                if cnt==0:
                    cnt+=1 
                    continue
                redate += date.strftime("%d-%b-%y")
            return redate, bcode
        
        else:
            return "", bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)