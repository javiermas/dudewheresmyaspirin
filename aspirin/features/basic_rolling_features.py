import pandas as pd
import numpy as np 


def calculate_rolling_features(data, transaction_function, operation):
    idx = 0

    operation_value = float('nan')
    dates = np.unique(data.index.get_level_values(3))
    brand_groups = np.unique(data.index.get_level_values(1))
    new_df = pd.DataFrame(columns=['Cluster', 'Brand Group', 'date', transaction_function])

    operation_results = []
    for brand in brand_groups:
        for cluster in clusters:
            for date_index_end in range(1, len(dates)):
                date_index_start = 0
                if date_index_end > 12:
                    date_index_start+=1

                # segment based on that specified window gap (max 12 months)
                date_range = dates[date_index_start:date_index_end]
                date_filter = data.index.get_level_values(3).isin(date_range)
                subset = data[date_filter]

                if operation == 'mean':
                    target_column = subset[transaction_function]
                    operation_value = target_column.mean(skipna=True)

                if operation == 'std' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.std(skipna=True)

                if operation == 'var' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.var(skipna=True)

                if operation == 'median' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.median(skipna=True)

                if operation == 'lower_quantile' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.quantile(0.25)

                if operation == 'upper_quantile' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.quantile(0.75)

                if operation == 'IQR' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.quantile(0.75) - target_column.quantile(0.25)

                if operation == 'min' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.min()

                if operation == 'max' :
                    target_column = subset[transaction_function]
                    operation_value = target_column.max()

                new_row = [cluster, brand, dates[date_index_end], operation_value]
                # print(new_row)

                new_df.loc[idx] = new_row
                idx += 1
        new_df = new_df.set_index(['Cluster', 'Brand Group', 'date'])
        return new_df





def calculate_all_basic_rolling_features(data):
    '''
    '''

    function_types = ['Investment 1', 'Investment 2', 'Investment 3', 'Investment 4', 'Investment 5', 'Investment 6',
                      'Sales 1', 'Sales 2']

    db_collection = []


    # rolling mean
    rolling_mean_table = []

    for transaction_function in function_types:
        db = calculate_rolling_features(data, transaction_function, 'mean')
        db_collection.append(db)

    for i in range(0,len(db_store)-1):
        if i == 0:
            rolling_mean_table = pd.concat([db_store[i], db_store[i+1]], axis = 1)
        elif i <len(db_store):
            rolling_mean_table = pd.concat([rolling_mean_table, db_store[i+1]], axis = 1)
        else:
            pass

    # rolling iqr
    db_collection = []
    rolling_iqr_table = []

    for transaction_function in function_types:
        db = calculate_rolling_features(data, transaction_function, 'IQR')
        db_collection.append(db)

    for i in range(0,len(db_store)-1):
        if i == 0:
            rolling_iqr_table = pd.concat([db_store[i], db_store[i+1]], axis = 1)
        elif i <len(db_store):
            rolling_iqr_table = pd.concat([rolling_mean_table, db_store[i+1]], axis = 1)
        else:
            pass

    return rolling_mean_table, rolling_iqr_table
