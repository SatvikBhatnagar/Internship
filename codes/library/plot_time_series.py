# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 07:39:56 2022

@author: satvik
"""

import matplotlib.pyplot as plt
import definitions_main
from datetime import datetime


def plot_time_series(ds_ts):

    ds_close = ds_ts['Close']
    ds_dates = ds_ts['Date']
    date_start = ds_ts.iloc[0,0]
    date_last = ds_ts.iloc[-1,0]
    asset_name = ds_ts.loc[0,'Name']
    asset_symbol = ds_ts.loc[0, 'Symbol']

    plt.rcParams["figure.figsize"] = [11.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    x = [datetime.strptime(d, "%d-%m-%Y").date() for d in ds_dates]

    ax = plt.gca()
    ax.plot(x, ds_close)

    year_start = definitions_main.year_extraction_from_date(date_start)
    year_last= definitions_main.year_extraction_from_date(date_last)


    plt.title('{} - ({}) - Time Series - Hourly - {} - {}'.format(asset_name, asset_symbol, year_start, year_last))
    plt.xlabel('Time - Hourly')
    plt.ylabel('Price - Closing (USD)')
    plt.savefig('../renders/Time Series - {}'.format(asset_name))
    plt.show()

    return True
