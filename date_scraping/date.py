import os
import glob
import psycopg2
import datetime
from dotenv import load_dotenv


load_dotenv()
conn = psycopg2.connect(    
        database = "do_db",
        user="do_user",
        password="Compo%6790",
        host="143.198.197.163",
        port="5432",
    )

cursor = conn.cursor()
query_to_run = "select bcode, display_name, sd_url, active, bref from bstat"
cursor = conn.cursor()
cursor.execute(query_to_run)
rows = cursor.fetchall()
bank_info = {}
for row in rows:
    # print(row)
    bank_info[row[0]] = row
    row = cursor.fetchone()
# Specify the path to the folder containing your modules
folder_path = f"C:/Users/Indore Intern1/Desktop/Ayush/email_trigger_automation/trigger_function/date_scraping"
# folder_path = os.path.dirname(__file__)
# Get a list of all Python files in the folder
file_list = glob.glob(os.path.join(folder_path, '*.py'))
# Import all modules dynamically
load_dotenv()
def get_date_list():
    """
    This function imports all python files in the date_scraping directory
    and gets the date and bank information from each module. It then returns
    a list of dates, a list of bank names and urls and a list of bank references.
    """
    # Initialize lists to store data
    date_list, bank_list, url_list = [], [], []

    # Iterate over each python file in the date_scraping directory
    for file_path in file_list:
        # Get the name of the module
        module_name = os.path.basename(file_path)[:-3]

        # If the module is not 'date', import it and get the date and bank info
        if module_name != 'date':
            module = __import__(module_name)
            date, bcode = module.get_date()
            
            # If the bank is active, add the date, bank info and url to the lists
            if bank_info[bcode][3]:
                date_list.append(date)
                bank_list.append((bank_info[bcode][1], bank_info[bcode][4]))
                url_list.append(bank_info[bcode][2])
                # print(bank_info[bcode][1], (date, bcode))
    
    # Return the lists
    return date_list, bank_list, url_list

def schema_storage():
    """
    This function retrieves the date and bank information from the get_date_list function and stores it in the database.
    It updates the 'dates_info' table to keep track of the number of times the page of each bank has not been opened.
    It then inserts the date and bank information into the 'sdrate_date_scrape' table and returns the date, bank, url,
    list of banks where the page has not been opened and list of banks where there was heavy traffic.
    """
    # Get date and bank information
    dates, banks, urls = get_date_list()
    
    # Connect to database
    conn = psycopg2.connect(  
        database = "do_db",
        user="do_user",
        password="Compo%6790",
        host="143.198.197.163",
        port="5432",
    )
    cursor = conn.cursor()
    
    # Get today's date and format it
    d = datetime.date.today()
    day = str(d.strftime("%d_%m_%y"))
    todays_date = d.strftime("%d-%b-%y")

    # Initialize lists to store data
    data = []
    page_not_open_bank = []
    heavy_traffic = []
    
    # Iterate over each date, bank and url
    for i in range(min(len(dates), len(banks))):
        # If the date is empty or '403', update the 'dates_info' table
        if dates[i]=='' or dates[i]=='403':
            sdrate_page = f"select sdrate_page_not_open from dates_info where bank_name='{banks[i][0]}'"
            cursor.execute(sdrate_page)
            page_not = cursor.fetchone()
            cur_value = page_not[0]
            if dates[i]=='403':
                page_not_open_bank.append((banks[i][0], 'SD', cur_value+1, urls[i]))
            select_query = f"SELECT last_change_date FROM sdrate_date_scrape WHERE bank_name='{banks[i][0]}'"
            blank_dates = []
            if dates[i]=='':
                heavy_traffic.append((banks[i][0], 'SD', cur_value+1, urls[i]))
            cursor.execute(select_query)
            row = cursor.fetchone()
            while row is not None:
                blank_dates.append(row[0])
                row = cursor.fetchone()
            dates[i] = blank_dates[-1]
            update_dates_info = f"update dates_info set sdrate_page_not_open={cur_value+1} where bank_name='{banks[i][0]}'"
            cursor.execute(update_dates_info)
        else:
            update_dates_info = f"update dates_info set sdrate_page_not_open={0} where bank_name='{banks[i][0]}'"
            cursor.execute(update_dates_info)

        # Create a tuple of bank name, date and today's date and append it to the data list

        updateDate = dates[i]
        if datetime.datetime.strptime(dates[i], '%d-%b-%y') > datetime.datetime.strptime(todays_date, '%d-%b-%y'):
            date_val = datetime.datetime.strptime(dates[i], '%d-%b-%y')
            date_val = date_val.strftime("%d/%m/%y")
            updateDate = datetime.datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
        dates[i]=updateDate
        val = (banks[i][0], updateDate, todays_date)
        data.append(val)
    
    # Insert the data into the 'sdrate_date_scrape' table
    for d in data:
        cursor.execute(f"INSERT into sdrate_date_scrape(bank_name, last_change_date, todays_date) VALUES (%s, %s, %s)", d)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Return the data
    return dates, banks, urls, page_not_open_bank, heavy_traffic

# dates, banks = schema_storage()
# print(dates, banks)