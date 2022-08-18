from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData, Sequence

metadata = MetaData()

users = Table(
    "my_users", metadata,
    Column("id", Integer, Sequence("user_id_seq"), primary_key=True),
    Column("email", String(100)),
    Column("password", String(100)),
    Column("fullname", String(100)),
    Column("created_on", DateTime),
    Column("status", String(1))
)


codes = Table(
    "my_codes", metadata,
    Column("id", Integer, Sequence("codes_id_seq"), primary_key=True),
    Column("email", String(100)),
    Column("reset_code", String(50)),
    Column("status", String(1)),
    Column("expired_in", DateTime)
)
