from .util import *


def preprocess_accounts(accounts):
    accounts = extract_date(accounts, "date")
    return accounts.rename(columns={"frequency": "account_frequency", "year": "account_year",
                                    "month": "account_month", "day": "account_day"})
