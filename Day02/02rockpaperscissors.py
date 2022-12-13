# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:34:23 2022

@author: friso
"""

# open the data file
#file = open("02rpstest.txt")
file = open("02tentrps.txt")
# read the file as a list and make it a numpy array
data = file.readlines()


scores = []

for line in data:
    score = 0
    
    if line[2] == 'X': #rock A
        score += 1
    elif line[2] == 'Y': #paper B
        score += 2
    elif line[2] == 'Z': #scissors C
        score += 3
        
    if line[:3] in ['A X','B Y','C Z'] : #gelijk/draw
        score += 3
    elif line[:3] in ['A Y','B Z','C X'] : #win
        score += 6
    #skipped +=0 for loss
    
    scores.append(score)
        
print(sum(scores))        
    

