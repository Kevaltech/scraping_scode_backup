from bs4 import BeautifulSoup
import requests
import datefinder

url = "https://www.axisbank.com/savings-accounts-interest-rate-structure"
bcode = 200

def get_date():
    try:
        response = requests.get(url)
        if response.status_code==403:
            return "403", url
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            content = soup.find('div', class_="tableWrapper intTable")
            cn = content.find_all("th")
            info = ""
            for i in cn:
                info += i.text 
            dates = datefinder.find_dates(info)
            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            return redate, bcode

        else:
            return "", bcode
    except:
        return "", bcode