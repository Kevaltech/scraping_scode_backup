from bs4 import BeautifulSoup 
import requests
import datefinder

url = "https://www.indusind.com/in/en/personal/rates.html"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

bcode = 211
# print(response)
# print(response.status_code)
# if response.status_code==200:
def get_date():
    try:
        response = requests.get(url,  headers=header)
        if response.status_code==403:
            return "403",  bcode
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find_all("h2", {"class":"text-primary text-bold pb-2 pb-sm-2 pb-md-3 pb-lg-3"})
        # print(soup, content)
        info =""
        for i in content:
            info += i.text 

        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        return redate,  bcode
    except:
        return "",  bcode

# else:
# print("url is not responding")