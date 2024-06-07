import smtplib
from email.message import EmailMessage
import random 
otp= ''.join([str(random.randint(0,9))for i in range(5)])
massg = str(otp)

subject = "One Time Password"
message = ('Your one time password is', massg , 'please don"t share.') 
msg = EmailMessage()
msg['from'] = 'project.exhibition.ii@gmail.com' 
msg['to'] = input("Enter your eamil id: ")
msg['subject'] = subject
msg.set_content = message
msg1=str(message)

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()  
server.login('project.exhibition.ii@gmail.com', 'lzyjknkscsmswtaz')
server.send_message(message)
server.close()