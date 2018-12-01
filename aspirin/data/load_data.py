import pandas as pd
import calendar


def load_data_and_submissions(data_path, submission_path):
    data = load_data(data_path)
    submission_template = pd.read_csv(submission_path)
    index_cols = ['Cluster', 'Brand Group']
    value_vars = [col for col in submission_template if col not in index_cols]
    submission_template = pd.melt(submission_template, id_vars=index_cols, value_vars=value_vars)
    submission_template = add_date_columns(submission_template)
    submission_template = submission_template.set_index(['Cluster', 'Brand Group', 'date']).drop('value', axis=1)
    submission_template['submission'] = 1
    data_and_submission = pd.merge(data, submission_template, right_index=True, left_index=True, how='outer')
    data_and_submission['submission'] = data_and_submission['submission'].fillna(0).astype(int)
    return data_and_submission


def load_data(data_path):
    data = pd.read_csv(data_path, header=[0, 1, 2, 3], sep=';')
    data = fix_columns(data)
    data = date_columns_to_index(data)
    data['value'] = data['value'].apply(lambda x: float(x.replace(',', '.')) if isinstance(x, str) else x)
    data = function_to_columns(data)
    data = add_date_columns(data.reset_index())
    data = reduce_brands(data)
    data = data.set_index(['Cluster', 'Brand Group', 'date'])
    return data


def fix_columns(data):
    data.columns = [col[3] for col in data.columns]
    data = data[[col for col in data if 'Unnamed' not in col]]
    data = data.rename(columns={' Country': 'Country'})
    return data.drop('Country', axis=1)


def date_columns_to_index(data):
    index_cols = ['Cluster', 'Brand Group', 'Function']
    date_cols = [col for col in data.columns if col not in index_cols]
    data = pd.melt(data, id_vars=index_cols, value_vars=date_cols)
    return data


def function_to_columns(data):
    index_cols = ['Cluster', 'Brand Group', 'variable']
    data = pd.pivot_table(data, columns=['Function'], index=index_cols)
    data.columns = [col[1] for col in data.columns]
    return data


def add_date_columns(data):
    month_dict = {v: k for k, v in enumerate(calendar.month_abbr)}
    data['year'] = data['variable'].apply(lambda x: x.split(' ')[1])
    data['month'] = data['variable'].apply(lambda x: x.split(' ')[0])
    data['month_num'] = data['month'].map(month_dict)
    data['date'] = data.apply(lambda x:
                              pd.Timestamp(year=int(x['year']), month=int(x['month_num']), day=1), axis=1)
    data = data.drop(['variable', 'year', 'month', 'month_num'], axis=1)
    return data


def reduce_brands(data):
    non_other_brands = {
        'Brand Group 17': 'Brand Group 17',
        'Brand Group 24': 'Brand Group 24',
        'Brand Group 30': 'Brand Group 30',
        'Brand Group 31': 'Brand Group 31',
        'Brand Group 36': 'Brand Group 36',
        'Brand Group 41': 'Brand Group 41',
        'Brand Group 96': 'Brand Group 96 97',
        'Brand Group 97': 'Brand Group 96 97',
        'Brand Group 51': 'Brand Group 51, 73, 90',
        'Brand Group 73': 'Brand Group 51, 73, 90',
        'Brand Group 90': 'Brand Group 51, 73, 90',
    }
    other_brands = {
        brand: 'others' for brand in data['Brand Group'].unique()
        if brand not in non_other_brands.keys()
    }
    brand_mapping = {**non_other_brands, **other_brands}
    data['Brand Group'] = data['Brand Group'].map(brand_mapping)
    data = data.groupby(['Cluster', 'Brand Group', 'date']).sum()
    return data.reset_index()
