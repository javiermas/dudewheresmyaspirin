from functools import reduce
import pandas as pd


def pipeline(data, preprocessors=[], features=[]):
    for preprocessor in preprocessors:
        data = preprocessor(data)

    feature_data = list()
    for feature in features:
        feature_data.append(feature(data))

    feature_dataframe = join_list_of_dataframes(feature_data)
    return feature_dataframe


def join_list_of_dataframes(list_of_dataframes):
    feature_dataframe = reduce(lambda l, r: pd.merge(l, r, left_index=True, right_index=True, how='outer'),
                               list_of_dataframes)
    return feature_dataframe
