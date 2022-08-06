# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:20:14 2022

@author: satvik
"""

import pandas as pd
import glob

import sys
sys.path.insert(0, './library')
import plot_time_series
import visibility_graph
import degree_distribution

commodities = '../dataset/commodities/*.csv'
tech_stocks = '../dataset/tech_stocks/*.csv'
crypto = '../dataset/crypto/*.csv'
forex = '../dataset/forex/*.csv'

assets = [crypto, commodities, forex]

for asset in assets:
    for file_ in glob.glob(asset):
        ds_ts = pd.read_csv(file_, infer_datetime_format=True, low_memory=False)

        '''### plotting time series
        success = plot_time_series.plot_time_series(ds_ts)
        if success:
            print(file_, "is successfully plotted")
        else:
            print(file_, "is not plotted due to an error")
        ############################

        ### degree distribution
        visibility_graph.vg(ds_ts)'''

        ### plotting degree distribution
        degree_distribution.dd(ds_ts)
