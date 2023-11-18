#imports
import os
import smtplib
import ssl
from email.message import EmailMessage

def sendSpam(name, lastName, email, infractions, badword, sitesVisited):

    # Define email sender and receiver
    email_sender = 'sharan.singh0203@gmail.com'
    email_password = "maxc yyjw urty esdd"
    email_receiver = email

    # Set the subject and body of the email
    if infractions == 1:
        subject = "Ruh Oh! Little {} has said a no-no word!".format(name)
        body = """
        Dear Mr. or Mrs. {}, we deeply regret to inform you that 
        your son / daughter has been saying bad words! He said
        the bad word, {}! Womp Womp! 
        This is but a courteous email to warn you as we wish no harm unto little {}, 
        just to let you know of his / her minor infraction. Hope you have a nice day!
        """.format(lastName, badword, name)
    elif infractions == 2:
        subject = "You've been a naughty, naughty boy"
        body = """
        {} YOU HAVE VISITED THESE SITES {}
        """.format(name, sitesVisited)
    elif infractions == 3:
        subject = "You've been a naughty, naughty boy"
        body = """
        {} YOUR DAYS ARE NUMBERED.
        """.format(name)
    elif infractions == 4:
        subject = "You've been a naughty, naughty boy"
        body = """
        {} YOUR DAYS ARE NUMBERED.
        """.format(name)
    else:
        subject = "You've been a naughty, naughty boy"
        body = """
        {} YOUR DAYS ARE NUMBERED.
        """.format(name)

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