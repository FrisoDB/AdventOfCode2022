# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 00:57:02 2023

@author: friso
"""

import numpy as np

def solve_reversed(key, array):
    if array[0] in monkeys:
        match array[1]:
            case '+': #key = 0+x -> x = key-0
                monkeys[array[2]] = np.int64( monkeys[key] - monkeys[array[0]] )
            case '-': #key = 0-x -> x = 0-key
                monkeys[array[2]] = np.int64( monkeys[array[0]] - monkeys[key] )
            case '*': #key = 0*x -> x = key/0
                monkeys[array[2]] = np.int64( monkeys[key] / monkeys[array[0]] )
            case '/': #key = 0/x -> x = 0/key
                monkeys[array[2]] = np.int64( monkeys[array[0]] / monkeys[key] )
        unknown.pop(key)
    elif array[2] in monkeys:
        match array[1]:
            case '+': #key = x+2 -> x = key-2
                monkeys[array[0]] = np.int64( monkeys[key] - monkeys[array[2]] )
            case '-': #key = x-2 -> x = 2+key
                monkeys[array[0]] = np.int64( monkeys[array[2]] + monkeys[key] )
            case '*': #key = x*2 -> x = key/2
                monkeys[array[0]] = np.int64( monkeys[key] / monkeys[array[2]] )
            case '/': #key = x/2 -> x = 2*key
                monkeys[array[0]] = np.int64( monkeys[array[2]] * monkeys[key] )
        unknown.pop(key)
    return None



file = open('21monkeymathtest.txt')
file = open('21monkeymath.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('\n','').split(":") for line in data0]

monkeys = dict()
unknown = dict()
for monkey in data:
    try:
        value = np.int64(monkey[1])
        monkeys[monkey[0]] = value
    except:
        value = monkey[1]
        unknown[monkey[0]] = monkey[1]

root = unknown.pop('root').split()
monkeys.pop('humn')

# in 11a15 rondes wordt het systeem versimpelt tot 72 onbekenden
for i in range(15): 
    for monkey in unknown.copy():
        array = unknown[monkey].split()
        first = array[0]
        last = array[2]
        try:
            value = np.int64(eval(f"{monkeys[first]}" +array[1]+ f"{monkeys[last]}"))
            monkeys[monkey] = value
            unknown.pop(monkey)
        except:
            pass
 
# using root = (a==b)  ; ['jwcq', '+', 'swbn']          
if (root[0] in monkeys) and not(root[2] in monkeys):
    monkeys[root[2]] = monkeys[root[0]]
elif (root[2] in monkeys) and not(root[0] in monkeys):
    monkeys[root[0]] = monkeys[root[2]]

unsolved_before = 10**10 #choose big

# reverse solve is added
while unsolved_before > len(unknown):
    unsolved_before = len(unknown)
    for monkey in unknown.copy():
        array = unknown[monkey].split()
        first = array[0]
        last = array[2]
        try:
            value = np.int64(eval(f"{monkeys[first]}" +array[1]+ f"{monkeys[last]}"))
            monkeys[monkey] = value
            unknown.pop(monkey)
        except:
            if monkey in monkeys:
                solve_reversed(monkey, array)

#answer2
print(monkeys['humn'])


  
    


