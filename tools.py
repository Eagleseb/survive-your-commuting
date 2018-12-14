#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:33:11 2018

@author: mlt

Some tools
"""

import pandas as pd


def plot_distrib(acc, group = "Day_of_Week", colname = 'index', ax = None, leg = ""):
    """
    Plot the distribution of colname per group for a given dataframe acc
    """
    if colname == 'index':
        acc[acc[group] != -1].groupby([group]).count().iloc[:,0].plot.bar(x = group, 
                                                       title = "Accidents distribution per {} {}".format(group, leg),
                                                       ax = ax)
    else:
        acc[acc[group] != -1].groupby([group])[colname].sum().plot.bar(x = group, 
                                                     title = "{} distribution per {} {}".format(colname, group, leg),
                                                     ax = ax)                        


