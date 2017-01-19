from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models import Orders, Base
from config import SOURCE_DB, WORK_DB

source_engine = create_engine(SOURCE_DB)
source_session = sessionmaker(source_engine)

dest_engine = create_engine(WORK_DB)
Base.metadata.create_all(dest_engine)
metadata = MetaData(bind=dest_engine)
dest_session = sessionmaker(dest_engine)

s_session = source_session()
d_session = dest_session()

if __name__ == '__main__':
    orders = s_session.query(Orders).all()
    for order in orders:
        new = Orders()
        new.id = order.id
        new.contact_name = order.contact_name
        new.contact_phone = order.contact_phone
        new.contact_email = order.contact_email
        new.status = order.status
        new.created = order.created
        new.confirmed = order.confirmed
        new.comment = order.comment
        new.price = order.price
        d_session.add(new)
    d_session.commit()
