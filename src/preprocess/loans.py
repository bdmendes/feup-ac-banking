import src.preprocess.util as pp


def preprocess_loans(loans):
    loans = pp.extract_date(loans, "date")
    loans = pp.korunas_to_euros(loans, "amount")
    loans = pp.korunas_to_euros(loans, "payments")
    loans.rename(columns={'payments': 'monthly_payment',
                 'duration': 'duration_months'}, inplace=True)
    return loans
