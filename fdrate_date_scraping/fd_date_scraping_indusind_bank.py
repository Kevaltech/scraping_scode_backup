import requests
from bs4 import BeautifulSoup
import datefinder 

from urllib.request import urlopen
header = {'User-Agent':'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}


url = "https://www.indusind.com/in/en/personal/rates.html"
bcode = 211
def get_date():

    try:

        res = requests.get(url,headers=header)
        # print(res)
        # if res.status_code==200:
        soup = BeautifulSoup(res.content, "html.parser")
        # print(soup)
        info = soup.find_all('h4')
        # content = info.find_all('h4')
        # print(info)
        cn = ""
        for i in info[0]:
            cn += i.text
        dates = datefinder.find_dates(cn)
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")
        return redate, bcode
        
        # else:
        #     return "565"
    
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)