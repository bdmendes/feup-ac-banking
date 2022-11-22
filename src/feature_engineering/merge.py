import numpy as np


def get_card_account_id(dispositions, disp_id):
    try:
        account_id = dispositions.query(f"disp_id == {disp_id}")[
            'account_id'].values[0]
        return account_id
    except:
        return np.nan


def merge_card_account(cards, dispositions):
    cards['account_id'] = cards['disp_id'].apply(
        lambda x: get_card_account_id(dispositions, x))
    return cards.rename(columns={'type': 'card_type', 'year': 'card_year', 'month': 'card_month', 'day': 'card_day'})


def merge_account_transactions(accounts, transactions):
    average_account_balances = transactions.groupby(
        ["account_id"])["balance"].mean().to_frame()
    average_account_balances.rename(
        columns={'balance': 'account_average_balance'}, inplace=True)
    return accounts.merge(average_account_balances, on="account_id")


def merge_account_dispositions(accounts, dispositions):
    # filter out dispositions with type 'OWNER'
    dispositions = dispositions.query("type == 'OWNER'")
    dispositions = dispositions.drop(columns=['client_district_id'])
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
