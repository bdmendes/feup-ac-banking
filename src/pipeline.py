import pandas as pd
import numpy as np

# Global settings
pd.set_option('display.max_columns', None)

COMP_DATA_SOURCE = "comp_data/"
DEV_DATA_SOURCE = "dev_data/"

# Reading the data
accounts = pd.read_csv(DEV_DATA_SOURCE + 'account.csv', sep=';')

cards_dev = pd.read_csv(DEV_DATA_SOURCE + 'card.csv', sep=';')
cards_comp = pd.read_csv(COMP_DATA_SOURCE + 'card.csv', sep=';')
cards = pd.concat([cards_dev, cards_comp])

clients = pd.read_csv(DEV_DATA_SOURCE + 'client.csv', sep=';')

dispositions = pd.read_csv(DEV_DATA_SOURCE + 'disp.csv', sep=';')

districts = pd.read_csv(DEV_DATA_SOURCE + 'district.csv', sep=';')

transactions_dev = pd.read_csv(DEV_DATA_SOURCE + 'trans.csv', sep=';')
transactions_comp = pd.read_csv(COMP_DATA_SOURCE + 'trans.csv', sep=';')
transactions = pd.concat([transactions_dev, transactions_comp])

loans_dev = pd.read_csv(DEV_DATA_SOURCE + 'loan.csv', sep=';')
loans_comp = pd.read_csv(COMP_DATA_SOURCE + 'loan.csv', sep=';')

# Data preprocessing

import src.preprocess.accounts as accpp
accounts = accpp.preprocess_accounts(accounts)

from src.preprocess.cards import preprocess_cards
cards = preprocess_cards(cards)

from src.preprocess.clients import preprocess_clients
clients = preprocess_clients(clients)

from src.preprocess.dispositions import preprocess_dispositions
dispositions = preprocess_dispositions(dispositions)

from src.preprocess.districts import preprocess_districts
districts = preprocess_districts(districts)

from src.preprocess.loans import preprocess_loans
loans_comp = preprocess_loans(loans_comp)
loans_dev = preprocess_loans(loans_dev)

from src.preprocess.transactions import preprocess_transactions
transactions = preprocess_transactions(transactions)

# data display
# accounts.head()
# cards.head()
# clients.head()
# print(dispositions.head())
# districts.head()
# loans_comp.head))
# loans_dev.head()
# transactions.head()