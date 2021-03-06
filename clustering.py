#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:27:36 2018

@author: AveryMavroudis
"""
import sys
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN

def cluster(locations):
    coordinates = locations[['latitude','longitude']]
    db = DBSCAN(eps = 0.1, min_samples = 5).fit(coordinates)
    coordinates['cluster'] = db.labels_
    clusters = coordinates.groupby('cluster').agg([np.mean, np.size])
    clusters.columns = ['latitude', 'density0', 'longitude', 'density']
    clusters = clusters.drop(columns = 'density0')
    return clusters
    
def locations_csv(data, file_name = ""):
    by_ID = data.groupby('id')
    all_clusters = by_ID.apply(cluster)
    all_clusters = all_clusters.reset_index(level = ['id','cluster'])
    outliers_rm = all_clusters.drop(all_clusters[all_clusters.cluster == -1].index)
    max_cluster = outliers_rm.groupby('id').apply(max)
    locations = max_cluster.drop(columns = 'cluster')
    locations.to_csv(file_name, index = False)

if len(sys.argv) == 3:
    locations = pd.read_csv(sys.argv[1])
    locations_csv(locations, sys.argv[2])
else:
    print("usage: python clustering.py input.csv output.csv ")   
    print("For more information, please visit https://github.com/averymavroudis/locations_python")
    
    