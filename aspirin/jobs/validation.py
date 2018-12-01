from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import TimeSeriesSplit

def validate_single_model(data, model):
    '''
    '''
    list_mapes = []
    X = data.drop('Sales 2', axis=1)
    y = data['Sales 2']
    tscv = TimeSeriesSplit(n_splits=6)
    for train_index, test_index in tscv.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        list_mapes.append(mean_absolute_error(y_test+1e-2, y_pred))

    return list_mapes

def validate_multiple_models(data, models):
    errors_dict = dict()
    count = 0
    for model, parameters in models:
        model = model(**parameters)
        errors_dict[model.__class__.__name__ + str(parameters)] = validate_single_model(data, model)
        count += 1

    return errors_dict
