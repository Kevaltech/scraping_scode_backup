from bs4 import BeautifulSoup 
import requests
import datefinder
import html2text

url = "https://www.janabank.com/interest-rates/"
bcode = 305

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403",  bcode
        if response.status_code ==200:
            soup = BeautifulSoup(response.content, "html.parser")
            table_info = soup.find("div", class_="accordion-inner panel-body")
            content = table_info.find_all("u")
            info = ""
            for i in content:
                info += i.text 
            dates = datefinder.find_dates(info)
            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            return redate,  bcode
        else:
            return "",  bcode
    except:
        return "",  bcode