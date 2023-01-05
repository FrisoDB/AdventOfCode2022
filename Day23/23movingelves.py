# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 13:51:40 2023

@author: friso
second part calculation takes long
"""
import numpy as np
import time
tic = time.perf_counter()

def spots_empty(spots):
    return not any( spot in elves.values() for spot in spots )

def visualise_field(values):
    xs = {x for (x,y) in values}
    xcor = -min(xs)
    xsize = max(xs)+1 +xcor
    ys = {y for (x,y) in values}
    ycor = -min(ys)
    ysize = max(ys)+1 +ycor

    field = np.zeros((xsize,ysize), dtype=bool)
    for x,y in values:
        field[x+xcor,y+ycor] = True
    return field
    

file = open('23elvessmalltest.txt')
file = open('23elvestest.txt')
file = open('23elves.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('\n','') for line in data0]

elves = dict()
number = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        if data[x][y]=='#':
            elves[number] = (x,y)
            number += 1

Nrounds = 1000 #10 for first part, 1000 for second part
for r in range(Nrounds):
    proposed = dict()
    for elf in elves:
        x,y = elves[elf]
        surrounding = [(x-1,y-1), (x-1,y), (x-1,y+1), (x+1,y-1), (x+1,y), (x+1,y+1), \
                       (x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y+1), (x,y+1), (x+1,y+1)]
        if not spots_empty(surrounding):
            for i in range(4):
                direction = surrounding[3*((i+r)%4):3+3*((i+r)%4)]
                if spots_empty(direction):
                    if direction[1] in proposed:
                        proposed[direction[1]].append(elf)
                    else:
                        proposed[direction[1]]=[elf]
                    break
    if len(proposed)==0:
        print(f'The elves stopped moving. This is round {r+1}.')
        answer2 = r+1
        break
    
    for dest in proposed:
        if len(proposed[dest])==1:
            elf = proposed[dest][0]
            elves[elf] = dest
    #field = visualise_field(elves.values())
    if r==9:
        elves10 = elves.copy()

#field = visualise_field(elves.values())

xs = {x for (x,y) in elves10.values()}
xsize = max(xs)+1 -min(xs)
ys = {y for (x,y) in elves10.values()}
ysize = max(ys)+1 -min(ys)

Nelves = len(elves)

answer1 = xsize*ysize-Nelves
print(answer1)

toc = time.perf_counter()
print(f"Finished in {toc - tic:0.2f} seconds")  
