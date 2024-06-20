import requests
from selenium import webdriver 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib3
from random import randint
import datefinder 
from fake_useragent import UserAgent
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS
proxies_list = ['180.183.157.159:8080',
 '203.0.113.69:80',
 '176.31.200.104:3128',
 '149.129.131.46:8080',
 '85.214.124.194:5001',
 '54.194.252.228:3128',
 '103.169.20.46:8080',
 '177.12.238.1:3128',
 '204.185.204.64:8080',
 '45.169.162.1:3128',
 '170.39.194.156:3128',
 '198.59.191.234:8080',
 '200.105.215.18:33630',
 '212.71.255.43:38613',
 '115.75.70.79:4100',
 '193.242.138.1:3128',
 '192.53.163.144:3128',
 '193.122.71.184:3128',
 '8.209.249.96:8080',
 '144.217.131.61:3148',
 '45.56.75.90:5344',
 '149.129.239.170:8080',
 '143.198.40.24:8888',
 '66.175.223.147:4153',
 '194.195.213.197:1080',]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
chrome = webdriver.ChromeOptions()
url1 = "https://www.bankofbaroda.in"
url = "https://www.bankofbaroda.in/interest-rate-and-service-charges/deposits-interest-rates"
bcode = 100

def get_date():
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        content = soup.find_all("div", class_="field-heading")
        # print(content)
        cn = content[-2]
        # print(cn)
        info = ""
        for i in cn:
            info += i.text 
        dates = datefinder.find_dates(info)
        date_list = []
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        driver.quit()
        return redate, bcode
    except:
        return "", bcode
    
# val = get_date()
# print(val)