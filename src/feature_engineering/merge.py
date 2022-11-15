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
