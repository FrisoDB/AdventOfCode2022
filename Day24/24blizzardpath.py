# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 16:08:43 2023

@author: friso
"""

import numpy as np
import time
tic = time.perf_counter()

def visualise_field(cur_blizs, walls, E):
    field = np.empty((len(data),len(data[0])), dtype=str)
    for bliz in cur_blizs:
        if np.all(bliz[2:]==[0,1]):
            field[bliz[0],bliz[1]] = '>'
        elif np.all(bliz[2:]==[0,-1]):
            field[bliz[0],bliz[1]] = '<'
        elif np.all(bliz[2:]==[1,0]):
            field[bliz[0],bliz[1]] = 'v'
        elif np.all(bliz[2:]==[-1,0]):
            field[bliz[0],bliz[1]] = '^'
    for wall in walls:
        field[wall[0],wall[1]] = '#'
    field[E[0],E[1]] = 'E'
    return field


file = open('24blizzardsdummy.txt')
file = open('24blizzardstest.txt')
file = open('24blizzards.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('\n','') for line in data0]

#gather positions blizzards and walls
blizzards = []
walls = [[-1,1]] #plug one hole
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]=='#':
            walls.append([i,j])
        elif data[i][j]=='>':
            blizzards.append([i,j,0,1])
        elif data[i][j]=='<':
            blizzards.append([i,j,0,-1])
        elif data[i][j]=='v':
            blizzards.append([i,j,1,0])
        elif data[i][j]=='^':
            blizzards.append([i,j,-1,0])

cur_blizs = np.array(blizzards)

#define start, finish, goals and more
start = (0,1)
finish = (len(data)-1, data[-1].index('.')) #plug another hole
walls.append([finish[0]+1,finish[1]])
goal = [finish, start, finish]
Nreached = 0     #how many (sub)goals are reached
Es = {start}
answer = []

Nrounds = 1000
for r in range(Nrounds):
    #calculate next positions blizzards
    next_blizs = cur_blizs[:,:2] + cur_blizs[:,2:]
    for i in range(len(next_blizs)):
        x,y = next_blizs[i,0:2]
        if x==0:
            next_blizs[i,0] = len(data)-2
        elif x==len(data)-1:
            next_blizs[i,0] = 1
        elif y==0:
            next_blizs[i,1] = len(data[0])-2
        elif y==len(data[0])-1:
            next_blizs[i,1] = 1
    #field = visualise_field(cur_blizs, walls, [0,1])
    
    #gather next positions Expidition
    next_Es = set()
    next_blizs2= next_blizs.tolist()
    for E in Es:
        x,y = E
        pot_Es = [[x-1,y], [x,y], [x+1,y], [x,y-1], [x,y+1]]
        for new_E in pot_Es:
            if (new_E not in next_blizs2) and (new_E not in walls):
                next_Es.add(tuple(new_E))
    
    #prepare for next minute
    cur_blizs[:,0:2] = next_blizs
    Es = next_Es
    
    if goal[Nreached] in Es:
        toc = time.perf_counter()
        print(f"Finished in {toc - tic:0.2f} seconds at {finish} after {r+1} rounds.")
        answer.append(r+1)
        if Nreached== len(goal)-1:
            break
        Es = {goal[Nreached]}
        Nreached += 1
        print(f"Started from {Es} toward {goal[Nreached]}.")

   
print(f"\n Answer 1 is {answer[0]}. \n Answer 2 is {answer[2]}.")

