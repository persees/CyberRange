import smtplib
import argparse

parser = argparse.ArgumentParser(description='Send emails')
parser.add_argument("-s", "--sender")
parser.add_argument("-r", "--receiver")

args = parser.parse_args()

sender = args.sender
receivers = [args.receiver]
message = """From: Test <{}>
To: Test <{}>
Subject: Company credentials expired

This is a friendly reminder that your company credentials are expiring in 5 days.

Please update your password so you don't lose access to your account:


""".format(sender, receivers)

try:
    smtpObject = smtplib.SMTP("localhost")
    smtpObject.sendmail(sender, receivers, message)
    print("Email sent with success")
except SMTPException as e:
    print(e)
