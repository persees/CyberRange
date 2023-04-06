import smtplib

sender = "test@example.com"
receivers = ["labworks01@outlook.com"]
message = """From: Test <test@example.com>
To: labworks01 <labworks01@outlook.com>
Subject: SMTP email example

This is a sample test

"""

try:
    smtpObject = smtplib.SMTP("localhost")
    smtpObject.sendmail(sender, receivers, message)
    print("Email sent with success")
except SMTPException as e:
    print(e)
