import smtplib, ssl, getpass
from datetime import date
import time
import sys

def infoMail(infoDict, scheduleDict)->bool:
    port = 587
    smtp_server = 'smtp.gmail.com'
    sender_emailid = 'testmycode102938@gmail.com'
    password = getpass.getpass(prompt=f'Please enter the password for the email id {sender_emailid}: ')
    receiver_emailid = infoDict["Email ID"]
    message = f"""
    /Subject: Meeting has been scheduled.

    Dear {infoDict['Name']},

    A meeting has been scheduled on {date(year=date.today().year, month=scheduleDict["Month"], day=scheduleDict["Date"])}.
    \n\nPlease call the number (+1)(111) 111-1111 for cancellation.

    Regards,
    Meeting Scheduler.
    """
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_emailid, password)
        server.sendmail(sender_emailid, receiver_emailid, message)
