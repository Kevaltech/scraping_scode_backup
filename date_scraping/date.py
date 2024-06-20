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
    #for kvb bank wait for some time it.
cursor = conn.cursor()
query_to_run = "select bcode, display_name, sd_url, active, bref from api_bstat"
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
    print("woooooe")
    date_list, bank_list, url_list = [], [], []
    for file_path in file_list:
        # Extract the module name from the file path
        # print(file_path)
        module_name = os.path.basename(file_path)[:-3]  # Remove '.py' extension
        # from module_name import get_date
        # print(get_date)
        not_check = ['.env', 'date', '.gitignore']
        if module_name not in not_check:
            module = __import__(module_name)
            date, bcode = module.get_date()
            # print(bank_info[bcode])
            if bank_info[bcode][3]:
                date_list.append(date)
                bank_list.append((bank_info[bcode][1],bank_info[bcode][4]))
                url_list.append(bank_info[bcode][2])
                print(bank_info[bcode][1], (date, bcode))
    return date_list, bank_list, url_list

def schema_storage():
    print("schema_storage")
    dates, banks, urls = get_date_list()

    
    d = datetime.date.today()
    day = str(d.strftime("%d_%m_%y"))
    todays_date = d.strftime("%d-%b-%y")
    # sql = f'''CREATE TABLE scraped_date{day}(
    #     id SERIAL NOT NULL,
    #     bank_name varchar(20) not null,
    #     last_change_date varchar(30) not null,
    #     todays_date varchar(30) not null
    #     )'''

    # cursor.execute(sql)
    data = []
    page_not_open_bank = []
    heavy_traffic = []
    # print(dates)
    for i in range(min(len(dates), len(banks))):
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
            # print(blank_dates)
            dates[i] = blank_dates[-1]

            update_dates_info = f"update dates_info set sdrate_page_not_open={cur_value+1} where bank_name='{banks[i][0]}'"
            cursor.execute(update_dates_info)

        else:
            update_dates_info = f"update dates_info set sdrate_page_not_open={0} where bank_name='{banks[i][0]}'"
            cursor.execute(update_dates_info)

        val = (banks[i][0], dates[i], todays_date)
        data.append(val)
    # print(dates)
    # print(data)
    for d in data:
        cursor.execute(f"INSERT into sdrate_date_scrape(bank_name, last_change_date, todays_date) VALUES (%s, %s, %s)", d)

    conn.commit()
    conn.close()
    return dates, banks, urls, page_not_open_bank, heavy_traffic

# dates, banks = schema_storage()
# print(dates, banks)