# import pandas as pd 
# import convert_date_same_format
# import email_trigger


# old_excel_data_df = pd.read_excel("Main(AutoRecovered).xlsx", sheet_name="date_formate_possible")
# # print(old_excel_data_df)
# old_date_list = convert_date_same_format.same_format(old_excel_data_df["Date"].to_list())
# # print(old_date_list)
# new_excel_date_df = pd.read_excel("main.xlsx", sheet_name="date_formate_possible")
# # print(new_excel_date_df)
# new_date_list = convert_date_same_format.same_format(new_excel_date_df['types_of_date'].to_list())
# print(old_date_list, new_date_list)
# length = min(len(old_date_list), len(new_date_list))
# i=0
# call_trigger = False
# dateChangedCounter=0
# bank_date_changed = ""
# while(i<length):
#     print(old_date_list[i], new_date_list[i])
#     if(old_date_list[i]!=new_date_list[i]):
#         call_trigger = True 
#         dateChangedCounter+=1
#         bank = new_excel_date_df.at[new_excel_date_df.index[i], "Bank"]
#         print(bank)
#         bank_date_changed += f" {bank}"
#     i+=1 
# if(call_trigger):
#     print(i)
#     email_trigger.call_trigger(bank_date_changed, dateChangedCounter)