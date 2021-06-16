from sqlalchemy import create_engine, MetaData, text

engine = create_engine("postgresql+psycopg2://bankingapi:Soubikun.20@bankingapi.cpiiv9dpoug5.us-east-2.rds.amazonaws.com:5432/pgdb", echo=True, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world"))
    print()

metadata = MetaData