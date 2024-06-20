from bs4 import BeautifulSoup
import requests
import datefinder 
import urllib3 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://www.dhanbank.com/interest-rates/"
bcode = 205

def get_date():
    try:
        response = requests.get(url, verify=False)
        if response.status_code==403:
            return "403", bcode
        if response.status_code==200:
            soup = BeautifulSoup(response.content, "html.parser")
            cn = soup.find("div", class_="tabsThree_service_list___KEhw")
            # print(cn)
            cont = cn.find_all("td", {"colspan":"5"})
            content = cont[3]
            # print(content)
            info = ""
            for i in content:
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

