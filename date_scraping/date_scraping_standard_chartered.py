import requests
from bs4 import BeautifulSoup
import datefinder
import re 
import datetime

url = "https://www.sc.com/in/deposits/interest-rates/"
bcode = 405

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",bcode
        soup = BeautifulSoup(response.content, "html.parser")
        cn = soup.find("div", class_="description")
        # print(cn)
        inf = cn.get_text()
        # print(inf)
        info = ""
        for i in range(0, len(inf)):
            if inf[i]=="‘":
                info=info[:-2]
                info+="."
            else:
                info += inf[i]
        
        # print(info)
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate += date.strftime("%d-%b-%y")

        return redate,  bcode
    except:
        return "",  bcode
    
# val = get_date()
# print(val)