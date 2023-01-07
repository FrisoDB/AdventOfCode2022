# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:07:01 2022

@author: friso
"""
#from copy import deepcopy
import numpy as np

file = open("07filesystemtest.txt")
file = open("07filesystem.txt")
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('\n','').split() for line in data0]

system = {}
location = ('/',)

# build system
for line in data:
    if line[0]=='$' and line[1]=='cd':
        if line[2]=='..':
            location = location[:-1]
        elif line[2]=='/':
            location = ('/',)
        else:
            location += (line[2],)
    elif line[0]=='$' and line[1]=='ls':
        system[location] = []
    elif line[0][0] in '0123456789':
        system[location].append(np.int64(line[0]))  
    elif line[0]=='dir':
        system[location].append((line[1],))

#system_copy = deepcopy(system)
dirSizes = {}
# determine directory sizes
for r in range(10):      
    for folder in system.copy():
        folder_complete = True
        for i in range(len(system[folder])):
            if type(system[folder][i])==tuple:
                subfolder = system[folder][i]
                if (folder+subfolder) in dirSizes:
                    system[folder][i] = dirSizes[(folder+subfolder)]
                else:
                    folder_complete = False
        if folder_complete:
            dirSizes[folder] = sum(system.pop(folder))

answer1 = [size for size in dirSizes.values() if size<=1e5] 
print(sum( answer1 ))

used = dirSizes[('/',)]
total = 7e7
available = total-used
update_size = 3e7
still_needed = update_size - available


answer2 = [size for size in dirSizes.values() if size>=still_needed] 
print(min( answer2 ))


