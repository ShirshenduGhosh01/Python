import random
import smtplib
#from OTP_generator import  OTP 
import math
import email 
 
# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(5) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
 
# Driver code
if __name__ == "__main__" :
     print()
    


OTP = generateOTP()
print=OTP


     
def EMAIL() : 
    server=smtplib.SMTP('smtp.gmail.com',587)
#adding TLS security 
    server.starttls()
#get your app password of gmail ----as directed in the video
    password='lzyjknkscsmswtaz'
    server.login('project.exhibition.II@gmail.com',password)
#generate OTP using random.randint() function
#otp=''.join([str(random.randint(0,9)) for i in range(4)])
    msg='Hello, Your OTP is '+str(OTP)
    sender='project.exhibition.II@gmail.com'  
    receiver=input("Enter your eamil id: ")
#sending
    server.sendmail(sender,receiver,msg)
    server.quit()
    return server
EMAIL()

verify= input('Enter the OTP: ')


if verify == OTP:
    print ("Email verified")

elif verify != OTP:
    print ("Wrong OTP")
else :
    print ("ERROR")


