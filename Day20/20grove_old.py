# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:43:42 2023

@author: friso

"""

file = open('20numberstest.txt')
file = open('20numbers.txt')
data0 = file.readlines()
initial = [int(line) for line in data0]

#initial = [1, 2, -3, 3, -2, 0, 4] #testset,[4,-3,2]= 3
work = initial.copy()

doubles = [(value,initial.count(value)) for value in initial if initial.count(value)>1]
if len(doubles)>1:
    print(f"There are {len(doubles)} values which occur multiple times in the input data, so this original setup is going to fail.")

for i in range(len(initial)):
    number = initial[i]
    loc = work.index(number)
    work.pop(loc)
    work.insert((loc+number)%len(work),number)
    
loc_zero = work.index(0)
coordinates = [ work[(loc_zero+1000)%len(work)], work[(loc_zero+2000)%len(work)], \
               work[(loc_zero+3000)%len(work)] ]

print(sum(coordinates))



