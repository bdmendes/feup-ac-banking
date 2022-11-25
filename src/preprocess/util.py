from datetime import datetime
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
        loan_data = datetime(
            df['year'][i], df['month'][i], df['day'][i])
        account_data = datetime(
            df['account_year'][i], df['account_month'][i], df['account_day'][i])

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


def extract_categorical(table, columnName):
    df_binary_columns = pd.get_dummies(table[columnName])
    for column in df_binary_columns.columns:
        table[column] = df_binary_columns[column]

    return table.drop(axis=1, columns=[columnName])


def extract_age(row):
    (owner_year, owner_month,
     owner_day) = row['owner_year'], row['owner_month'], row['owner_day']
    (loan_year, loan_month, loan_day) = row['year'], row['month'], row['day']
    owner_age = -1
    if owner_year <= loan_year:
        owner_age = loan_year - owner_year
        if owner_month == loan_month:
            if owner_day > loan_day:
                owner_age -= 1
        elif owner_month > loan_month:
            owner_age -= 1
    return owner_age
