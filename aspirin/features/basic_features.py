import pandas as pd
import numpy as np

def basic_brand_features(data):
    '''
    function to aggregate features through countries based on brand
    Not using rolling aggregation but just stand-alone stats
    
    input: standardised dataframe
    output: pre-defined dataframe 
    '''
    i = 0
    function_types = ['Investment 1', 'Investment 2', 'Investment 3', 'Investment 4', 'Investment 5', 'Investment 6',
                  'Sales 1', 'Sales 2']

    # create new_df to fill in informations
    new_df = pd.DataFrame(columns = ['Cluster', 'Brand Group', 'date', 'Investment 1 mean', 'Investment 2 mean', 'Investment 3 mean', 'Investment 4 mean',
                                     'Investment 5 mean', 'Investment 6 mean', 'Sales 1 mean', 'Sales 2 mean', 
                                     'Investment 1 std', 'Investment 2 std', 'Investment 3 std', 'Investment 4 std',
                                     'Investment 5 std', 'Investment 6 std', 'Sales 1 std', 'Sales 2 std', 
                                     'Investment 1 var', 'Investment 2 var', 'Investment 3 var', 'Investment 4 var', 
                                     'Investment 5 var', 'Investment 6 var', 'Sales 1 var', 'Sales 2 var',
                                     'Investment 1 median', 'Investment 2 median', 'Investment 3 median', 
                                     'Investment 4 median', 'Investment 5 median', 'Investment 6 median',
                                     'Sales 1 median', 'Sales 2 median', 
                                     'Investment 1 lq', 'Investment 2 lq', 'Investment 3 lq', 'Investment 4 lq',
                                     'Investment 5 lq', 'Investment 6 lq', 'Sales 1 lq', 'Sales 2 lq',
                                     'Investment 1 uq', 'Investment 2 uq', 'Investment 3 uq', 'Investment 4 uq',
                                     'Investment 5 uq', 'Investment 6 uq', 'Sales 1 uq', 'Sales 2 uq', 
                                     'Investment 1 iqr', 'Investment 2 iqr', 'Investment 3 iqr', 'Investment 4 iqr',
                                     'Investment 5 iqr', 'Investment 6 iqr', 'Sales 1 iqr', 'Sales 2 iqr', 
                                     'Investment 1 min', 'Investment 2 min', 'Investment 3 min', 'Investment 4 min', 
                                     'Investment 5 min', 'Investment 6 min', 'Sales 1 min', 'Sales 2 min', 
                                     'Investment 1 max', 'Investment 2 max', 'Investment 3 max', 'Investment 4 max',
                                     'Investment 5 max', 'Investment 6 max', 'Sales 1 max', 'Sales 2 max'                                     
                                    ])
    
    for brand in brand_groups:
        df = data[data.index.get_level_values(1) == brand]
        for time_period in dates:
            df = df[df.index.get_level_values(3) == time_period]
            
            clusters = np.unique(df.index.get_level_values(0))
            for cluster in clusters: 
                df = df[df.index.get_level_values(0) == cluster]
                
                
                basic_features = []
                for func in function_types:
                    basic_features.append(df[func].mean(skipna=True))
                    basic_features.append(df[func].std(skipna=True))
                    basic_features.append(df[func].var(skipna=True))
                    basic_features.append(df[func].median(skipna=True))
                    basic_features.append(df[func].quantile(0.25))
                    basic_features.append(df[func].quantile(0.75))
                    basic_features.append(df[func].quantile(0.75) - df[func].quantile(0.25))
                    basic_features.append(df[func].min(skipna=True))
                    basic_features.append(df[func].max(skipna=True))

                new_row = [cluster, brand, time_period] + basic_features
                # new_row = np.nan_to_num(new_row)
                new_df.loc[i] = new_row
                i += 1
    new_df = new_df.set_index(['Cluster', 'Brand Group', 'date'])            
    return new_df
