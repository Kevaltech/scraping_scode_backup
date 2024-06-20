# import pandas as pd
# import dateutil.parser
# def same_format(date_list):
#     # print(date_list)
#     same_format_list = []
#     for date in date_list:
#         if date=='na':
#             same_format_list.append("na")
#         else:
#             if(type(date)!=str):
#                 date = date.strftime('%m/%d/%y')
#             same_format_list.append(dateutil.parser.parse(date).strftime("%Y-%m-%d"))
#     return same_format_list