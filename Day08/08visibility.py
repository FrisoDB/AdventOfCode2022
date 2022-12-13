# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 00:50:15 2022

@author: friso
"""

import numpy as np

# open the data file
file = open("08treeheights.txt")
#file = open("08treetest.txt")
# read the file as a list and make it a numpy array
data = file.readlines()


field = np.array([list(line.strip()) for line in data], dtype=int)
visible_updown = np.zeros_like(field, dtype=bool)
visible_leftright = np.zeros_like(field, dtype=bool)

# up down
visible_updown[0] = visible_updown[-1] = True
pref_up = field[0]
pref_down = field[-1]

for i in range(1,len(field)):
     visible_updown[i] += (pref_up<field[i])
     pref_up = np.fmax(pref_up, field[i])
     visible_updown[-i-1] += (pref_down<field[-i-1])
     pref_down = np.fmax(pref_down, field[-i-1])
     
#leftright
visible_leftright[:,0] = visible_leftright[:,-1] = True
pref_left = field[:,0]
pref_right = field[:,-1]

for i in range(1,len(field)):
    visible_leftright[:,i] += (pref_left<field[:,i])
    pref_left = np.fmax(pref_left, field[:,i])
    visible_leftright[:,-i-1] += (pref_right<field[:,-i-1])
    pref_right = np.fmax(pref_right, field[:,-i-1])
    
visible = visible_leftright + visible_updown

print(sum(sum(visible)))
    


