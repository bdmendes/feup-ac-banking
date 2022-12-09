import numpy as np


def merge_dispositions_cards(dispositions, cards):
    cards = cards.drop(columns=['card_id'])
    cards.columns = "card_" + cards.columns.values
    cards.rename(columns={'card_disp_id': 'disp_id'}, inplace=True)
    dispositions = dispositions.merge(
        cards[['disp_id', 'card_type']], on="disp_id", how="left").fillna('missing')
    return dispositions


def merge_account_transactions(accounts, transactions):
    # extract credit and debit per month
    positive_transactions = transactions[transactions['type'] == "credit"]
    negative_transactions = transactions[transactions['type'] != "credit"]

    account_credit_per_month = positive_transactions.fillna(0).groupby(
        ["account_id", "month"])["amount"].sum().to_frame().groupby("account_id").mean()
    account_credit_per_month.columns = ["average_account_credit_per_month"]

    account_debit_per_month = negative_transactions.fillna(0).groupby(
        ["account_id", "month"])["amount"].sum().to_frame().groupby("account_id").mean()
    account_debit_per_month.columns = ["average_account_debit_per_month"]
    account_debit_per_month["average_account_debit_per_month"] = account_debit_per_month["average_account_debit_per_month"].abs()

    # average balance per month
    account_balance_per_month = transactions.fillna(0).groupby(
        ["account_id", "month"])["balance"].mean().to_frame().groupby("account_id").mean()
    account_balance_per_month.columns = ["average_account_balance_per_month"]

    accounts = accounts.merge(account_credit_per_month, on="account_id", how="left")  \
        .merge(account_debit_per_month, on="account_id", how="left") \
        .merge(account_balance_per_month, on="account_id", how="left")
    return accounts.fillna(0)


def merge_account_dispositions(accounts, dispositions):
    # filter out dispositions with type 'OWNER'
    dispositions = dispositions.query("type == 'OWNER'")
    dispositions = dispositions.rename(columns={
                                       "client_day": "owner_day", "client_month": "owner_month", "client_year": "owner_year", "client_gender": "owner_gender"})

    accounts = accounts.merge(dispositions, on="account_id", how="left")
    accounts = accounts.drop(columns=['disp_id', 'type'])
    accounts = accounts.drop_duplicates(
        subset=['account_id'], ignore_index=True)
    return accounts


def merge_dispositions_clients(dispositions, clients):
    dispositions = dispositions.merge(
        clients, on="client_id", how="left")
    dispositions = dispositions.drop(columns=['client_id'])
    dispositions = dispositions.rename(columns={
                                       'day': 'client_day', 'month': 'client_month', 'year': 'client_year', 'gender': 'client_gender', 'district_id': 'client_district_id'})
    return dispositions


def merge_accounts_districts(accounts, districts):
    districts = districts.copy()
    districts.columns = "account_" + districts.columns.values
    districts.rename({'account_district_id': 'district_id'},
                     axis=1, inplace=True)
    accounts = accounts.merge(
        districts, on="district_id", how="left", suffixes=('', '_account'))
    #accounts.drop(columns=['district_id'], inplace=True)
    accounts.rename(
        columns={'district_id': 'account_district_id'}, inplace=True)
    return accounts


def merge_client_districts(clients, districts):
    districts = districts.copy()
    districts.columns = "owner_" + districts.columns
    districts.rename(
        columns={'owner_district_id': 'district_id'}, inplace=True)
    clients = clients.merge(
        districts, on="district_id", how="left")
    #clients.drop(columns=['district_id'], inplace=True)
    clients.rename(columns={'district_id': 'owner_district_id'}, inplace=True)
    return clients
