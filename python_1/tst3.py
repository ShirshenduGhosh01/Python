import os
import math
import random
import smtplib

sender = "project.exhibition.II@gmail.com"
app_password= "lzyjknkscsmswtaz"
emailid = input("Enter your email: ")



digits="0123456789"
OTP=""
for i in range(5):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender, app_password)
s.sendmail('project.exhibition.II@gmail.com',emailid,msg)

b= 0

while b != 5 :
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
        break
    else:
        print("Please Check your OTP again") 
        b += 1