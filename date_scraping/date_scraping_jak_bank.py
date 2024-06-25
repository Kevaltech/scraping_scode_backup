from bs4 import BeautifulSoup 
import requests
import datefinder
from datetime import datetime

url = "https://www.jkbank.com/others/common/intrates.php"
bcode = 212


def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",  bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="table-responsive")
            content = cn.find_all("strong")
            # print(cn, content)
            info = ""
            for i in content[1]:
                info += i.text 
            
            dates = datefinder.find_dates(info)

            redate = ""
            for date in dates:
                date_val = date.strftime("%d/%m/%y")
                redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
            return redate,  bcode

        else:
            return "",  bcode
    except:
        return "",  bcode