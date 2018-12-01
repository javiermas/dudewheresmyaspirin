from pandas import DataFrame, merge

def slopes_multiseries(multiseries, lags=[6, 12, 18, 24]):
    '''
    '''

    all_rolled = DataFrame(index=multiseries.index)
    unrolled_cols = [col for col in multiseries.columns if 'lag' in col]
    slopes = lags

    for slope in slopes:
        rolled_series = multiseries[unrolled_cols].diff(slope)
        rolled_series.columns = ['{}_slope_{}'.format(c, slope) for c in unrolled_cols]
        all_rolled = merge(all_rolled, rolled_series, left_index=True, right_index=True)

    return all_rolled
