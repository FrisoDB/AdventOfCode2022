# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:02:40 2022

@author: friso
"""

import numpy as np

# open the data file
file = open("08treeheights.txt")
#file = open("08treetest.txt")
# read the file as a list and make it a numpy array
data = file.readlines()

field = np.array([list(line.strip()) for line in data], dtype=int)

outlook = np.ones_like(field, dtype=int)


#downward
for i in range(len(field)):
    current = field[i]
    if i==(len(field)-1):
        #from the edge you see zero trees
        outlook[i] *= np.zeros_like(current)
    else:
        #start counting
        counter = np.ones_like(current)
        further_counting = np.ones_like(current, dtype=bool)
        for j in range(i+1,len(field)-1):
            test_line = field[j]
            counter += (test_line<current) & further_counting
            further_counting = np.fmin(further_counting, (test_line<current) )
        outlook[i] *= counter
            
#upward
for i in range(len(field)):
    current = field[-i-1]
    if i==(len(field)-1):
        #from the edge you see zero trees
        outlook[-i-1] *= np.zeros_like(current)
    else:
        #start counting
        counter = np.ones_like(current)
        further_counting = np.ones_like(current, dtype=bool)
        for j in range(i+1,len(field)-1):
            test_line = field[-j-1]
            counter += (test_line<current) & further_counting
            further_counting = np.fmin(further_counting, (test_line<current) )
        outlook[-i-1] *= counter        
    
#rightward
for i in range(len(field)):
    current = field[:,i]
    if i==(len(field)-1):
        #from the edge you see zero trees
        outlook[:,i] *= np.zeros_like(current)
    else:
        #start counting
        counter = np.ones_like(current)
        further_counting = np.ones_like(current, dtype=bool)
        for j in range(i+1,len(field)-1):
            test_line = field[:,j]
            counter += (test_line<current) & further_counting
            further_counting = np.fmin(further_counting, (test_line<current) )
        outlook[:,i] *= counter
            
#leftward
for i in range(len(field)):
    current = field[:,-i-1]
    if i==(len(field)-1):
        #from the edge you see zero trees
        outlook[:,-i-1] *= np.zeros_like(current)
    else:
        #start counting
        counter = np.ones_like(current)
        further_counting = np.ones_like(current, dtype=bool)
        for j in range(i+1,len(field)-1):
            test_line = field[:,-j-1]
            counter += (test_line<current) & further_counting
            further_counting = np.fmin(further_counting, (test_line<current) )
        outlook[:,-i-1] *= counter
        
print(outlook.max())


