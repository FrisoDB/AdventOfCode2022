# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:50:23 2022

@author: friso

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

dist = np.abs(loc[:,0]-loc[:,2]) + np.abs(loc[:,1]-loc[:,3])

xcorrection = -min(np.min(loc[:,0]),np.min(loc[:,2])) +np.max(dist)
loc[:,0] += xcorrection
loc[:,2] += xcorrection

sizes= max(np.max(loc[:,0]),np.max(loc[:,2])) +np.max(dist)

coverage = np.zeros(sizes,dtype=bool)
#sensors = 0
beacons = np.zeros_like(coverage)


for i in range(len(loc)):
    #i=6 
    # if loc[i,1]== y_check:
    #     sensors += 1
    if loc[i,3]== y_check:
        beacons[loc[i,2]] = True
        
    j = np.abs(y_check - loc[i,1])
    if 0<=j<=dist[i]:
        coverage[ (loc[i,0]-dist[i]+j):(loc[i,0]+dist[i]-j+1)] = True

#answer1
answer1 = np.sum(coverage)-np.sum(beacons)
print(answer1)


loc[:,0] -= xcorrection
loc[:,2] -= xcorrection

sensors = np.concatenate((loc[:,:2],dist[:,None]+1), axis =1)

for sensor in sensors:
#sensor = np.array([2920303, 3059306,  504422])
    #vier zijden van ruit opbouwen
    j = np.arange(0,sensor[2], dtype=int)
    rand = np.zeros((4*sensor[2],2), dtype=int)
    rand[0:sensor[2],0] = sensor[0]+j
    rand[0:sensor[2],1] = sensor[1]+sensor[2]-j
    rand[sensor[2]:2*sensor[2],0] = sensor[0]-j
    rand[sensor[2]:2*sensor[2],1] = sensor[1]-sensor[2]+j   
    rand[2*sensor[2]:3*sensor[2],0] = sensor[0]+sensor[2]-j
    rand[2*sensor[2]:3*sensor[2],1] = sensor[1]-j
    rand[3*sensor[2]:4*sensor[2],0] = sensor[0]-sensor[2]+j
    rand[3*sensor[2]:4*sensor[2],1] = sensor[1]+j    

    #filteren op zoekgebied
    to_remove = np.any( (0>rand) + (rand>xylimit) , axis=1)
    rand = rand[~to_remove]

    #filteren op groot genoeg afstand ten opzichte van ALLE sensoren
    for test_sensor in sensors:
        test_dist = np.abs(test_sensor[0]-rand[:,0]) + np.abs(test_sensor[1]-rand[:,1])
        rand = rand[(test_dist >= test_sensor[2])]

    if len(rand)>0:
        coordinates = rand[0].astype('int64')
        break

answer2 = 4*10**6 *coordinates[0] + coordinates[1]
print(answer2)
#104....779