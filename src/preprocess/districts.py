import numpy as np


def preprocess_districts(districts):
    districts["no. of commited crimes '95"] = np.where(districts["no. of commited crimes '95"].eq(
        "?"), districts["no. of commited crimes '96"], districts["no. of commited crimes '95"])
    districts = districts.astype(
        {"no. of commited crimes '95": int, "no. of commited crimes '96": int})
    districts["crime_growth"] = districts["no. of commited crimes '96"] / \
        districts["no. of commited crimes '95"]

    districts["unemploymant rate '95"] = np.where(districts["unemploymant rate '95"].eq(
        "?"), districts["unemploymant rate '96"], districts["unemploymant rate '95"])
    districts = districts.astype(
        {"unemploymant rate '95": float, "unemploymant rate '96": float})
    districts["unemploymant_growth"] = districts["unemploymant rate '96"] / \
        districts["unemploymant rate '95"]

    districts.drop(axis=1, columns=["no. of commited crimes '95", "unemploymant rate '95", "no. of municipalities with inhabitants < 499", "no. of municipalities with inhabitants 500-1999",
                   "no. of municipalities with inhabitants 2000-9999", "no. of municipalities with inhabitants 2000-9999", "no. of municipalities with inhabitants >10000", "name", "region"], inplace=True)
    districts["no. of enterpreneurs per 1000 inhabitants"] = districts["no. of enterpreneurs per 1000 inhabitants"] / 1000
    districts.rename({"code": "district_id", "no. of inhabitants": "district_no_inhabitants", "no. of cities": "district_no_cities", "ratio of urban inhabitants": "district_urban_inhabitants_ratio", "average salary": "district_average_salary", "unemploymant_growth": "district_unemploymant_growth",
                     "crime_growth": "district_crime_growth", "no. of enterpreneurs per 1000 inhabitants": "districts_entrepreneurs_ratio", "unemploymant rate '96": "district_unemployment_rate", "no. of commited crimes '96": "district_crimes_per_year"}, axis=1, inplace=True)
    districts['district_crimes_per_year'] = districts['district_crimes_per_year'].astype(
        int) / districts['district_no_inhabitants']
    districts.rename(
        {"district_crimes_per_year": "district_crimes_per_inhabitant"}, axis=1, inplace=True)

    return districts
