import smtplib
import datetime as dt
import random
import pandas as pd


MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "#### #### #### ####"

now = dt.datetime.now()
month = now.month
day = now.day

df = pd.read_csv('birthdays.csv')
birthdays = df.to_dict(orient='records')

current_birthdays = []
for birthday in birthdays:
    if birthday['month'] == month and birthday['day'] == day:
        current_birthdays.append(birthday)

if current_birthdays:
    for birthday in current_birthdays:
        num = random.randint(1,3)
        file_path = f"letter_templates/letter_{num}.txt"
        with open(file_path, "r") as f:
            content = f.read()
            new_content = content.replace("[NAME]", birthday['name'])
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday["email"],
                                msg=f"Subject:Happy Birthday, "
                                f"{birthday['name']}!\n\n{new_content}")
