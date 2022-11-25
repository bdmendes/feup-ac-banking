import src.preprocess.util as encoding
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def cluster_monthly_payment_per_loan_amount(loans):
    df = loans[['amount', 'monthly_payment']]
    label = KMeans(n_clusters=5, random_state=1).fit_predict(df)

    u_labels = np.unique(label)

    for i in u_labels:
        filtered_label = df[label == i]
        plt.scatter(filtered_label["amount"],
                    filtered_label["monthly_payment"], label=i)
    plt.legend()
    plt.show()

    loans['loan_profile'] = label


def cluster_transactions(transactions):
    transactions = encoding.extract_categorical(transactions, 'type')
    transactions = encoding.extract_categorical(transactions, 'k_symbol')

    table = transactions.groupby(['account_id']).agg({'credit': 'sum', 'withdrawal': 'sum', 'withdrawal in cash': 'sum', 'household': 'sum', 'insurrance payment': 'sum',
                                                      'interest credited': 'sum', 'old-age pension': 'sum', 'payment for statement': 'sum', 'sanction interest if negative balance': 'sum'}).reset_index()
    print(table.shape)
    table.head()

    df = table[['credit', 'withdrawal', 'withdrawal in cash', 'household', 'insurrance payment',
                'interest credited', 'old-age pension', 'payment for statement', 'sanction interest if negative balance']]
    table['transaction_profile'] = KMeans(
        n_clusters=10, random_state=1).fit_predict(df)

    return table[['account_id', 'transaction_profile']]

def cluster_districts(districts):
    print(districts.head())

    df = districts[['district_no_inhabitants', 'district_no_cities', 'district_urban_inhabitants_ratio',
        'district_average_salary', 'district_unemployment_rate', 'districts_entrepreneurs_ratio', 'district_crimes_per_inhabitant','district_crime_growth']]

    districts['districts_profile'] = KMeans(
        n_clusters=10, random_state=1).fit_predict(df)

    return districts[['district_id', 'districts_profile']]
    