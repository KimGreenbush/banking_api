from .account import Account
from src.db import metadata
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import relationship

class Client:
    __tablename__ = "client"
    client_table = Table(
    "client",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(20)),
    Column("total_balance", Integer)
    )
    accounts = relationship("Account", back_populates="client")

    def __init__(self, id, name, init_deposit, type):
        self._client_id = id
        self._name = name
        self._bank_accounts = [Account(id, init_deposit, type)]
        self._total_balance = 0

    def add_account(self, id, init_deposit, type):
        new_account = Account(id, init_deposit, type)
        self._bank_accounts.push(new_account)
        return self

    def remove_account(self, id):
        for account in self._bank_accounts:
            if account._id == id:
                del self._bank_accounts[id-1]
        return self

    def deposit(self, id):
        self._bank_accounts[id-1].deposit()
        return self

    def withdraw(self, id):
        self._bank_accounts[id-1].withdraw()
        return self

    def transfer(self, account1_id, account2_id):
        self._bank_accounts[account1_id-1].transfer(account2_id)
        return self