# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:03:23 2022

@author: friso
"""

import numpy as np

#file = open('09stepstest.txt')
#file = open('09stepstest2.txt')
file = open('09steps.txt')

data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = np.array([line.split() for line in data0])

Nknots = 10         #choose 2 or 10 for part1 or 2 <<<<<<<<---------
pos = np.zeros((Nknots,2), dtype=int) #the positions of each knot

Thist = np.zeros((1000,1000), dtype=bool) #just choose it big enough
Thist[pos[-1,0],pos[-1,1]] = True       #record each position the tail/last knot has been at least once

for line in data:
    
    for i in range(int(line[1])):
        
        #head moves
        if line[0] == 'R':
            pos[0,1] +=1
        elif line[0] == 'L':
            pos[0,1] -=1
        elif line[0] == 'U':
            pos[0,0] +=1
        elif line[0] == 'D':
            pos[0,0] -=1
        
        #tail pieces may move
        for j in range(Nknots-1):
            #checks distance for each knot, maybe moves it and then checks next knot
            if np.any( abs(pos[j]-pos[j+1])>1 ):
                pos[j+1] += np.sign(pos[j]-pos[j+1])
            
        Thist[pos[-1,0],pos[-1,1]] = True

print(sum(sum(Thist)))
            
            
            

