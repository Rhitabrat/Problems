#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:18:11 2019

@author: rhitik
"""

import csv

# creating list
items = []

# opening a file
with open('Data.csv') as f:
    reader = csv.reader(f)
    
    rowN = 1;
    for row in reader:
        if rowN>=1:
            items.append(row[0])
            
        rowN = rowN + 1

print(items)

def countItem(items, x):    
    count = 0
    for item in items:
        if(item == x):
            count = count + 1
        
    return count
    
print(countItem(items, 'orange'))