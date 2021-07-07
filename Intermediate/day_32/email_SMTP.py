import smtplib

my_email = "touhidalamin1@gmail.com"
pasword = "EaminAlamin782489"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=pasword)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="sadeamin13@gmail.com", 
                        msg="Subject:hello\n\nthis is the body of my email."
                        )
    
    