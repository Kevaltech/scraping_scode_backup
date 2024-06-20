import requests
from bs4 import BeautifulSoup
import datefinder


url = "https://theunitybank.com/saving_accounts.html"
bcode = 310

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            # cn = soup.find("div", class_="slide-content")
            # # print(soup)
            # content = cn.find_all("p")
            cn = soup.find_all("p", {"class": "key-differentiators-item"})
            # print(cn)
            info = ""

            for i in cn[6]:
                info += i.text

            # print(info)
            cnt = 0
            numdate= ""

            while(cnt<len(info)):
                if info[cnt]=='3':
                    numdate += info[cnt:]
                    break 
                cnt += 1 
            
            # print(numdate)
            dates = datefinder.find_dates(numdate)

            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            # print(redate)
            return redate,  bcode


        else:
            return "",  bcode
    except:
        return "",  bcode

