# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:07:01 2022

@author: friso
"""
from copy import deepcopy


# open the data file
file = open("07filesystemtest.txt")
file = open("07filesystem.txt")
# read the file as a list and make it a numpy array
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.split() for line in data0]


filesys = {}
location = ['/']
gather_directory = [0]

for line in data:
    
    if line[0]=='$':
        #commands
        
        if gather_directory != [0]:
            #saves gathered list of contest after $ls command
            filesys[location[-1]]=gather_directory
            gather_directory = [0]
            
        if line[1]=='ls':
            #gather_directory = [0] #not necessary
            continue

        #change location/directory
        elif (line[1]=='cd' and line[2]=='/'):
            #return to main directory
            location = ['/']
        elif (line[1]=='cd' and line[2]=='..'):
            #move OUT one level
            location.pop()
        elif line[1]=='cd':
            #choose directory, move level IN
            location.append(line[2])
        
    
    elif line[0]== 'dir':
        #directory
        gather_directory.append(line[1])
    
    elif line[0][0] in '0123456789':
        #filesize+file
        gather_directory[0] += int(line[0])

        
#check whether last directory is properly added to filesystem
if gather_directory != [0]:
    #saves gathered list of contest after $ls command
    filesys[location[-1]]=gather_directory
    gather_directory = [0] 
    
filesys_copy = deepcopy(filesys)
directorysizes = {}

# iterating over filesys to get sizes of all directory including their subdirectories
while len(filesys)>0:
    removepile = []
    
    for directory in filesys:
        #a = filesys[directory]
        if type( filesys[directory][-1]) is int:
            # directory size is known :)
            size = filesys[directory][-1]
            directorysizes[directory] = size
            removepile.append(directory)
            
            for directory2 in filesys:
                #check whether directory in other directories
                #c = filesys[directory2]
                if directory in filesys[directory2]:
                    #add this (sub)directorie size to those directories
                    filesys[directory2][0] += size
                    filesys[directory2].remove(directory)
    
    for i in removepile:
        filesys.pop(i)

answer = [size for size in directorysizes.values() if size<=1e5] 
print(sum( answer ))
    




