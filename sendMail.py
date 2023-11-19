import os
import smtplib
import ssl
from email.message import EmailMessage

def sendSpam(name, lastName, email, infractions, badword, sitesVisited):
    email_sender = 'sharan.singh0203@gmail.com'
    email_password = "maxc yyjw urty esdd"
    email_receiver = email

    # Set the subject and body of the email based on infractions
    if infractions == 1:
        subject = "Ruh Oh! Little {} has said a no-no word!".format(name)
        body = """
        Dear Mr. or Mrs. {}, we deeply regret to inform you that 
        your son / daughter has been saying bad words! He said
        the bad word, {}! Womp Womp! 
        This is but a courteous email to warn you as we wish no harm unto little {}, 
        just to let you know of his / her minor infraction. Hope you have a nice day!
        """.format(lastName, badword, name)
        attachment_path = 'thumbsup.jpg'  # Attachment for infraction 1
    elif infractions == 2:
        subject = "Bad Move, Child!"
        body = """
        Oh gee oh golly! It seems as though your son / daughter {} has
        said yet another Bad Word™! That's no good! As such, we will be revealing
        the sites that your son / daughter frequents! Enjoy!
        Word Said: {}
        {}
        """.format(name, badword, sitesVisited)
        attachment_path = 'crying.jpg'  # Attachment for infraction 2
    elif infractions == 3:
        subject = "HEY! STOP!"
        body = """
        {}. SWEARING?! UNDER THE JURISDICTION OF THE ANTI-SLANDERINATOR?!
        PREPOSTEROUS!
        UNHEARD OF!
        ABSOLUTELY UNFORGIVABLE!!!111!!!1!
        """.format(name)
        attachment_path = 'angry.jpg'  # Attachment for infraction 3
    elif infractions == 4:
        subject = "You've been a naughty, naughty boy"
        body = """
        {} YOUR DAYS ARE NUMBERED.
        """.format(name)
        attachment_path = 'thumbsdown.jpg'  # Attachment for infraction 4
    else:
        subject = "You've been a naughty, naughty boy"
        body = """
        {} YOUR DAYS ARE NUMBERED.
        Word Said: {}
        {}
        """.format(name, badword, sitesVisited)
        attachment_path = 'uncanny.jpg'  # Attachment for other infractions

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add image attachment based on infractions
    with open(attachment_path, 'rb') as img_file:
        img_data = img_file.read()
        em.add_attachment(img_data, maintype='image', subtype='jpg', filename=os.path.basename(attachment_path))

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
