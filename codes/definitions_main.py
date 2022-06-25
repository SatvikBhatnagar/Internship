# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 22:25:33 2022

@author: satvik
"""

from datetime import datetime

def year_extraction_from_date(date):
    date = date[::-1]
    date = date[:4]
    date = date[::-1]
    return date
