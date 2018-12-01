import pandas as pd
import calendar


def load_data(path='../data/Data_Novartis_Datathon-Participants.csv'):
    data = pd.read_csv(path, header=[0, 1, 2, 3], sep=';')
    data.columns = [col[3] for col in data.columns]
    data = data[[col for col in data if 'Unnamed' not in col]]
    data = data.rename(columns={' Country': 'Country'})
    index_cols = ['Cluster', 'Brand Group', 'Country', 'Function']
    date_cols = [col for col in data.columns if col not in index_cols]
    data = pd.melt(data, id_vars=index_cols,value_vars=date_cols)
    data['value'] = data['value'].apply(lambda x: float(x.replace(',', '.')) if isinstance(x, str) else x)
    index_cols = ['Cluster', 'Brand Group', 'Country', 'variable']
    data = pd.pivot_table(data, columns=['Function'], index=index_cols)
    data.columns = [col[1] for col in data.columns]
    month_dict = {v: k for k,v in enumerate(calendar.month_abbr)}
    data = data.reset_index()
    data['year'] = data['variable'].apply(lambda x: x.split(' ')[1])
    data['month'] = data['variable'].apply(lambda x: x.split(' ')[0])
    data['month_num'] = data['month'].map(month_dict)
    data['date'] = data.apply(lambda x: pd.Timestamp(year=int(x['year']), month=int(x['month_num']), day=1), axis=1)
    data = data.drop('variable', axis=1)
    data = data.set_index(['Cluster', 'Brand Group', 'Country', 'date'])
    return data
