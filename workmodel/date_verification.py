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
    """
    Calculate the number of days between two dates.

    Args:
        dt1 (str): The first date in the format 'dd-MMM-yy'.
        dt2 (str): The second date in the format 'dd-MMM-yy'.

    Returns:
        int: The number of days between the two dates. Returns 10 if there is an exception.
    """
    try:
        # Specify the date format
        date_format = "%d-%b-%y"

        # Convert the dates to timestamps
        a = time.mktime(time.strptime(dt1, date_format))
        b = time.mktime(time.strptime(dt2, date_format))

        # Calculate the delta in seconds
        delta = abs(b - a)

        # Convert the delta to days and return
        return int(delta / 86400)

    # If there is an exception, return 10
    except:
        return 10

def sdrate_main():
    """
    Retrieves the current and old dates of each bank from the database and checks if the date has changed.
    If the date has changed, it calculates the number of days between the new and old dates and adds the bank details
    to the list of bank_date_changed.
    Returns a tuple containing the list of bank_date_changed, the list of banks with page not found, the list of banks with heavy traffic,
    and the count of banks with changed dates.
    """
    # Retrieve current and old dates, banks, urls, page not found banks and heavy traffic from date.schema_storage()
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

    cnt1 = 0
    sd_bank_date_changed = []  # List to store bank details with changed dates
    for i in range(len(sd_current_dates)):
        if sd_current_dates[i]!="":
            sd_old_dates = []  # List to store old dates of the bank
            cursor.execute(f"SELECT effdate FROM api_sdrate WHERE bref='{sd_banks[i][1]}' ORDER BY id")
            row = cursor.fetchone()
            while row is not None:
                sd_old_dates.append(row[0])
                row = cursor.fetchone()
            date_in_table = sd_old_dates[-1]  # Get the most recent date in the table
            if date_in_table!=sd_current_dates[i]:
                cnt1+=1
                days = days_between_dates(sd_current_dates[i], today)
                sd_bank_date_changed.append((sd_banks[i][0], days, sd_current_dates[i], sd_urls[i]))
    return sd_bank_date_changed, sd_page_not_found_bank, sd_heavy_taffic, cnt1


def main():
    """
    Calls the sdrate_main() and fdrate_main() functions to check the dates of banks and
    triggers the email_trigger.call_trigger() function to send emails if dates have changed.
    """
    # Scan for changed dates in Savings Deposit Rates
    print("SD RATE Scanning")
    sd_bank_date_changed, sd_page_not_found_bank, sd_heavy_traffic, cnt1 = sdrate_main()

    # Scan for changed dates in Fixed Deposit Rates
    print("FD RATE Scanning")
    fd_bank_date_changed, fd_page_not_found_bank, fd_heavy_traffic, cnt2 = fd_date_verification.fdrate_main()

    # Trigger email if dates have changed
    # Merge the lists of page not found banks and heavy traffic
    page_not_found_banks = sd_page_not_found_bank + fd_page_not_found_bank
    heavy_traffic = sd_heavy_traffic + fd_heavy_traffic
    email_trigger.call_trigger(sd_bank_date_changed, fd_bank_date_changed,
                               page_not_found_banks, heavy_traffic, cnt1, cnt2)

main()