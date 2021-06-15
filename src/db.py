from sqlalchemy import create_engine, MetaData

engine = create_engine("", echo=True, future=True)

metadata = MetaData