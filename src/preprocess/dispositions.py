def preprocess_dispositions(dispositions):
    no_dispositions = dispositions.groupby("account_id")["type"].count(
    ).reset_index(name="number_account_dispositions")
    dispositions = dispositions.merge(no_dispositions, on="account_id")
    return dispositions
