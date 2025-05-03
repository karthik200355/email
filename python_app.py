#go over to our gmail account and setup 2 factor authentication
#generate app password
#create a function to send the  mail
from email.message import EmailMessage
from userpassword import password 
import ssl 
import smtplib
  
email_sender ="karthikdadi6@gmail.com"
email_password = 'fgwc ludq zypa whmg'

email_receiver = "karthikdadi812004@gmail.com"

subject = "this  is project using email"

body=""" this is the project to send email form sender to receiver """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject']=subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())


