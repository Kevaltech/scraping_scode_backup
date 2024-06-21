import requests 
from bs4 import BeautifulSoup
import datefinder 
from pypdf import PdfReader
import io
from selenium import webdriver
from urllib.request import urlopen

driver = webdriver.Chrome()
url = "https://www.axisbank.com/interest-rate-on-deposits"
bcode = 200
def get_date():

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # print(soup)
        info = soup.find("div", class_="intDeposit")
        content = info.find_all("a")
        # print(content)
        link = content[2]['href']
        # print(link)
        # driver.quit()
        res = requests.get(f"https://www.axisbank.com{link}")
        with io.BytesIO(res.content) as f:
            pdf = PdfReader(f)
            page = pdf.pages[0]
            text = page.extract_text()
            # print(text[530:570])
            dates = datefinder.find_dates(text[530:570])
            redate = ""
            for date in dates:
                redate += date.strftime("%d-%b-%y")

        driver.quit()
        return redate ,bcode
    except:
        return "",bcode
    
# ans = get_date()
# print(ans)