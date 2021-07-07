import datetime as dt
import random

date_of_birth = dt.datetime(year=2008, month=4, day=13)


    
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("Intermediate\day_32\quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        import smtplib

        my_email = "touhidalamin1@gmail.com"
        pasword = "EaminAlamin782489"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pasword)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="sadeamin13@gmail.com", 
                            msg=f"Subject:Monday Motivation\n\n{quote}."
                            )
