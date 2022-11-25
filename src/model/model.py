from imblearn.over_sampling import RandomOverSampler, ADASYN, SMOTE
from imblearn.under_sampling import ClusterCentroids, EditedNearestNeighbours, AllKNN, RandomUnderSampler, TomekLinks, CondensedNearestNeighbour, OneSidedSelection, NeighbourhoodCleaningRule, InstanceHardnessThreshold
from imblearn.combine import SMOTETomek, SMOTEENN
import pandas as pd


def train_test_split_unbalanced(data, target_column, sampling_strategy="smote_tomek", sort_by_date=True, train_ratio=0.8, random_state=None):
    # order dataset for splitting
    if sort_by_date:
        data = data.sort_values(by=['year', 'month', 'day'])
    else:
        data = data.sample(frac=1, random_state=random_state).reset_index(drop=True)

    # split dataset
    independent = data.drop(target_column, axis=1)
    target = data[target_column]
    train_size = int(len(independent) * train_ratio)
    x_train = independent[:train_size]
    y_train = target[:train_size]
    x_test = independent[train_size:]
    y_test = target[train_size:]

    # balance dataset
    if sampling_strategy != None and sampling_strategy != "":
        match sampling_strategy:
            # oversampling
            case "SMOTE" | "smote":
                sampler = SMOTE(random_state=random_state)
            case "random":
                sampler = RandomOverSampler(random_state=random_state)
            case "adasyn":
                sampler = ADASYN(random_state=random_state)
            # undersampling
            case "centroids":
                sampler = ClusterCentroids(random_state=random_state)
            case "edited_nearest_neighbours":
                sampler = EditedNearestNeighbours()
            case "all_knn":
                sampler = AllKNN()
            case "random_under_sampler":
                sampler = RandomUnderSampler(random_state=random_state)
            case "tomek_links":
                sampler = TomekLinks()
            case "condensed_nearest_neighbour":
                sampler = CondensedNearestNeighbour(random_state=random_state)
            case "one_sided_selection":
                sampler = OneSidedSelection(random_state=random_state)
            case "neighbourhood_cleaning_rule":
                sampler = NeighbourhoodCleaningRule()
            case "instance_hardness_threshold":
                sampler = InstanceHardnessThreshold(random_state=random_state)
            # combined methods
            case "smote_tomek":
                sampler = SMOTETomek(random_state=random_state)
            case "smote_enn":
                sampler = SMOTEENN(random_state=random_state)
            case _:
                raise ValueError("Unknown sampling strategy")
        x_train, y_train = sampler.fit_resample(x_train, y_train)

    return x_train, x_test, y_train, y_test


def self_confidence_score(y_proba):
    l = y_proba.tolist()
    return sum(map(lambda x: 2*abs(x - 0.5), l)) / len(l)
