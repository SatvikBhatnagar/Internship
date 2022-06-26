# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:17:10 2022

@author: satvi
"""

import networkx as nx
import matplotlib.pyplot as plt
from ts2vg import NaturalVG

import definitions_main

def vg(ds_ts):
    #defining variables
    ts = ds_ts['Close']
    date_start = ds_ts.iloc[0,0]
    date_last = ds_ts.iloc[-1,0]
    asset_name = ds_ts.loc[0,'Name']
    asset_symbol = ds_ts.loc[0, 'Symbol']
    ###################

    #build visibility graph
    g = NaturalVG(directed=None).build(ts)
    nxg = g.as_networkx()
    ###################

    #make plots
    plt.rcParams["figure.figsize"] = [100, 30]
    plt.rcParams["figure.autolayout"] = True


    graph_plot_options = {
        'with_labels': False,
        'node_size': 2,
        'node_color': [(0, 0, 0, 1)],
        'edge_color': [(0, 0, 0, 0.15)]
        }

    ax = plt.gca()
    nx.draw_networkx(nxg, ax = ax, pos=g.node_positions(), **graph_plot_options)

    ax.plot(ts)

    year_start = definitions_main.year_extraction_from_date(date_start)
    year_last= definitions_main.year_extraction_from_date(date_last)


    plt.title('Visibility Graph{} - ({}) - Time Series {} - {}'.format(asset_name, asset_symbol, year_start, year_last))
    plt.show()
