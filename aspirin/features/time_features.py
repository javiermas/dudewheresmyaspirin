from pandas import concat, DataFrame, get_dummies
from numpy import sin, pi, cos

def add_time_columns(df, add_month=True, add_year=True, add_season=True,
        add_trigonometries=True, add_dummies=True):
    '''
    '''
    time_columns = ['year', 'month', 'season']
    new_df = DataFrame(data=None, index=df.index)
    if add_year:
        new_df['year'] = new_df.index.get_level_values(0).year

    if add_month:
        new_df['month'] = new_df.index.get_level_values(0).month
        new_df['daysinmonth'] = new_df.index.get_level_values(0).daysinmonth
        if add_trigonometries:
            new_df['month_sin'] = new_df.month\
                    .apply(lambda dtmonth: sin(2 * dtmonth * pi) / 12)
            new_df['cos_month'] = new_df.month\
                    .apply(lambda dtmonth: cos(2 * dtmonth * pi) / 12)

    if add_season:
        new_df['season'] = new_df.month\
                .apply(lambda dtmonth: (dtmonth % 12 + 3) // 3)
        if add_trigonometries:
            new_df['season_sin'] = new_df.season\
                    .apply(lambda dtseason: sin(2 * dtseason * pi) / 4)
            new_df['season_cos'] = new_df.season\
                    .apply(lambda dtseason: sin(2 * dtseason * pi) / 4)

    if add_dummies:
        time_columns = ['year', 'month', 'season']
        for column in time_columns:
            new_df = concat([new_df, get_dummies(new_df[column],
                            prefix = str(column), drop_first=False)], axis=1)

    return new_df
