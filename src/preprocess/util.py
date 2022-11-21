import numpy as np
import pandas as pd


def extract_date(df: pd.DataFrame, date_column, extract_gender: bool = False) -> pd.DataFrame:
    df["year"] = df[date_column] // 10000
    df["month"] = (df[date_column] % 10000) // 100
    df["day"] = df[date_column] % 100
    if extract_gender:
        df["gender"] = np.where(df["month"] >= 50, "female", "male")
        df["month"] = np.where(
            df["month"] >= 50, df["month"] - 50, df["month"])
    df.drop(axis=1, columns=[date_column], inplace=True)
    return df


def korunas_to_euros(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = df[column].apply(lambda x: float("{:.2f}".format(x / 24.4)))
    return df

def account_date_to_levels(df: pd.DataFrame):
    data_range = []

    for i in df.index:
        loan_data = datetime.datetime(df['year'][i], df['month'][i], df['day'][i])
        account_data = datetime.datetime(df['account_year'][i], df['account_month'][i], df['account_day'][i])

        if loan_data < account_data:
            print("loan data is before account data")
            data_range.append(-1)
        else:
            diff_data = loan_data - account_data
            if diff_data.days < 92:
                data_range.append(0)
            elif diff_data.days < 138:
                data_range.append(1)
            elif diff_data.days < 183:
                data_range.append(2)
            elif diff_data.days < 365:
                data_range.append(3)
            elif diff_data.days < 730:
                data_range.append(4)
            else:
                data_range.append(5)

    df['account_level'] = data_range
    df = df.drop(columns=['account_year', 'account_month', 'account_day'])
    return df