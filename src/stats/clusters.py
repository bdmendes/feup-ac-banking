import src.preprocess.onehotencoding as encoding
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def cluster_monthly_payment_per_loan_amount(loans):
    df = loans[['amount', 'monthly_payment']]
    label = KMeans(n_clusters=5, random_state=1).fit_predict(df)

    u_labels = np.unique(label)
    
    for i in u_labels:
        filtered_label = df[label == i]
        plt.scatter(filtered_label["amount"] , filtered_label["monthly_payment"] , label = i)
    plt.legend()
    plt.show()

def cluster_transactions(transactions):
    transactions = encoding.extract_categorical(transactions, 'type')
    transactions = encoding.extract_categorical(transactions, 'k_symbol')

    table = transactions.groupby(['account_id']).agg({'credit': 'sum','withdrawal': 'sum','withdrawal in cash': 'sum', 'household': 'sum', 'insurrance payment': 'sum', 'interest credited': 'sum', 'old-age pension': 'sum', 'payment for statement': 'sum', 'sanction interest if negative balance': 'sum'}).reset_index()
    print(table.shape)
    table.head()

    df = table[['credit', 'withdrawal', 'withdrawal in cash', 'household', 'insurrance payment', 'interest credited', 'old-age pension', 'payment for statement', 'sanction interest if negative balance']]
    table['transaction_profile'] = KMeans(n_clusters=5, random_state=1).fit_predict(df)

    return table[['account_id', 'transaction_profile']]
    