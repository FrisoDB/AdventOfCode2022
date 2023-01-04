# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 01:34:54 2023

@author: friso
"""

import numpy as np
#import networkx as nx
# import time
# tic = time.perf_counter()

file = open('17rockmovestest.txt')
file = open('17rockmoves.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = np.array(list(data0[0]))

jet = np.where(data=='>',1,-1)

#building the rocks
Min = np.ones((1,4), dtype=bool)

Plus = np.zeros((3,3), dtype=bool)
Plus[1] = True
Plus[:,1] = True

Hook = np.ones((3,3), dtype=bool)
Hook[:2,:2] = False

Pole = np.ones((4,1), dtype=bool)

Cube = np.ones((2,2), dtype=bool)

rocks = [Min, Plus, Hook, Pole, Cube]

state = np.zeros((0 ,7))
jetcount = 0
Nrocks = 2022

for i in range(Nrocks):
    #new rock
    rock = rocks[i%len(rocks)]
    height, width = np.shape(rock)
    
    #field grows
    field = np.zeros((height + 3 + np.sum(np.any(state, axis=1)) ,7), dtype=bool)
    field[height+3:] = state[-np.sum(np.any(state, axis=1)):]
    
    y = 2
    pixelsum = np.sum(field) + np.sum(rock)
    
    # rock appears
    state = np.copy(field)
    state[0:height, y:y+width] = rock
    
    for x in range(len(field)):
        #rock moves sideways
        direction = jet[jetcount%len(jet)]
        jetcount += 1
        
        newstate = np.copy(field)
        if np.shape(newstate[x:x+height, y+direction:y+direction+width]) == (height, width):
            newstate[x:x+height, y+direction:y+direction+width] += rock
        if np.sum(newstate) == pixelsum:
            state = np.copy(newstate)
            y += direction

        #rock moves down
        newstate = np.copy(field)
        if np.shape(newstate[x+1:x+1+height, y:y+width]) == (height, width):
            newstate[x+1:x+1+height, y:y+width] += rock

        if np.sum(newstate) == pixelsum:
            state = np.copy(newstate)
        else:
            #rock has landed and frozen, seen in 'state'
            break


answer1 = np.sum(np.any(state, axis=1))


        
        
        
        


