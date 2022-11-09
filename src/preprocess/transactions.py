import numpy as np
from .util import *


def preprocess_transactions(transactions):
    transactions = extract_date(transactions, "date")
    transactions = korunas_to_euros(transactions, "amount")
    transactions = korunas_to_euros(transactions, "balance")
    transactions["amount"] = np.where(transactions["type"].eq(
        "credit"), transactions["amount"], transactions["amount"] * -1)
    return transactions
