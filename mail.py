import smtplib

def send_email(smtp, port,
               user, pwd,
               recipient,       # can be list
               subject, body
               ):

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP_SSL(smtp, int(port))
    #server.ehlo()
    #server.set_debuglevel(1)
    server.ehlo()
    #server.starttls()

    server.login(gmail_user, gmail_pwd)

    server.sendmail(FROM, TO, message)
    server.close()

