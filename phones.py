import re
from sqlalchemy.exc import DBAPIError
from dump import d_session
from models import Orders


def remove_non_digit(string):
    string = re.sub(r'\D', '', string)
    return string[-10:] if len(string) > 10 else string


def main():
    def query():
        for order in d_session.query(Orders):
            number = remove_non_digit(order.contact_phone)
            order.fmt_phone = number

    run_query(query)


def run_query(f, attempts=3):
    while attempts:
        attempts -= 1
        try:
            return f()
        except DBAPIError as exc:
            if attempts > 0 and exc.connection_invalidated:
                d_session.rollback()
            else:
                raise


if __name__ == '__main__':
    main()
    d_session.commit()
