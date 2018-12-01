from pandas import DataFrame, merge

def max_multiseries(multiseries, lags=[6, 12, 18, 24]):
    '''
    '''

    all_rolled = DataFrame(index=multiseries.index)
    unrolled_cols = [col for col in multiseries.columns if 'lag' in col]
    rolling_windows = lags

    for window in rolling_windows:
        rolled_series = multiseries[unrolled_cols].rolling(window).max()
        rolled_series.columns = ['{}_max_{}'.format(c, window) for c in unrolled_cols]
        all_rolled = merge(all_rolled, rolled_series, left_index=True, right_index=True)

    return all_rolled
