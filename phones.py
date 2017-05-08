import re
from sqlalchemy.exc import DBAPIError
from models import get_session, Orders
non_digits = re.compile(r'\D')


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
def query():
    for order in session.query(Orders).filter(Orders.fmt_phone.is_(None)):
        number = remove_non_digit(order.contact_phone)
        order.fmt_phone = number


if __name__ == '__main__':
    session = get_session()
    query()
    session.commit()
