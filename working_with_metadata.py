from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata_obj = MetaData()

address_table = Table(
    'address',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False)
)

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String())
)

print(user_table.c.keys())
print(user_table.primary_key)

print(address_table.c.values())
print(address_table.description)

metadata_obj.create_all(engine)
metadata_obj.drop_all(engine)
