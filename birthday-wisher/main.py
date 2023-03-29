import random, smtplib, pandas
import datetime as dt

# to generate a birthday letter
def letter(name):
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as f:
       msg = f.read()
    msg = msg.replace("[NAME]", name)
    msg = msg.replace("Angela", "Avrora")
    return msg

# getting creds for sending email
with open("creds.txt", "r") as f:
    content = [l.rstrip() for l in f.readlines()]
    email, pswd = content[0], content[1]

# getting birthday data from csv
data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")

# checking date and sending email
now = dt.datetime.now()
for p in data:
    if p['month'] == now.month and p['day'] == now.day:
        congrats = letter(p['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # secure connection
            connection.login(user=email, password=pswd)
            connection.sendmail(from_addr=email, 
                                to_addrs=p['email'], 
                                msg=f"Subject:Happy birthday\n\n{congrats}"
                                )





