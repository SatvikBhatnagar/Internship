# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:20:14 2022

@author: satvik
"""
import time
start_time = time.time()
import pandas as pd
import glob

import sys
sys.path.insert(0, './library')
import plot_time_series
import visibility_graph
import horizontal_visibility_graph
import degree_distribution

commodities = '../dataset/commodities/*.csv'
tech_stocks = '../dataset/tech_stocks/*.csv'
crypto = '../dataset/crypto/*.csv'
forex = '../dataset/forex/*.csv'

assets = [crypto, commodities, forex]

for asset in assets:
    for file_ in glob.glob(asset):
        ds_ts = pd.read_csv(file_, infer_datetime_format=True, low_memory=False)
        
        ### plotting time series
        print("Time Series of {} is on its way!".format(file_))
        success = plot_time_series.plot_time_series(ds_ts)
        if success:
            print(file_, "is successfully plotted")
        else:
            print(file_, "is not plotted due to an error")
        ############################
        
        ### plotting VG
        print("VG of {} is on its way!".format(file_))
        success = visibility_graph.vg(ds_ts)
        if success:
            print(file_, "'s VG has been successfully generated and saved")
        else:
            print(file_, "'s VG has beenhas not been generated")
        
        
        ### plotting degree distribution
        print("Degree Distribution of {} is on its way!".format(file_))
        success = degree_distribution.dd(ds_ts)
        if success:
            print(file_, "'s Degree Distribution has been successfully generated and saved")
        else:
            print(file_, "'s Degree Distribution has not been generated")
        '''
        ###horizontal visibility graph
        print("HG of {} is on its way!".format(file_))
        success = horizontal_visibility_graph.hg(ds_ts)
        if success:
            print(file_, "'s HG has been successfully generated and saved")
        else:
            print(file_, "'s HG has beenhas not been generated")
        '''
print("--- %s seconds ---" % (time.time() - start_time))