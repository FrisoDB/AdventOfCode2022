# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:54:40 2023

@author: friso
"""

import re
import numpy as np
from queue import Queue
import time
tic = time.perf_counter()


def hash_state(state):
    time,robots,storage = state
    h = str(time)+'_'
    for i in robots:
        h += '_'+str(i)
    h += '_'
    for i in storage:
        h += '_'+str(i)
    return h

def max_geodes(blueprint, timemax):
    max_robots = np.max(blueprint, axis=0)
    
    robots = np.array([1,0,0,0], dtype=int)
    storage = np.zeros(4, dtype=int)
    time = 0
    start = (time,robots,storage)
    
    states = { hash_state(start) }
    geodes_max = 0
    q = Queue()
    q.put(start)
    
    while not q.empty():
        # get a state from the queue
        time, robots, storage = q.get()
        # minimal geodes you can get from this state
        geodes_minimal_possible = storage[-1] + robots[-1]*(timemax-time)
        if geodes_minimal_possible > geodes_max:
            geodes_max = geodes_minimal_possible
        
        for i in range(len(robots)):
            price = blueprint[i]
            needed = price - storage
            time_gathering = [0,0,0,0]
            for j in range(len(price)):
                if (needed[j]>0) and robots[j]: # if robots[j]!=0 there is at least one robot producing
                    time_gathering[j] = needed[j]//robots[j] + int(needed[j]%robots[j]>0)
                elif needed[j]>0:  # needed but no robots producing 
                    time_gathering[j] = timemax+1 # make it bigger than remaining time
                # else: storage has enough of material, so zero time needed gathering
            dt = max(time_gathering) # time go gather enough resources to build this robot[i]
            
            if (time+dt+1+1) <= timemax: #enough time to build new robot and let it produce at least once
                storage_new = storage + (dt+1)* robots - price
                robots_new = np.copy(robots)
                robots_new[i] += 1
                
                #if not ( robots_new <= max_robots )[:3].all() : # do not consider geodes 
                if (robots_new > max_robots)[:3].any() : 
                    # check whether a new robot is even needed
                    # a production (and thus Nrobots) bigger than maximum price cannot be spend,
                    # as only one robot can be build each minute
                    continue
                
                t_after = timemax - (time+dt+1)     # time left after building new robot
                # most optimistic scenario of only adding geode robots, 
                # not considering if there will always be resources to build geode robots
                geodes_max_potential = storage_new[-1] + t_after*robots_new[-1] + ((t_after-1)*t_after)//2
                if geodes_max_potential<=geodes_max:
                    continue
                
                # queue new state
                state_new = (time+dt+1,robots_new,storage_new)
                h = hash_state(state_new)
                if h not in states:
                    q.put(state_new)
                    states.add(h)
    
    return geodes_max

file = open('19miningtest.txt')
file = open('19miningrobots.txt')
datanumbers = [ [int(i) for i in re.findall("\d+",line)] for line in file.readlines()]

blueprints = []
for line in datanumbers:
    blueprints.append(np.array([[line[1], 0, 0, 0],
                                [line[2], 0, 0, 0],
                                [line[3], line[4], 0, 0],
                                [line[5], 0, line[6], 0] ]))
blueprints = np.array(blueprints)

geodes_maxima1 = np.zeros(len(blueprints),dtype=int)
for i,blueprint in enumerate(blueprints):
    timemax = 24
    geodes_maxima1[i] = max_geodes(blueprint,timemax)

quality_levels1 = (np.arange(len(blueprints), dtype=int)+1)*geodes_maxima1
#answer1
print(np.sum(quality_levels1))

toc = time.perf_counter()
print(f"Part 1 in {toc - tic:0.2f} seconds")

tic = time.perf_counter()
geodes_maxima2 = np.zeros(3,dtype=int)
for i,blueprint in enumerate(blueprints[:3]):
    timemax = 32
    geodes_maxima2[i] = max_geodes(blueprint,timemax)
    print(f"Part 2 blueprint {i+1} done.")
#answer2
print(np.prod(geodes_maxima2))

toc = time.perf_counter()
print(f"Part 2 in {toc - tic:0.2f} seconds")

