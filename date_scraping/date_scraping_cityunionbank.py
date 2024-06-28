from bs4 import BeautifulSoup
import requests
import datefinder 
from datetime import datetime

url = "https://www.cityunionbank.com/deposit-interest-rate"
bcode = 202
def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403", bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="col-sm-10 payments p-0")
            content = cn.find_all("th", {"colspan": "2"})
            # print(content)
            info = ""
            for i in content[3]:
                info += i.text
            # print(info)
            dates = datefinder.find_dates(info)
            i = 0
            date_value = ""
            for date in dates:
                if i==0:
                    redate = date.strftime("%d/%m/%y")
                    date_value += datetime.strptime(redate, '%m/%d/%y').strftime("%d-%b-%y")
                i += 1 
            return date_value , bcode
        else:
            return "", bcode
    except:
        return "", bcode

# val = get_date()
# print(val)