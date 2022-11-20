import pandas as pd


def extract_categorical(table, columnName):
    df_binary_columns = pd.get_dummies(table[columnName])
    for column in df_binary_columns.columns:
        table[column] = df_binary_columns[column]

    return table.drop(axis=1, columns=[columnName])
