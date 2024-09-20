import numpy as np
# import matplotlib.pyplot as plt
from sklearn.cluster import HDBSCAN
import pandas as pd

def cluster():
    url = "./../Accident Data Analysis/Copy_of_AccidentReports.csv"
    data = pd.read_csv(url)
    data = data[['Latitude', 'Longitude']]
    data = data[(data['Latitude']!=0.0) & (data['Longitude']!=0.0)]
    data = data[(data['Latitude']<=14) & (data['Latitude']>=13) & (data['Longitude']<=78)& (data['Longitude']>=76)]

    X = data.to_numpy()
    model = HDBSCAN(min_cluster_size=10).fit(X)

    clusters = model.labels_

    data['color'] = clusters
    return data



