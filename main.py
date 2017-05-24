import time

import config
from mail import send_email


time.sleep(300)

while True:
    title = []
    body = []

    for currency in config.currencies:
        temp_title, temp_body = currency.generate_mail_lists()
        title.extend(temp_title)
        body.extend(temp_body)
        body.append('<br/>\n')           # make line between currencies


    if len(title) > 0:
        send_email(config.SMTP_SERVER, config.PORT, config.LOGIN, config.PASSWORD, config.RECIPENTS,
                       ' '.join(title),
                       '<br/>\n'.join(body)
                       )

    time.sleep(600)
