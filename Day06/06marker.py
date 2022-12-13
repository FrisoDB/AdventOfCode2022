# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:40:47 2022

@author: friso
"""

# open the data file
#file = open("05stacktest.txt")
file = open("06tuning.txt")
# read the file as a list and make it a numpy array
data = file.readlines()

text = data[0]
# two test texts below
#text = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' #7/19
#text = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' #10/29

# choose 4 for 1st part, 14 for 2nd part
N = 14

for i in range(N,len(text)+1):
    marker = text[i-N:i]
    if len(set(marker)) == len(marker):
        break

print(i, marker)



