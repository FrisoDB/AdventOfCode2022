# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:16:45 2022

@author: friso
"""

import numpy as np

#file = open('10cyclestest.txt')
#file = open('10cyclestest2.txt')
file = open('10cycles.txt')

data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.split() for line in data0]

cycle = 1
Xs = np.ones(2*len(data)+1, dtype=int)

for line in data:
    if line[0] == 'noop':
        cycle += 1
    elif line[0] == 'addx':
        cycle += 2
        Xs[cycle:] = Xs[cycle] + int(line[1])

sig = np.arange(0,len(Xs), dtype=int) *Xs

answer = [sig[i] for i in range(20, 230, 40)]
print(sum(answer))

###

tekst0 = [ (i%40 in range(Xs[i+1]-1,Xs[i+1]+2))  for i in range(240) ]

tekst = np.reshape(tekst0, (6,40)) #RBPARAGF




 