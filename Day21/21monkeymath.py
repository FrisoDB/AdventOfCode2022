# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 00:57:02 2023

@author: friso
"""

file = open('21monkeymathtest.txt')
file = open('21monkeymath.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.split(":") for line in data0]


monkeys = dict()
unknown = dict()
for monkey in data:
    try:
        value = int(monkey[1])
        monkeys[monkey[0]] = value
        
    except:
        value = monkey[1]
        unknown[monkey[0]] = monkey[1]

  
while len(unknown)>0:
    for monkey in unknown.copy():
        array = unknown[monkey].split()
        first = array[0]
        last = array[2]
        try:
            value = eval(f"{monkeys[first]}" +array[1]+ f"{monkeys[last]}")
            monkeys[monkey] = value
            unknown.pop(monkey)
        except:
            continue
                
#answer1       
print(monkeys["root"])           
        
    
    
    
    


