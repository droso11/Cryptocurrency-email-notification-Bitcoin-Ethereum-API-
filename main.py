import time
import datetime

import config
from mail import send_email
from currency import DowntimeException

time.sleep(300)
errors = 0


while True:
    title = []
    body = []

    try:
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
        errors = 0

    except DowntimeException:
        time.sleep(300)
        continue

    except Exception as e:
        errors += 1

        with open('logs', 'a+') as f:
            f.write(
                '{0}: {1}!\n'.format(
                    str(datetime.datetime.now().replace(microsecond=0)),
                    str(e)
                )
            )

        if errors >= 5:
            break

    time.sleep(600)
