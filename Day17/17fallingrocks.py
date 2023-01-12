# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:09:41 2023

@author: friso
"""

from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def new_rock(i,y):
    if i==0:
        new_rock = [(2,y),(3,y),(4,y),(5,y)] #bar
    elif i==1:
        new_rock = [(2,y+1),(3,y),(3,y+1),(3,y+2),(4,y+1)] #cross
    elif i==2:
        new_rock = [(2,y),(3,y),(4,y),(4,y+1),(4,y+2)] # hook
    elif i==3:
        new_rock = [(2,y),(2,y+1),(2,y+2),(2,y+3)] # pole
    elif i==4:
        new_rock = [(2,y),(2,y+1),(3,y),(3,y+1)] # block
    return new_rock

def visualise_field(field_dict, ymax):
    field = np.zeros((ymax+1, 7))
    for (x,y),value in field_dict.items():
        if value:
            field[y,x] = value
    plt.imshow(field, origin='lower', cmap='binary')
    plt.axis('off')
    return field

def falling_rocks(jets, Nrocks=2022, repetitions=0):
    states = defaultdict(list)
    field = defaultdict(int)
    for x in range(7):
        field[(x,0)] = 6
    
    ymax = 0
    jet_count = 0
    
    for rock_count in range(Nrocks):
        # get new rock
        rock = new_rock(rock_count%5, ymax+4)
        jet0 = jet_count
        # move rock multiple times, until stopped
        while True:
            # jet pushes rock, if no collision with wall or objects
            jet = jets[jet_count%len(jets)]
            jet_count += 1
            rock_pushed = [ (x+1,y) if jet==">" else (x-1,y) for x,y in rock ]
            collision = False
            
            if (rock_pushed[0][0] < 0) or (rock_pushed[-1][0] > 6):
                collision = True
            else:
                for point in rock_pushed:
                    if field[point]:
                        collision = True
                        break
                
            if collision:
                rock_pushed = rock
            
            # rock falls, or gets stopped and added to field
            rock_falling = [ (x,y-1) for x,y in rock_pushed ]
            collision = False
            
            for point in rock_falling:
                if field[point]:
                    collision = True
                    break
            
            if collision:
                # cannot fall, so add rock_pushed to field
                for point in rock_pushed:
                    field[point] = rock_count%5 +1 
                
                ymax_rock = max(y for x,y in rock_pushed)
                
                dy_fallen = ymax + 4 - rock_pushed[0][1] #how much the rock has fallen
                x_landing = rock_pushed[0][0] #landing should be the same each cycle
                state = f'{rock_count%5}_{jet0%len(jets)}_{dy_fallen}_{x_landing}'
                states[state].append(rock_count)
                
                if repetitions and (len(states[state]) >= repetitions):
                    return states[state], state, ymax
                
                if ymax_rock > ymax:
                    ymax = ymax_rock
                break
            
            else:
                rock = rock_falling

    return ymax

file = open('17rockmovestest.txt')
file = open('17rockmoves.txt')
jets = file.read()

ymax1 = falling_rocks(jets, 2022, 0)
answer1 = ymax1
print(answer1)

# 1000000000000 = 10**12, so searching for repetitions
Nrocks_big = 10**12

# choose Nrocks big enough to contain the repetitions + some offset
# more repetitions is stronger
find_repetition = falling_rocks(jets,10**4,6)

# in number of rocks
periods = np.diff(find_repetition[0])
period = periods[-1]
offset = find_repetition[0][2]

# in height
h_offset = falling_rocks(jets,offset,0)
h_offset_period = falling_rocks(jets,offset+period,0)
h_period = h_offset_period - h_offset

N_periods = (Nrocks_big-offset)//period
tail = (Nrocks_big-offset)%period

h_offset_tail = falling_rocks(jets,offset+tail,0)
h_total = h_offset_tail + N_periods*h_period

answer2  = h_total
print(f'10^(12) rocks have a total height of: {h_total}.')
print(f'This unbuildable tower has at least {N_periods} repeating part of {period} rocks, each period having a height of {h_period}.')



