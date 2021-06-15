from src.db import metadata
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Account:
    __tablename__ = "account"
    acount_table = Table(
    "account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", ForeignKey("client.id"), nullable=False),
    Column("balance", Integer),
    Column("type", String(15))
    )
    owner = relationship("Client", back_populates="accounts")

    def __init__(self, id, client_id, init_deposit, type):
        self._account_id = id
        self._client_id = client_id
        self._balance = init_deposit
        self._type = type

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def transfer(self, other_acct, amount):
        self._balance -= amount
        other_acct._balance += amount