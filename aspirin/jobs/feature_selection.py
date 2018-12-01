import operator
from sklearn.feature_selection import mutual_info_regression

def compute_mutual_information_importance(data, target, k):
    X = data.drop(target, axis=1)
    y = data[target]
    mi = mutual_info_regression(X, y)
    mi_dict = dict(zip(X.columns, mi))
    sorted_mi_dict = sorted(mi_dict.items(), key=operator.itemgetter(1), reverse=True)
    return [i[0] for i in sorted_mi_dict[:k]]

