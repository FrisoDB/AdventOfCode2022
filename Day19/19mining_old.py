# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:08:15 2023

@author: friso
#veel te traag, geen oplossingsrichting
"""

import numpy as np


def mining(time, robots, storage, max_geodes):
    if time==0:
        return storage[-1]
    pot_geodes = storage[-1]+ time* robots[-1] + time*(time-1)/2
    if pot_geodes<=max_geodes:
        return 0
    
    #no new robots
    geodes = [0]
    #consider making new robot
    for i in reversed(range(len(prices))):
        price = prices[i]
        if np.all((storage-price)>=0):
            newrobot = np.zeros(4, dtype=int)
            newrobot[i] = 1
            geodes.append( mining(time-1, robots+newrobot, storage-price+robots, max(geodes)))
    geodes.append( mining(time-1, robots, storage+robots, max(geodes)))
    
    return max(geodes)


#inlezen prijzen robots/blueprints


#loop over blueprints regelen



prices = np.array([[4,0,0,0],[2,0,0,0],[3,14,0,0],[2,0,7,0]], dtype=int)

storage = np.zeros(4, dtype=int)

robots = np.array([1,0,0,0], dtype=int)

starttime = 24

test = mining(starttime, robots, storage, 0)


