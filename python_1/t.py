import smtplib, ssl
import math, random


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "project.exhibition.II@gmail.com"
receiver_email = input("Enter your eamil address: ")
password = "lzyjknkscsmswtaz"
OTP= ''.join([str(random.randint(0,9))for i in range (5)])
# Create a secure SSL context
context = ssl.create_default_context()
message = "OTP is: " +str(OTP) ,"Please don't share"
# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print("Somthing went wrong",e)
finally:
    server.quit() 