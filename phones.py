import re
import sys
import signal
from time import sleep
from sqlalchemy.exc import DBAPIError
from models import get_session, Orders

non_digits = re.compile(r'\D')
DELAY_IN_SEC = 60


def remove_non_digit(raw_number):
    number = non_digits.sub('', raw_number)
    return number[-10:] if len(number) > 10 else number


def run_query(f, attempts=3):
    def wrapper():
        for _ in range(attempts):
            try:
                return f()
            except DBAPIError:
                continue
        else:
            session.rollback()
    return wrapper


@run_query
def format_contact_phones():
    for order in session.query(Orders).filter(Orders.fmt_phone.is_(None)):
        number = remove_non_digit(order.contact_phone)
        order.fmt_phone = number


def signal_exit(signum, frame):
    sys.exit('Signal {} has received. Exiting'.format(signum))


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_exit)
    session = get_session()
    while True:
        try:
            format_contact_phones()
            session.commit()
            sleep(DELAY_IN_SEC)
        except KeyboardInterrupt:
            print('Exiting')
            break
