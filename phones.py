import re
from sqlalchemy.exc import DBAPIError
from models import get_session, Orders
match = re.compile(r'\D')


def remove_non_digit(raw_number):
    number = match.sub('', raw_number)
    return number[-10:] if len(number) > 10 else number


def run_query(f, attempts=3):
    def wrapper():
        for _ in range(attempts):
            try:
                return f()
            except DBAPIError:
                continue
        else:
            print('why i"m here')
            session.rollback()
    return wrapper


@run_query
def query():
    for order in session.query(Orders):
        number = remove_non_digit(order.contact_phone)
        order.fmt_phone = number


if __name__ == '__main__':
    session = get_session()
    query()
    session.commit()
