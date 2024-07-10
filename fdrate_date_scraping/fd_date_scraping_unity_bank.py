import requests 
from pypdf import PdfReader
import io 
from bs4 import BeautifulSoup 
import datefinder
from selenium.webdriver.support.ui import WebDriverWait
from urllib.request import urlopen 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
from selenium.webdriver.chrome.service import Service as ChromeService
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

url = "https://theunitybank.com/fixed-deposits.html"
bcode = 310
def get_date():
    try:
        driver.implicitly_wait(10)
        driver.get(url)
        original_window = driver.current_window_handle
        driver.find_element(By.XPATH, "/html/body/div[2]/section[4]/div/div/div/p/span").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.new_window_is_opened)

        all_windows = driver.window_handles

        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
                break
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        current_url = driver.current_url
        res = requests.get(current_url)
        # print(res.content)
        if res.status_code==200:
            with io.BytesIO(res.content) as f:
                pdf = PdfReader(f)
                pages = pdf.pages[0]
                content = pages.extract_text()
                # print(content)
                info = content[402:418]
                # print(info)
                val =info[0:4]+'-'+info[5:8]+'-'+info[11:14]+info[15:]
                # print(val)
                # return info, bcode
                dates = datefinder.find_dates(val)
                redate = ""
                for date in dates:
                    redate += date.strftime("%d-%b-%y")
                return redate, bcode

    except:
        return "", bcode


# print(get_date())
