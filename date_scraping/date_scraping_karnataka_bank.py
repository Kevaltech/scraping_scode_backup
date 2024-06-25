from bs4 import BeautifulSoup 
from urllib.request import Request
import requests 
import datefinder
from datetime import datetime

url = "https://karnatakabank.com/savings-account-interest-rates"
bcode = 213



def get_date():
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }
        req = requests.get(url, headers=headers, stream=True)
        if req.status_code==403:
            return "403",  bcode
        # req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
        # response = urlopen(req).read()
        soup = BeautifulSoup(req.content, "html.parser")
        cn = soup.find_all("div", class_="custom-container")
        # print(cn)
        content = cn[1].find_all("h1", {'class':"heading40"})
        # print(content)
        info = ""
        # print(info)
        for i in content:
            info += i.text
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            date_val = date.strftime("%d/%m/%y")
            redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
        # print(date, redate)
        return redate,  bcode
    except:
        return "",  bcode
# val = get_date()
# print(val)