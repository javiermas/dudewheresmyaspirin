from pandas import DataFrame, merge

def slopes_multiseries(multiseries, lags=[6, 12, 18, 24]):
    '''
    '''

    all_rolled = DataFrame(index=multiseries.index)
    unrolled_cols = ['Investment 1', 'Investment 2', 'Investment 3', 'Investment 4',
        'Investment 5', 'Investment 6', 'Sales 1', 'Sales 2']
    slopes = lags

    for slope in slopes:
        rolled_series = multiseries[unrolled_cols].diff(slope)
        rolled_series.columns = ['{}_slope_{}'.format(c, slope) for c in unrolled_cols]
        all_rolled = merge(all_rolled, rolled_series, left_index=True, right_index=True)

    return all_rolled
