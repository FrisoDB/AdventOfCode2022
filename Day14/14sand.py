# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 01:38:21 2022

@author: friso
"""

import numpy as np

#file = open('14structuretest.txt')
file = open('14structure.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('->','').split() for line in data0]

structure = np.zeros((1000,1000), dtype=bool)
for line in data:
    for i in range(len(line)-1):
        x1,y1 = eval(line[i])
        x2,y2 = eval(line[i+1])
        if x1>x2:
            x1,x2 = x2,x1
        elif y1>y2: #rechte lijnen dus elif
            y1,y2 = y2,y1
        structure[y1:y2+1,x1:x2+1] = True
        
floor = 2+ max(  np.arange(1000)[np.any(structure, axis=1)]  )
structure[floor]=True         #uncomment for part2, comment this line for part1

source = 500 #[0,500]

structure_size = np.sum(structure)

while ~structure[0,source]: #check source not blocked
    #always looking 1 space below current sand
    pos = source
    
    for i in range(1,len(structure)):
        if ~structure[i,pos]: #if it can fall down
            continue
        elif ~structure[i,pos-1]: # if it can fall left
            pos -=1
        elif ~structure[i,pos+1]: # if it can fall right
            pos +=1
        else: #it cannot fall at all
            structure[i-1,pos] = True
            break
    else:
        break #after the sand touches the 'infinite' bottom the for loop ends and the while loop must be broken
    
print(np.sum(structure)-structure_size)



