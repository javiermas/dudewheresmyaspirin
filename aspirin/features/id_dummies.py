import pandas as pd


def compute_id_dummies(data):
    clusters = pd.DataFrame({
        'Cluster': data.index.get_level_values('Cluster'),
    }, index=data.index)
    brands = pd.DataFrame({
        'Brand Group': data.index.get_level_values('Brand Group'),
    }, index=data.index)
    cluster_dummies = pd.get_dummies(clusters)
    brand_dummies = pd.get_dummies(brands)
    features = pd.merge(brand_dummies, cluster_dummies, right_index=True, left_index=True)
    return features
