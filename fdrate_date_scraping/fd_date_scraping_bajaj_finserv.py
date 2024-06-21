import requests
from bs4 import BeautifulSoup
import datefinder
from urllib.request import urlopen

url = "https://www.bajajfinserv.in/investments/fixed-deposit-application-form?&utm_source=googlesearch_mktg&utm_medium=cpc&PartnerCode=76783&utm_campaign=WPB_FD_11022021_RM_BP_RLSA_Des_Exact_Pan_India&utm_term=bajaj%20finance%20fd&device=c&utm_location=9303277&utm_placement=&gad_source=1&gclid=CjwKCAjw17qvBhBrEiwA1rU9w5V2X5cx9rdNIzUpoiH7-bMBNsYD2A7djoFx-GvfpbLOuSMTd_li7xoCm8UQAvD_BwE"
bcode = 501
def get_date():
    try:
        res = requests.get(url)

        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find("div", class_="table-card__desc-text")
            content = info.find_all("p")
            cn = ""
            # print(content)
            for i in content[0]:
                cn += i.text
            dates = datefinder.find_dates(cn)

            redate = ""
            cnt = 0
            for date in dates:
                if cnt>1:
                    redate += date.strftime("%d-%b-%y")
                cnt += 1

            return redate,bcode
        
        else:
            return "",bcode
        
    except:
        return "",bcode
    
# ans = get_date()
# print(ans)