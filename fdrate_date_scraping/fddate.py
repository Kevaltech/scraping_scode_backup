import os
import glob 
import datetime
import psycopg2
from dotenv import load_dotenv

folder_path = "C:/Users/Indore Intern1/Desktop/Ayush/email_trigger_automation/trigger_function/fdrate_date_scraping"

file_list = glob.glob(os.path.join(folder_path, '*.py'))
conn = psycopg2.connect(    
    database = "do_db",
    user="do_user",
    password="Compo%6790",
    host="143.198.197.163",
    port="5432",
)
#for kvb bank wait for some time it.
cursor = conn.cursor()
query_to_run = "select bcode, display_name,fd_url, active, bref from api_bstat"
cursor = conn.cursor()
cursor.execute(query_to_run)
rows = cursor.fetchall()
bank_info = {}
for row in rows:
    # print(row)
    bank_info[row[0]] = row
    row = cursor.fetchone()
    
def get_date_list():
    """
    This function imports all python files in the fdrate_date_scraping directory
    and gets the date and bank information from each module. It then returns
    a list of dates, a list of bank names and urls and a list of bank references.
    """
    # Initialize lists to store data
    date_list, bank_list, url_list = [], [], []

    # Iterate over each python file in the fdrate_date_scraping directory
    for file_path in file_list:
        # Get the name of the module
        module_name = os.path.basename(file_path)[:-3]

        # If the module is not 'fddate', import it and get the date and bank info
        if module_name != 'fddate':
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


load_dotenv()
def schema_storage():
    """
    This function stores the date and bank information in the 'fdrate_date_scrape' table in the database.
    It first retrieves the date and bank information using the 'get_date_list' function. Then, it connects
    to the database and updates the 'dates_info' table to keep track of the number of times the page of
    each bank has not been opened. It then inserts the date and bank information into the 'fdrate_date_scrape'
    table and returns the date, bank, url, list of banks where the page has not been opened and list of banks
    where there was heavy traffic.
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

    # Update 'dates_info' table
    cursor = conn.cursor()
    d = datetime.date.today()
    day = str(d.strftime("%d_%m_%y"))
    todays_date = d.strftime("%d-%b-%y")

    # Insert date and bank information into 'fdrate_date_scrape' table
    data = []
    page_not_open_bank = []
    heavy_traffic = []
    for i in range(min(len(dates), len(banks))):
        if dates[i]=='' or dates[i]=='403':
            # Update 'dates_info' table
            sdrate_page = f"select fdrate_page_not_open from dates_info where bank_name='{banks[i][0]}'"
            cursor.execute(sdrate_page)
            page_not = cursor.fetchone()
            cur_value = page_not[0]
            if dates[i]=='403':
                page_not_open_bank.append((banks[i][0], 'FD', cur_value+1, urls[i]))
            select_query = f"SELECT last_change_date FROM fdrate_date_scrape WHERE bank_name='{banks[i][0]}'"
            blank_dates = []
            if dates[i]=='':
                heavy_traffic.append((banks[i][0], 'FD', cur_value+1, urls[i]))
            cursor.execute(select_query)
            row = cursor.fetchone()
            while row is not None:
                blank_dates.append(row[0])
                row = cursor.fetchone()
            dates[i] = blank_dates[-1]

            update_dates_info = f"update dates_info set fdrate_page_not_open={cur_value+1} where bank_name='{banks[i][0]}'"
            cursor.execute(update_dates_info)
        else:
            update_dates_info = f"update dates_info set fdrate_page_not_open={0} where bank_name='{banks[i][0]}'"
            cursor.execute(update_dates_info)

        updateDate = dates[i]
        if datetime.datetime.strptime(dates[i], '%d-%b-%y') > datetime.datetime.strptime(todays_date, '%d-%b-%y'):
            date_val = dates[i].strftime("%d/%m/%y")
            updateDate = datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")
        
        val = (banks[i][0], updateDate, todays_date)
        data.append(val)
    for d in data:
        cursor.execute(f"INSERT into fdrate_date_scrape(bank_name, last_change_date, todays_date) VALUES (%s, %s, %s)", d)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Return relevant information
    return dates, banks, urls, page_not_open_bank, heavy_traffic

# schema_storage()