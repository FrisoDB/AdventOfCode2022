# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:50:23 2022

@author: friso
estimated to run for maximum 3.5 hours
it took about 2.5 hours
"""

import numpy as np
import time
tic = time.perf_counter()

file = open('15sensortest.txt')
file = open('15sensors.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('=',' ').replace(',','').replace(':','').split() for line in data0]

y_check = int(2e6)    #10 or 2e6
xylimit = int(4e6)    #20 or 4e6

loc = np.array([[int(line[3]), int(line[5]), int(line[11]), int(line[13])] for line in data], dtype=np.int64)

dist = abs(loc[:,0]-loc[:,2]) + abs(loc[:,1]-loc[:,3])

xcorrection = -min(min(loc[:,0]),min(loc[:,2])) +np.max(dist)
loc[:,0] += xcorrection
loc[:,2] += xcorrection

sizes= max(np.max(loc[:,0]),np.max(loc[:,2])) +np.max(dist)

sensors = np.zeros(sizes,dtype=bool)
beacons = np.zeros_like(sensors)
coverage = np.zeros_like(sensors)

for i in range(len(loc)):
    #i=6 
    if loc[i,1]== y_check:
        sensors[loc[i,0]] = True
    if loc[i,3]== y_check:
        beacons[loc[i,2]] = True
        
    j = np.abs(y_check - loc[i,1])
    if 0<=j<=dist[i]:
        coverage[ (loc[i,0]-dist[i]+j):(loc[i,0]+dist[i]-j+1)] = True

#answer1
print(np.sum(coverage)-np.sum(beacons))

#deel2 duurt lang
for y_check in range(xylimit+1):
    coverage = np.zeros_like(sensors)
    
    for i in range(len(loc)):
        #i=6 
        j = np.abs(y_check - loc[i,1])
        if 0<=j<=dist[i]:
            coverage[ (loc[i,0]-dist[i]+j):(loc[i,0]+dist[i]-j+1)] = True
    
    coordinates = np.where(~coverage[xcorrection:xcorrection+xylimit+1])
    
    if np.size(coordinates[0])!=0:
        print(coordinates[0][0], y_check)
        break
    elif y_check%1e4==0:
        print(y_check)
        toc = time.perf_counter()
        print(f"In {toc - tic:0.2f} seconds")
        
#answer2
print(4*10**6*coordinates[0][0] + y_check )
toc = time.perf_counter()
print(f"Finished in {toc - tic:0.2f} seconds")
#it worked: 10457634860779
