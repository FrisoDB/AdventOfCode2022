# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:50:23 2022

@author: friso
"""

import numpy as np

file = open('15sensortest.txt')
#file = open('15sensors.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('=',' ').replace(',','').replace(':','').split() for line in data0]

loc = np.array([[int(line[3]), int(line[5]), int(line[11]), int(line[13])] for line in data])

dist = abs(loc[:,0]-loc[:,2]) + abs(loc[:,1]-loc[:,3])

xcorrection = -min(min(loc[:,0]),min(loc[:,2])) +np.max(dist)
loc[:,0] += xcorrection
loc[:,2] += xcorrection

sizes= np.max(loc)+2*np.max(dist)

sensors = np.zeros((sizes,sizes),dtype=bool) #later nog wat kloten met sizes en correcties!!
beacons = np.zeros_like(sensors)
coverage = np.zeros_like(sensors)

for i in range(len(loc)):
    #i=6 
    sensors[loc[i,1],loc[i,0]] = True
    beacons[loc[i,3],loc[i,2]] = True
       
    for j in range(dist[i]+1):
        coverage[loc[i,1]+j, (loc[i,0]-dist[i]+j):(loc[i,0]+dist[i]-j+1)] = True
        coverage[loc[i,1]-j, (loc[i,0]-dist[i]+j):(loc[i,0]+dist[i]-j+1)] = True

print(sum(coverage[10])-sum(beacons[10]))


inspect =  coverage[0:21,xcorrection:xcorrection+21]
#inspect[11,14] = True
coordinates = np.where(~inspect)

if np.size(coordinates[0])==0:
    coordinates = [[0],[0]]

print(4*10**6*coordinates[1][0] + coordinates[0][0] )
