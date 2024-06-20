from bs4 import BeautifulSoup 
import requests
import datefinder 
from urllib.request import Request, urlopen

url = "https://www.kotak.com/bank/mailers/intrates/get_all_variable_data_latest.php?section=NRO_Term_Deposit"
bcode=215

def get_date():
    try:
        res = Request(url=url, headers={'User-Agen':'Mozilla/5.0'})
        response = urlopen(res).read()
        # if response.status_code==200:
        soup = BeautifulSoup(response, "html5lib")
        cn = soup.find_all("td")
        # print(cn)
        info = ""
        for i in cn[0]:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        return redate, bcode

        # else:
        #     return "453"
    except:
        return "", bcode

# ans = get_date()
# print(ans)