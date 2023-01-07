# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:43:42 2023

@author: friso

"""
import numpy as np

def mixing(initial, rounds):
    tracker = list(range(len(initial)))
    work = initial.copy()

    if initial.count(0)>1:
        print("Multiple occurences of zero (0) detected in input data.")
    
    for r in range(rounds):
        for i in range(len(initial)):
            cur_pos = tracker.index(i)
            number = initial[i]
            new_pos = cur_pos + number
            work.pop(cur_pos)
            tracker.pop(cur_pos)
            work.insert(new_pos%len(work), number)
            tracker.insert(new_pos%len(tracker),i)

    loc_zero = work.index(0)
    coordinates = [ work[(loc_zero+1000)%len(work)], work[(loc_zero+2000)%len(work)], \
                   work[(loc_zero+3000)%len(work)] ]
    return coordinates
    

file = open('20numberstest.txt') #[4,-3,2]= 3
file = open('20numbers.txt')
data = file.readlines()

initial = [np.int64(line) for line in data]

coordinates1 = mixing(initial,1)
answer1 = sum(coordinates1)
print(answer1)

key = 811589153
initial2 = [number*key for number in initial]

coordinates2 = mixing(initial2,10)
answer2 = sum(coordinates2)
print(answer2)

