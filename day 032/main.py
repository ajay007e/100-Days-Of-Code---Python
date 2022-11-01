import smtplib

email ="ajay010e.edu@gmail.com"
password = "password@123"
recipient_mail = "ajay010e@gmail.com"

sub = "Testing Mail"
msg = "This is a test message to check the smtplib."

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=email,password=password)
# connection.sendmail(
#     from_addr=email,
#     to_addrs=recipient_mail,
#     msg=f"Subject:{sub}\n\n{msg}")
# connection.close()

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=recipient_mail,
        msg=f"Subject:{sub}\n\n{msg}"
        )