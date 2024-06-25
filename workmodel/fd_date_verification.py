import psycopg2
import schedule
import time
import datetime
from datetime import timedelta
import email_trigger
import sys
import os
from dotenv import load_dotenv
sys.path.insert(0,"C:/Users/Indore Intern1/Desktop/Ayush/email_trigger_automation/trigger_function/fdrate_date_scraping")
# sys.path.insert(0, './fdrate_date_scraping')
import fddate

def days_between_dates(dt1, dt2):
    try:
        date_format = "%d-%b-%y"
        a = time.mktime(time.strptime(dt1, date_format))
        b = time.mktime(time.strptime(dt2, date_format))
        delta = abs(b - a)
        return int(delta / 86400)
    except:
        return 10

def fdrate_main():
    load_dotenv()
    conn = psycopg2.connect(    
        database = "do_db",
        user="do_user",
        password="Compo%6790",
        host="143.198.197.163",
        port="5432",
    )

    cursor = conn.cursor()
    yesterday = datetime.date.today()
    today = yesterday.strftime('%d-%b-%y')
    
    fd_current_dates, fd_banks, fd_urls, page_not_open, heavy_trafic = fddate.schema_storage()
    # print(old_dates)
    # print(old_dates, current_dates)
    cnt2 = 0
    fd_bank_date_changed = []
    for i in range(len(fd_current_dates)):
        if fd_current_dates[i]!="":
            fd_old_dates = []
            cursor.execute(f"SELECT effstartdate FROM api_fdrate WHERE bref='{fd_banks[i][1]}' ORDER BY id")
            row = cursor.fetchone()
            while row is not None:
                fd_old_dates.append(row[0])
                row = cursor.fetchone()
            date_in_table = fd_old_dates[-1]
            if date_in_table!=fd_current_dates[i]:
                cnt2+=1
                days = days_between_dates(fd_current_dates[i], today)
                fd_bank_date_changed.append((fd_banks[i][0], days, fd_current_dates[i], fd_urls[i]))
    return fd_bank_date_changed,page_not_open, heavy_trafic, cnt2

# fdrate_main()