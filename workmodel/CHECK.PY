# import psycopg2
# import datetime
# from datetime import timedelta
# import email_trigger
# import sys
import os
# from dotenv import load_dotenv


# # current_dates, banks = date.schema_storage()
# load_dotenv()
# conn = psycopg2.connect(
#     database = os.environ.get("DB_NAME"),
#     user= os.environ.get("DB_USER"),
#     password=os.environ.get("DB_PASSWORD"),
#     host=os.environ.get("DB_HOST"),
#     port=os.environ.get('DB_PORT'),
# )


# cursor = conn.cursor()
# yesterday = datetime.date.today() - timedelta(days=1)
# ydate = yesterday.strftime('%d-%b-%y')
# old_dates = []
# cursor.execute(f"SELECT last_change_date FROM scraped_date25_01_24 WHERE todays_date='11-Feb-24' ORDER BY id")
# row = cursor.fetchone()
# while row is not None:
#     old_dates.append(row[0])
#     row = cursor.fetchone()
path=os.getcwd()
print(os.path.abspath(path))
# print(old_dates)