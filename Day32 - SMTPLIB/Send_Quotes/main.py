import random
import smtplib
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    my_email = "email"
    my_password = "password"


    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection = smtplib.SMTP("smtp-mail.outlook.com")

        connection.sendmail(from_addr=my_email, to_addrs="exampleemail@examlesmtp.com",
                            msg=f"Subject:Motivation E-Mail!\n\n {quote} ")

