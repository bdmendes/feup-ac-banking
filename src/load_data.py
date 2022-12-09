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