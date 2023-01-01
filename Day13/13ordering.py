# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:17:40 2022

@author: friso
"""

def Compare_lists(first,second):
    ordered = None
    
    for i in range( min(len(first),len(second)) ):
        left = first[i]
        right = second[i]
        if type(left)==list and type(right)==list:
            #Compare two list recursive
            ordered = Compare_lists(left, right)
        elif type(left)==list and type(right)==int:
            ordered = Compare_lists(left, [right])
        elif type(left)==int and type(right)==list:
            ordered = Compare_lists([left], right)
        #two ints from hereon
        elif left<right:
            ordered = True
        elif left>right:
            ordered = False
        #else: #left==right   continue
    
        if type(ordered)==bool:
            return ordered
        
    if len(first)<len(second):
        ordered = True
    elif len(first)> len(second):
        ordered = False
        
    return ordered


#file = open('13decodetest.txt')
file = open('13decode.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [eval(line) for line in data0 if line !='\n']

ordered = []
for i in range(len(data)//2):
    first = data[i*2]
    second = data[1+i*2]
    if Compare_lists(first, second):
        ordered.append(i+1)

#answer1
print(sum(ordered))

toevoeging =[ [[2]], [[6]] ]
data.extend(  toevoeging  )

unordered = True
Npackets = len(data)

while unordered:
    unordered = False
    for i in range(Npackets-1):
        first = data[i]
        second = data[1+i]
        if not Compare_lists(first, second):
            data[i], data[1+i] = data[1+i], data[i]
            unordered = True

key = [data.index(i)+1 for i in toevoeging]

#answer2
print(key[0]*key[1])



