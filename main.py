import time
import datetime
import threading

import config
from mail import send_email

time.sleep(300)
errors = 0
exitFlag = 0

threads = []
thread_lock = threading.Lock()


def check_cryptocurrency(currency, lock):
    global exitFlag
    global errors

    while not exitFlag:

        title = []
        body = []

        lock.acquire()              # LOCK ACQUIRE

        try:
            # Main currency first!
            temp_title, temp_body = currency.generate_mail_lists()
            title.extend(temp_title)
            body.extend(temp_body)
            body.append('<br/>\n')

            for _currency in config.currencies:
                if currency == _currency:
                    continue

                time.sleep(3)
                temp_title, temp_body = _currency.generate_mail_lists()
                title.extend(temp_title)
                body.extend(temp_body)
                body.append('<br/>\n')

            if len(title) > 0:
                send_email(config.SMTP_SERVER, config.PORT, config.LOGIN, config.PASSWORD, config.RECIPENTS,
                           ' '.join(title),
                           '<br/>\n'.join(body))

            errors = 0

        except Exception as e:
            errors += 1

            with open(config.PATH, 'a+') as f:
                f.write(
                    '{0}: {1}!\n'.format(
                        str(datetime.datetime.now().replace(microsecond=0)),
                        str(e)
                    )
                )

            if errors >= config.ErrorAttemps:
                exitFlag = 1
        finally:
            lock.release()      # LOCK RELEASE

        time.sleep(600)


for currency in config.currencies:
    threads.append(threading.Thread(target=check_cryptocurrency, args=(currency,thread_lock)))
    threads[-1].start()
