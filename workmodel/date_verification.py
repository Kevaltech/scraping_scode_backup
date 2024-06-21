import psycopg2
import schedule
import time
import datetime
from datetime import timedelta
import email_trigger
import sys
import os
from dotenv import load_dotenv
sys.path.insert(0,"C:/Users/Indore Intern1/Desktop/Ayush/email_trigger_automation/trigger_function/date_scraping")
# sys.path.insert(0, './date_scraping')
import date
import fd_date_verification


def days_between_dates(dt1, dt2):
    date_format = "%d-%b-%y"
    a = time.mktime(time.strptime(dt1, date_format))
    b = time.mktime(time.strptime(dt2, date_format))
    delta = b - a
    return int(delta / 86400)

def sdrate_main():
    print("sdrate_func")
    sd_current_dates, sd_banks, sd_urls, sd_page_not_found_bank, sd_heavy_taffic = date.schema_storage()
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

    # print(old_dates)
    # print(old_dates, current_dates)
    cnt1 = 0
    sd_bank_date_changed = []
    for i in range(len(sd_current_dates)):
        if sd_current_dates[i]!="":
            sd_old_dates = []
            cursor.execute(f"SELECT effdate FROM api_sdrate WHERE bref='{sd_banks[i][1]}' ORDER BY id")
            row = cursor.fetchone()
            while row is not None:
                sd_old_dates.append(row[0])
                row = cursor.fetchone()
            date_in_table = sd_old_dates[-1]
            if date_in_table!=sd_current_dates[i]:
                cnt1+=1
                days = days_between_dates(date_in_table, today)
                sd_bank_date_changed.append((sd_banks[i][0], days, sd_current_dates[i], sd_urls[i]))
    return sd_bank_date_changed, sd_page_not_found_bank, sd_heavy_taffic, cnt1


def main():
    print("sdrate_scanning")
    sd_bank_date_changed, sd_page_not_found_bank, sd_heavy_traffic, cnt1 = sdrate_main()
    print("fdrate_scanning")
    fd_bank_date_changed,fd_page_not_found_bank, fd_heavy_traffic, cnt2 = fd_date_verification.fdrate_main()

    # print(cnt, bank_date_changed)
    email_trigger.call_trigger(sd_bank_date_changed, fd_bank_date_changed, sd_page_not_found_bank+fd_page_not_found_bank,
                               sd_heavy_traffic+fd_heavy_traffic, cnt1, cnt2)
    # print(old_dates)
# schedule.every().day.at("17:23").do(main)

# while True:
#     schedule.run_pending()
#     time.sleep(360)
main()