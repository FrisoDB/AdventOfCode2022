# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:09:43 2023

@author: friso
"""

import numpy as np


def snafu_to_decimal(snafu):
    snafu_digits = []
    for digit in reversed(snafu):
        if digit in '012':
            snafu_digits.append(int(digit))
        elif digit=='-':
            snafu_digits.append(-1)
        elif digit=='=':
            snafu_digits.append(-2)
    n = np.arange(len(snafu), dtype=np.int64)
    powers_of_5 = 5**n
    return np.dot(snafu_digits, powers_of_5)
        
def decimal_to_snafu(decimal):
    #only works for positive integers (decimal>0)
    digits = []
    reduced = decimal+2
    while reduced >2:
        digits.append(reduced%5)
        reduced = reduced//5 +2
    
    digits.reverse()
    snafu_digits_numeric = np.array(digits) -2
    snafu_digits = []
    for digit in snafu_digits_numeric:
        if digit in [0,1,2]:
            snafu_digits.append(str(digit))
        elif digit==-1:
            snafu_digits.append('-')
        elif digit==-2:
            snafu_digits.append('=')
    return ''.join(snafu_digits)


file = open('25snafutest.txt')
file = open('25snafu.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
snafus = [line.replace('\n','') for line in data0]

decimals = []
for snafu in snafus:
    decimals.append(snafu_to_decimal(snafu))
    
decimal_sum2 = np.sum(decimals)

# dump = []
# for i in range(1,10):  #0 is not wellbehaved (yet)
#     dump.append(decimal_to_snafu(i))
# dump.append(decimal_to_snafu(314159265))

answer1 = decimal_to_snafu(decimal_sum2)
print(answer1)


