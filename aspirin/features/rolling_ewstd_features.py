from pandas import DataFrame, merge

def rolling_ewstd_multiseries(multiseries, lags=[6, 12, 18, 24]):
    '''
    '''

    all_rolled = DataFrame(index=multiseries.index)
    unrolled_cols = ['Investment 1', 'Investment 2', 'Investment 3', 'Investment 4',
        'Investment 5', 'Investment 6', 'Sales 1', 'Sales 2']
    rolling_windows = lags

    for window in rolling_windows:
        rolled_series = multiseries[unrolled_cols].ewm(span=window).std()
        rolled_series.columns = ['{}_ewstd_{}'.format(c, window) for c in unrolled_cols]
        all_rolled = merge(all_rolled, rolled_series, left_index=True, right_index=True)

    return all_rolled
