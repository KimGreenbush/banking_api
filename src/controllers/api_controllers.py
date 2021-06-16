from flask import request
from src.app import app
from src.models import Client

# usually have logger is other file and import module
import logging

logging.basicConfig(filename="banking_api.log", level=logging.INFO)

# POST /clients => Creates a new client return a 201 status code
@app.route("/clients", methods=["POST"])
def new_client():
    logging.info(request.get_json())
    pass

# GET /clients => gets all clients return 200
@app.route("/clients", methods=["GET"])
def get_clients():
    return { "message": "Welcome to my project routes!"}

# GET /clients/10 => get client with id of 10 return 404 if no such client exist
@app.route("/clients/<id>",  methods=["GET"])
def get_client(id):
    logging.info(f"Client id is {id}")
    return

# PUT /clients/12 => updates client with id of 12 return 404 if no such client exist
@app.route("/clients/<id>", methods=["PUT"])
def update_client(id):
    pass

# DELETE /clients/15 => deletes client with the id of 15 return 404 if no such client exist return 205 if success
@app.route("/clients/<id>", methods=["DELETE"])
def delete_client(id):
    pass

# POST /clients/5/accounts =>creates a new account for client with the id of 5 return a 201 status code
@app.route("/clients/<id>/accounts", methods=["POST"])
def add_client_account(id):
    pass

# GET /clients/7/accounts => get all accounts for client 7 return 404 if no client exists
@app.route("/clients/<id>/accounts",  methods=["GET"])
def get_client_accounts(id):
    pass

# GET /clients/7/accounts?amountLessThan=2000&amountGreaterThan400 => get all accounts for client 7 between 400 and 2000 return 404 if no client exists
@app.route("/clients/<id>/accounts",  methods=["GET"])
def get_client_accounts_between_400_2000(id):
    pass

# GET /clients/9/accounts/4 => get account 4 for client 9 return 404 if no account or client exists
@app.route("/clients/<client_id>/accounts/<account_id>",  methods=["GET"])
def get_client_account(client_id, account_id):
    pass

# PUT /clients/10/accounts/3 => update account with the id 3 for client 10 return 404 if no account or client exists
@app.route("/clients/<client_id>/accounts/<account_id>", methods=["PUT"])
def update_client_account(client_id, account_id):
    pass

# DELETE /clients/15/accounts/6 => delete account 6 for client 15 return 404 if no account or client exists
@app.route("/clients/<client_id>/accounts/<account_id>", methods=["DELETE"])
def delete_client_account(client_id, account_id):
    pass

# PATCH /clients/17/accounts/12 => Withdraw/deposit given amount (Body: {"deposit":500} or {"withdraw":250} return 404 if no account or client exists return 422 if insufficient funds
@app.route("/clients/<client_id>/accounts/<account_id", methods=["PATCH"])
def update_client_account_balance(client_id, account_id):
    pass

# PATCH /clients/12/accounts/7/transfer/8 => transfer funds from account 7 to account 8 (Body: {"amount":500}) return 404 if no client or either account exists return 422 if insufficient funds
@app.route("/clients/<client_id>/accounts/<account1_id>/transfer/<account2_id>",  methods=["PATCH"])
def  transfer_between_accounts(client_id, account1_id, account2_id):
    pass
