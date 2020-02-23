import smtplib


# Module to collect data, format email and send the email.
def send_email(senders_mail, recipient_mail, credential, msg):
    # msg = """Subject: Hi there

    # This message is sent from Python."""
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.starttls()
    mailServer.login(senders_mail, credential)
    mailServer.sendmail(senders_mail, recipient_mail, msg)
    print(" \n Sent!")
    mailServer.quit()
