import matplotlib.pyplot as plt
import numpy as np

def plot_salary_per_district(districts):
    plt.scatter(districts['district_id'], districts['district_average_salary'])

    plt.xlabel("District Code")
    plt.ylabel("Average Salary")
    plt.xticks(np.arange(0, districts.shape[0], 5))
    plt.xlim(0, districts.shape[0] + 1)
    plt.yticks(np.arange(districts['district_average_salary'].min() - 100, districts['district_average_salary'].max() + 100, 500))
    plt.grid()
    plt.show()

def plot_card_type_distribution(cards):
    card_types = {}
    print(cards.head())
    total = cards.shape[0]
    types = cards['type'].unique()

    for t in types:
        card_types[t] = cards[cards['type'] == t].shape[0]

    y = np.array([v * 100 / total for v in card_types.values()])
    mylabels = [k + ' - ' + str(v) for k,v in card_types.items()]

    plt.pie(y, labels = mylabels)
    plt.show() 

def plot_gender_distribution(clients):
    clients_gender = {}
    total = clients.shape[0]
    genders = clients['gender'].unique()

    for g in genders:
        clients_gender[g] = clients[clients['gender'] == g].shape[0]

    y = np.array([v * 100 / total for v in clients_gender.values()])
    mylabels = [k + ' - ' + str(v) for k,v in clients_gender.items()]

    plt.pie(y, labels = mylabels)
    plt.show() 


def plot_monthly_payment_per_loan_amount(loans):
    import matplotlib.pyplot as plt

    status = []

    print(loans["status"].unique())

    for s in loans["status"]:
        status.append(0) if s == -1 else status.append(100) 

    plt.scatter(loans["amount"],loans["monthly_payment"], alpha=.7, edgecolor='k', s = 50, c=status)
    plt.xlabel('x - loan amount')
    plt.ylabel('y - monthly payment')


def plot_monthly_payment_per_status(loans):
    # status and monthly payment
    x = [x for x in loans['status']]
    y = [y for y in loans['monthly_payment']]

    dic = {}

    for i in range(0, len(x)):
        if (x[i] in dic):
            dic[x[i]].append(y[i])
        else:
            dic[x[i]] = [y[i]]

    data = []

    for i in dic.keys():
        data.append(dic[i])

    plt.figure( figsize=(12,6) )
    plt.boxplot(data, labels=["debt", "regular"])
    print("", end="")