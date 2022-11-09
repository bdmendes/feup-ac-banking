def preprocess_dispositions(dispositions):
    no_dispositions = dispositions.groupby("account_id")["type"].count(
    ).reset_index(name="number_account_dispositions")
    disposition_owner_ratio = dispositions.groupby("account_id")["type"].apply(
        lambda x: x[x == 'DISPONENT'].count()).reset_index(name="number_account_disponents")
    dispositions = dispositions.merge(no_dispositions, on="account_id").merge(
        disposition_owner_ratio, on="account_id")
    return dispositions
