import schedule 
import time 
from tabulate import tabulate
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os 
import pandas as pd

def message(subject, text, img=None, attachment=None): 
	
	msg = MIMEMultipart() 
	
	# Add Subject 
	msg['Subject'] = subject 
	
	# Add text contents 
	msg.attach(MIMEText(text, "html")) 

	return msg 


def mail(sd_bank_name,fd_bank_name, broken_links, working_links_but_issue, date_changed1, date_changed2): 
	print("in mail function")
	# initialize connection to our email server, 
	# we will use gmail here 
	smtp = smtplib.SMTP('smtp.gmail.com', 587) 
	smtp.ehlo() 
	smtp.starttls() 
	# smtp.ehlo()
	fd_data = {'Name':[], "Days Since Not Updated":[], 'Date':[]}
	for i in fd_bank_name:
		v1,v2,v3,v4 = i
		fd_data['Name'].append(f'<a href="{v4}">{v1}</a>')
		fd_data['Days Since Not Updated'].append(v2)
		fd_data['Date'].append(f'<span style="white-space: nowrap;">{v3}</span>')
	

	fd_table = pd.DataFrame(fd_data)
	html_fd_table = fd_table.to_html(index=False, escape=False)
	html_fd_table = html_fd_table.replace('<th>', '<th style="text-align: center;">')
	sd_data = {'Name':[], "Days Since Not Updated":[], 'Date':[]}
	for i in sd_bank_name:
		v1, v2, v3, v4 = i
		sd_data['Name'].append(f'<a href="{v4}">{v1}</a>')
		sd_data['Days Since Not Updated'].append(v2)
		sd_data['Date'].append(f'<span style="white-space: nowrap;">{v3}</span>')
    
	sd_table = pd.DataFrame(sd_data)
	html_sd_table = sd_table.to_html(index=False, escape=False)
	html_sd_table = html_sd_table.replace('<th>', '<th style="text-align: center;">')

	broken_link_info = {'Name':[],'Type':[], "Days Since Issue":[]}
	for i in broken_links:
		v1,v2,v3,v4 = i
		broken_link_info['Name'].append(f'<a href="{v4}">{v1}</a>')
		broken_link_info['Type'].append(v2)
		broken_link_info['Days Since Issue'].append(v3)

	broken_link_table = pd.DataFrame(broken_link_info)
	html_broken_table = broken_link_table.to_html(index=False, escape=False)
	html_broken_table = html_broken_table.replace('<th>', '<th style="text-align: center;">')

	scraping_issue_info = {'Name':[],"Type":[], "Days Since Issue":[]}
	for i in working_links_but_issue:
		v1,v2,v3,v4=i
		scraping_issue_info['Name'].append(f'<a href="{v4}">{v1}</a>')
		scraping_issue_info['Type'].append(v2)
		scraping_issue_info['Days Since Issue'].append(v3)
	# Login with your email and password 
	scraping_issue_table = pd.DataFrame(scraping_issue_info)
	html_scraping_table = scraping_issue_table.to_html(index=False, escape=False)
	html_scraping_table = html_scraping_table.replace('<th>', '<th style="text-align: center;">')

	smtp.login('kevaltechnology@gmail.com', 'dqhw ojbf zbav yacd') 
	# print("login_successfully")
	# Call the message function 
	msg = message(f"{date_changed1}-SD and {date_changed2}-FD, {len(broken_links)} Broken, {len(working_links_but_issue)} Scraping Issue",
	f"""<html><body><p>*** Information about the FD Rate </p><br> {html_fd_table}<br><br><p> **Information about the SD Rate**</p><br> {html_sd_table}
	<br><br><p>**Broken Links**</p><br> {html_broken_table}<br><br><p> **Scraping Issue**</p><br>{html_scraping_table}<br><br>
	<p>Update date on the admin server: https://backend.keval.in/admin or on pgadmin.</p></body></html>""") 
	
	# Make a list of emails, where you wanna send mail 
	to = ["ayushsingh.rv123@gmail.com", "patidarhariom134@gmail.com", "architkh@gmail.com"]
	# to = ["ayushsingh.rv123@gmail.com"]

	# Provide some data to the sendmail function! 
	smtp.sendmail(from_addr="ayshksingh2002@gmail.com", 
				to_addrs=to, msg=msg.as_string()) 
	
	# Finally, don't forget to close the connection 
	smtp.quit() 



def call_trigger(sd_bank, fd_bank, broken_links, working_links_but_issue, sdrate_dateChangedCounter, fdrate_dateChangedCounter):
	mail(sd_bank, fd_bank, broken_links, working_links_but_issue, sdrate_dateChangedCounter, fdrate_dateChangedCounter)


