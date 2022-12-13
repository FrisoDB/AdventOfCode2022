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

elfmax = 0
elfcal = 0
for line in data:
    if line == '\n':
        #witregel dus hierna nieuwe elf
        if elfcal>elfmax:
            elfmax = elfcal
        elfcal = 0
    else:
        elfcal += int(line)

if elfcal>elfmax:
    elfmax = elfcal

print(elfmax)
        
        
    
