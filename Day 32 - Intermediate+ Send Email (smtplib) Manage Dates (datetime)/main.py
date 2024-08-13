import smtplib
import datetime as dt
import random


now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

my_email = "engineeringsolutionke@gmail.com"
password = "sqhbyioviculeayu"

yahoo_mail = "engineeringsolutionske1@yahoo.com"
yahoo_password = "wTv3Qfcrrz4L8L8"


if weekday == 0:
    with open("quote.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shariq.isak@gmail.com  ",
            msg=f"Subject: Monday Motivation\n\n {quote}"
        )







