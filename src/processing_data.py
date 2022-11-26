from load_data import accounts, cards, clients, dispositions, districts, loans_comp, loans_dev, transactions

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