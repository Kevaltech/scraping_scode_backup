import requests 
from bs4 import BeautifulSoup 
from pypdf import PdfReader
import io
import datefinder 
from urllib.request import urlopen 
from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://www.utkarsh.bank/personal/term-deposits/fixed-deposits"
bcode = 311
def get_date():
    
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        content = soup.find("div", id="interest-rate-tab")
        cn = content.find("p", class_="h5 TTNorms-400 p16")
        val = cn.find_all('a')
        link = val[0]['href']
        res = requests.get(link)
        with io.BytesIO(res.content) as f:
            pdf = PdfReader(f)
            page = pdf.pages[0]
            text = page.extract_text()
            # print(text[224:241])
            dates = datefinder.find_dates(text[224:241])
            redate = ""
            for date in dates:
                redate += date.strftime("%d-%b-%y")
        driver.quit()
        return redate, bcode
    except:
        return "", bcode


# ans = get_date()
# print(ans)