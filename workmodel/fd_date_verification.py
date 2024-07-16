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

def fdrate_main():
    """
    This function retrieves the current and old dates of each bank from the database and checks if the date has changed.
    If the date has changed, it calculates the number of days between the new and old dates and adds the bank details
    to the list of bank_date_changed.
    Returns a tuple containing the list of bank_date_changed, the list of banks with page not found, the list of banks with heavy traffic,
    and the count of banks with changed dates.
    """
    # Connect to the database
    load_dotenv()
    conn = psycopg2.connect(    
        database = "do_db",
        user="do_user",
        password="Compo%6790",
        host="143.198.197.163",
        port="5432",
    )

    cursor = conn.cursor()
    # Get today's date
    yesterday = datetime.date.today()
    today = yesterday.strftime('%d-%b-%y')
    
    # Retrieve current and old dates, banks, urls, page not found banks and heavy traffic from fddate.schema_storage()
    fd_current_dates, fd_banks, fd_urls, page_not_open, heavy_trafic = fddate.schema_storage()
    
    cnt2 = 0
    fd_bank_date_changed = []  # List to store bank details with changed dates
    for i in range(len(fd_current_dates)):
        if fd_current_dates[i]!="":
            fd_old_dates = []  # List to store old dates of the bank
            # Execute SQL query to retrieve old dates from the database
            cursor.execute(f"SELECT effstartdate FROM fdrate WHERE bref='{fd_banks[i][1]}' ORDER BY id")
            row = cursor.fetchone()
            while row is not None:
                fd_old_dates.append(row[0])
                row = cursor.fetchone()
            date_in_table = fd_old_dates[-1]  # Get the most recent date in the table
            if date_in_table!=fd_current_dates[i]:
                cnt2+=1
                days = days_between_dates(fd_current_dates[i], today)
                fd_bank_date_changed.append((fd_banks[i][0], days, fd_current_dates[i], fd_urls[i]))
    return fd_bank_date_changed,page_not_open, heavy_trafic, cnt2

# fdrate_main()