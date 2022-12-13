# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:16:22 2022

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
    
    if line[2] == 'Y': #draw
        score += 3
    elif line[2] == 'Z': #win
        score += 6
    #skipped +=0 for loss
        
    if line[:3] in ['A Y','B X','C Z'] : #rock R
        score += 1
    elif line[:3] in ['A Z','B Y','C X'] : #paper P
        score += 2
    elif line[:3] in ['A X','B Z','C Y'] : #scissors S
        score += 3
    
    scores.append(score)
        
print(sum(scores))        

#rockA paperB scissorsC