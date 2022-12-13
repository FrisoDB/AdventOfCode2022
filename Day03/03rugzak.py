# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:04:10 2022

@author: friso
"""

# open the data file
#file = open("03rugzaktest.txt")
file = open("03rugzak.txt")
# read the file as a list and make it a numpy array
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line[:-1] if line[-1:]=='\n' else line for line in data0]

both = []
for line in data:
    compart1 = set(line[:len(line)//2])
    compart2 = set(line[len(line)//2:])
    both.append(compart1 & compart2)

priority = []
for line in both:
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
        
    
    
    


