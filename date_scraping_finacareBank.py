from bs4 import BeautifulSoup
import requests
import datefinder 
import urllib3
import html2text

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://fincarebank.com/interest-rate"


def get_date():
    try:
        response = requests.get(url, timeout=20, verify=False)
        if response.status_code==403:
            return "403"
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            table_info = soup.find("div", class_="elementor-element elementor-element-2d147610 e-con-full e-flex e-con e-child")
            info = table_info.find_all('th')
            # print(table_info, info)
            information = ""
            for i in info[0]:
                # print(i, i.text)
                information += i.text
            # print(info, information)
            dates = datefinder.find_dates(information)
            redate = ""
            for date in dates:
                redate+= date.strftime("%d-%b-%y")
            return redate
        else:
            return ""
    except:
        return ""

# val = get_date()
# print(val)