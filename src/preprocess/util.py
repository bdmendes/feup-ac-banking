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
