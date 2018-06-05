#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:27:36 2018

@author: AveryMavroudis
"""
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import geopy.distance as dist

locations = pd.read_csv('./locations/data/locations.csv')


#Subsetting with a single user
user53535 = locations.loc[(locations.id == 53535),('latitude','longitude')]

#DBSCAN with user 53535
db = DBSCAN(eps = 0.1, min_samples = 5).fit(user53535)
user53535['clusters'] = db.labels_
clusters = user53535.groupby('clusters').agg([np.mean, np.size])
clusters.columns = ['latitude', 'size0', 'longitude', 'size']
clusters.drop(columns = 'size0')

def cluster(locations):
    coordinates = locations[['latitude','longitude']]
    db = DBSCAN(eps = 0.1, min_samples = 5).fit(coordinates)
    coordinates['cluster'] = db.labels_
    