#smtplib and managing dates

import smtplib


my_email = input("type your outlook email")
my_password = input("type your outlook password")

connection = smtplib.SMTP("smtp-mail.outlook.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="exampleemail@examlesmtp.com", msg="Subject:Hello!\n\n This is the body of my ")
connection.close()

# or 
with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="exampleemail@examlesmtp.com", msg="Subject:Hello!\n\n This is the body of my ")


# data and time

import datetime as dt:
now = dt.datetime.now()
print(now)

date_of_birth = dt.datetime(year=2000, month=1, day=1, hour=20:00)

#