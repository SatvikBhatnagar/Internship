# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 10:10:05 2022

@author: satvi
"""

from ts2vg import HorizontalVG
import matplotlib.pyplot as plt
import plot_graph_horizontal

def hg(ds_ts):
    ts = ds_ts['Close']
    asset_name = ds_ts.loc[0,'Name']

    g = HorizontalVG(directed=None).build(ts)
    ax=plt.gca()
    plot_graph_horizontal.plot_graph(g, ax=ax, title="directed=None", arrow_heads=True)
    
    plt.savefig('../renders/HG - {}'.format(asset_name))
    plt.show()