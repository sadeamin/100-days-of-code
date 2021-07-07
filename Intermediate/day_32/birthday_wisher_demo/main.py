##################### Extra Hard Starting Project ######################
from datetime import *
import pandas
import random
import smtplib

my_email = "touhidalamin1@gmail.com"
password = "EaminAlamin782489"

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv("Intermediate/day_32/birthday_wisher_demo/birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"Intermediate/day_32/birthday_wisher_demo/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday! \n\n {contents}")


