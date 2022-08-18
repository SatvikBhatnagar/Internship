# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 23:44:25 2022

@author: satvi
"""

from ts2vg import NaturalVG
import matplotlib.pyplot as plt

def dd(ds_ts):
    #defining variables
    ts = ds_ts['Close']
    asset_name = ds_ts.loc[0,'Name']


    #build visibility graph
    g = NaturalVG().build(ts, only_degrees=True)

    #get degree distribution
    ks, ps = g.degree_distribution

    #make plots
    fig, [ax0, ax1] = plt.subplots(ncols=2, figsize=(12, 3.5))

    ax0.scatter(ks, ps, s=2, c='#000', alpha=1)
    ax0.set_title('Degree Distribution - {}'.format(asset_name))
    ax0.set_xlabel('k')
    ax0.set_ylabel('P(k)')

    ax1.scatter(ks, ps, s=2, c='#000', alpha=1)
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax1.set_title('Degree Distribution (log-log) - {}'.format(asset_name))
    ax1.set_xlabel('k')
    ax1.set_ylabel('P(k)')
    
    plt.savefig('../renders/Degree Distibution - {}'.format(asset_name))
