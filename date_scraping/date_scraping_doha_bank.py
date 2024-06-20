import requests 
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import datefinder
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://in.dohabank.com/personal-banking/savings-account/#:~:text=With%20savings%20Bank%2C%20Your%20money%20is%20always%20within%20your%20reach.&text=*%20The%203.00%25%20interest%20will%20be,over%20%26%20above%20INR%2050%20lac.'
bcode = 403
def get_date():
    try:
        res = requests.get(url=url, headers={"user-agent":"Mozilla/5.0"}, timeout=5, verify=False)
        # response = urlopen(res).read()
        if res.status_code==403:
            return "403", bcode
        soup = BeautifulSoup(res.content, "html.parser")
        # print(soup)
        cn= soup.find("div", class_="panel active")
        content = cn.find_all('em')
        # print(cn)
        # print(content)
        info = ""
        for i in content[1]:
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