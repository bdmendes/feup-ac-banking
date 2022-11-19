from imblearn.over_sampling import RandomOverSampler, ADASYN, SMOTE
import pandas as pd


def train_test_split_unbalanced(data, target_column, sampling_strategy="SMOTE", sort_by_date=True, train_ratio=0.8):
    target = data[target_column]
    independent = data.drop(target_column, axis=1)

    # repeat positive targets at the end of the dataset
    match sampling_strategy:
        case "SMOTE" | "smote":
            sampler = SMOTE(random_state=0)
            independent, target = sampler.fit_resample(independent, target)
        case "random" | "RANDOM" | "RandomOverSampler":
            sampler = RandomOverSampler(random_state=0)
            independent, target = sampler.fit_resample(independent, target)
        case "ADASYN" | "adasyn":
            sampler = ADASYN(random_state=0)
            independent, target = sampler.fit_resample(independent, target)
        case "none" | None | "":
            pass

    # order dataset properly for splitting
    data = pd.concat([independent, target], axis=1)
    if sort_by_date:
        data = data.sort_values(by=['year', 'month', 'day'])
    else:
        data = data.sample(frac=1, random_state=0).reset_index(drop=True)
    independent = data.drop(target_column, axis=1)
    target = data[target_column]

    # split dataset
    train_size = int(len(independent) * train_ratio)
    x_train = independent[:train_size]
    y_train = target[:train_size]
    x_test = independent[train_size:]
    y_test = target[train_size:]

    return x_train, x_test, y_train, y_test
