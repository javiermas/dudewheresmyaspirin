from pandas import DataFrame, merge

def lag_multiseries(multiseries, lags=list(range(1, 12))):
    '''
    '''
    all_lagged = DataFrame(index=multiseries.index)
    unlagged_cols = ['Investment 1', 'Investment 2', 'Investment 3', 'Investment 4',
       'Investment 5', 'Investment 6', 'Sales 1', 'Sales 2']

    for lag in lags:
        lagged_series = multiseries.groupby(['Cluster', 'Brand Group'])[unlagged_cols].shift(lag)
        lagged_series.columns = ['{}_lag_{}'.format(c, lag) for c in unlagged_cols]
        all_lagged = merge(all_lagged, lagged_series, left_index=True, right_index=True)

    return all_lagged

