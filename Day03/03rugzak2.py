# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:43:17 2022

@author: friso
"""

# open the data file
#file = open("03rugzaktest.txt")
file = open("03rugzak.txt")
# read the file as a list and make it a numpy array
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line[:-1] if line[-1:]=='\n' else line for line in data0]

common = []
for i in range(len(data)//3):
    first = set(data[3*i])
    second = set(data[3*i+1])
    third = set(data[3*i+2])
    common.append(first & second & third)

#print(common)

priority = []
for line in common:
    count = 0
    for i in line:
        if ord(i)>95:
            #lowercase
            count += ord(i)-ord('a')+1
        else:
            #Uppercase
            count += ord(i)-ord('A')+27
    priority.append(count)
    
print(sum(priority))



