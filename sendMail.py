#imports
import os
import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'sharan.singh0203@gmail.com'
email_password = "maxc yyjw urty esdd"
email_receiver = 'ssing288@ucr.edu'

# Set the subject and body of the email
subject = 'waz good bitch'
body = """
you just got gojo'd bitch https://youtube.com/shorts/YOwUCwzmhZM?si=9VgVMwy4JXnWBUKk
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())