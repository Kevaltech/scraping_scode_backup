import requests 
from bs4 import BeautifulSoup 
from pypdf import PdfReader 
from pdfquery import PDFQuery
from PyPDF2 import PdfFileReader
import io 
import datefinder 
from urllib.request import urlopen 
from datetime import datetime

url = "https://www.utkarsh.bank/xsite/assests/pdf/Fixed_Deposit_Rates_wef_August_21_2023_Website.pdf"
bcode = 311
def get_date():
    
    try:
        res = requests.get(url)
        if res.status_code==200:
            pdf = PdfFileReader(io.BytesIO(res.content))
            info = pdf.getDocumentInfo()
            dates = datefinder.find_dates(info['/Title'])
            redate = ""
            for date in dates:
                redate += date.strftime("%d-%b-%y")
            return redate , bcode

        else:
            return "", bcode
    except:
        return "", bcode


# ans = get_date()