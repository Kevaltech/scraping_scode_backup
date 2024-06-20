import requests
import datefinder
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://in.dohabank.com/personal-banking/deposit-interest-rates/"
bcode = 403
def get_date():
    try:
        res = requests.get(url=url, headers={"user-agent":"Mozilla/5.0"}, timeout=5, verify=False)
        # print(res)
        # if res.status_code==200:
        soup = BeautifulSoup(res.text, 'html.parser')
        info = soup.find('div', class_="artical-body")
        # print(soup, info)
        content = info.find_all('h3')
        # print(content)
        cn = ""
        for i in content[1]:
            cn += i.text 
        dates = datefinder.find_dates(cn)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        return redate, bcode
        # else:
        #     return "", url
        
    except:
        return "", bcode
    
print(get_date())