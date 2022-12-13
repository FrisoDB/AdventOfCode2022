# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:00:43 2022

@author: friso
"""

import numpy as np

# open the data file
#file = open("04dubbelwerktest.txt")
file = open("04dubbelwerk.txt")
# read the file as a list and make it a numpy array
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.strip() for line in data0]
#[line[:-1] if line[-1:]=='\n' else line for line in data0] #oud

a = [line.replace('-',',').split(',') for line in data]
assignments = np.array(a, dtype='int')

#is de tweede ingesloten in de eerste range of vice versa?
infirst = (assignments[:,0]<=assignments[:,2]) &  (assignments[:,1]>=assignments[:,3])
insecond = (assignments[:,0]>=assignments[:,2]) &  (assignments[:,1]<=assignments[:,3])

enclosed = infirst | insecond
print(sum( enclosed ))

#raakt eerste de tweede aan onderkant/bovenkant range?
lowtouch = (assignments[:,0]<=assignments[:,2]) &  (assignments[:,1]>=assignments[:,2])
hightouch = (assignments[:,0]<=assignments[:,3]) &  (assignments[:,1]>=assignments[:,3])

overlap = lowtouch | hightouch

print(sum( overlap|enclosed ))


