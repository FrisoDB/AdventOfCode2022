# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:41:29 2022

@author: friso
"""

# open the data file
#file = open("01testcal.txt")
file = open("01elfcals.txt")
# read the file as a list and make it a numpy array
data = file.readlines()

elfsums = []
elf = 0
for line in data:
    if line == '\n':
        #witregel dus hierna nieuwe elf
        elfsums.append(elf)
        elf = 0
    else:
        elf += int(line)
elfsums.append(elf)

print(max(elfsums)) #first answer
#print(elfsums)

elfsums.sort(reverse=True) #places highest values first

#print(elfsums[:3])
print(sum(elfsums[:3])) #second answer
