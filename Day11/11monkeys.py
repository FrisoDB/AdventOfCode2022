# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:10:40 2022

@author: friso
"""

import numpy as np
import time
tic = time.perf_counter()

#file = open('11monkeystest.txt')
file = open('11monkeys.txt')

data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace(',','').split() for line in data0]

Monkeys = []
for i in range( (len(data)+1)//7 ):
    monkey = [ [ np.int64(data[1+i*7][j]) for j in range(2,len(data[1+i*7]))] ]
    #int64 to prevent overflow, big integers
    monkey.append(''.join(data[2+i*7][3:]) )
    monkey.append(int(data[3+i*7][-1]))
    monkey.append(int(data[4+i*7][-1]))
    monkey.append(int(data[5+i*7][-1]))
    monkey.append(0) #inspections counter
    Monkeys.append(monkey)

# options for part 1 or 2    
Nrounds = 20     #choose 10**4 or 20
destress = 3       #choose 1 or 3
bigdif = np.prod([monkey[2] for monkey in Monkeys])

for r in range(Nrounds):
    for monkey in Monkeys:
        for old in monkey[0]:
            new = (eval(monkey[1])//destress) % bigdif
            if (new% monkey[2]==0):
                Monkeys[monkey[3]][0].append(new)
            else:
                Monkeys[monkey[4]][0].append(new)
        monkey[-1] += len(monkey[0]) #add inspections
        monkey[0] = []

counts = [monkey[-1] for monkey in Monkeys]
counts.sort()
print(counts[-1],counts[-2], counts[-1]*counts[-2])   

toc = time.perf_counter()
print(f"In {toc - tic:0.4f} seconds")
