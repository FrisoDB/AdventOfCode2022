# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 00:57:02 2023

@author: friso
#sympy kan niet zoveel vergelijkingen aan, werkt alleen voor testset
"""
from sympy import solve, Eq, S, symbols

file = open('21monkeymathtest.txt')
file = open('21monkeymath.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('cbrt','cibrti').replace('\n','').split(":") for line in data0]
# cbrt blijkt een (numpy)functie


equations = []
for monkey in data:
    if monkey[0]=='root':
        array = monkey[1].split()
        root = symbols(array[0])
        equations.append( Eq(S(array[0]), S(array[-1])) )
    elif monkey[0]=='humn':
        humn = symbols('humn')
    else:
        equations.append( Eq(S(monkey[0]), S(monkey[1])) )
    
answer2 = solve(equations)
print(answer2[0][humn], answer2[0][root])
    
        
   
    

  
    


