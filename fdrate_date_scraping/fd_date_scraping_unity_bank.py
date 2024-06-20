import requests 
from pypdf import PdfReader
import io 
from bs4 import BeautifulSoup 
import datefinder
from urllib.request import urlopen 

url = "https://theunitybank.com/docs/policies/Website-disclosure-Effective-29-Feb-2024.pdf"
bcode = 310
def get_date():
    try:
        res = requests.get(url)

        if res.status_code==200:
            with io.BytesIO(res.content) as f:
                pdf = PdfReader(f)
                pages = pdf.pages[0]
                content = pages.extract_text()
                info = ""
                i = 388
                while(i<404):
                    if content[i]=='n':
                        i += 3
                        info += '-'
                        continue
                    if content[i]==',':
                        i += 2
                        info += '-'
                        continue
                    info += content[i]
                    i += 1
                info.replace(" ", "")
                return info, bcode
                # dates = datefinder.find_dates(info)
                # for date in dates:
                #     print(date)

    except:
        return "", bcode


# ans = get_date()
