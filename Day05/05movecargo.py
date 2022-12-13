# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:22:53 2022

@author: friso
"""

# open the data file
#file = open("05stacktest.txt")
file = open("05stack.txt")
# read the file as a list and make it a numpy array
data0 = file.readlines()

data0.reverse()
Nstacks = (len(data0[0])+1)//4
stack = [ [] for i in range(Nstacks)  ]

for line in data0:
    for i in range(Nstacks):
        if line[i*4]=='[':
            stack[i].append(line[i*4+1])            
            
# open the data file
#file = open("05movestest.txt")
file = open("05moves.txt")
# read the file as a list and make it a numpy array
data1 = file.readlines()

a = [line.split() for line in data1]
moves = [ [int(line[1]),int(line[3]),int(line[5])] for line in a ]

for move in moves:
    for i in range(move[0]):
        stack[move[2]-1].append(stack[move[1]-1][-1])
        stack[move[1]-1].pop()

stacktop = ''
for i in range(Nstacks):
    stacktop = stacktop + stack[i][-1]

print(stacktop)



