# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:22:44 2023

@author: friso
"""

def take_steps(move,x,y):
    for i in range(move):
        #track.append([x,y])
        match facing:
            case 0:
                #moving rightward
                ynew = (y+1)%len(board[x])
                while board[x][ynew]==' ':
                    ynew = (ynew+1)%len(board[x])
                if board[x][ynew]=='.':
                    y = ynew
                    continue
                elif board[x][ynew]=='#':
                    break
            case 2:
                #moving leftward
                ynew = (y-1)%len(board[x])
                while board[x][ynew]==' ':
                    ynew = (ynew-1)%len(board[x])
                if board[x][ynew]=='.':
                    y = ynew
                    continue
                elif board[x][ynew]=='#':
                    break
            case 1:
                #moving downward
                xnew = (x+1)%len(board)
                while board[xnew][y]==' ':
                    xnew = (xnew+1)%len(board)
                if board[xnew][y]=='.':
                    x = xnew
                    continue
                elif board[xnew][y]=='#':
                    break
            case 3:
                #moving upward
                xnew = (x-1)%len(board)
                while board[xnew][y]==' ':
                    xnew = (xnew-1)%len(board)
                if board[xnew][y]=='.':
                    x = xnew
                    continue
                elif board[xnew][y]=='#':
                    break
    return x,y
    

file0 = open('22testboard.txt')
file1 = open('22testmoves.txt')

# file0 = open('22board.txt')
# file1 = open('22moves.txt')

data0 = file0.readlines()
#preprocessing to remove newline \n from datastrings
data0 = [line.replace('\n','') for line in data0]
width_board = max( [len(line) for line in data0] )
board = [line+' '*(width_board-len(line)) for line in data0]

data1 = file1.read()

moves = []
value = ''
for char in data1:
    if char in 'LR':
        moves.append(int(value))
        value = ''
        moves.append(char)
    elif char in '0123456789':
        value += char
moves.append(int(value))

#track = []
x = 0
y = board[0].index('.')
facing = 0

for move in moves:
    if move=='L':
        facing = (facing-1)%4
    elif move=='R':
        facing = (facing+1)%4
    elif type(move)==int:
        #steps are made
        x,y = take_steps(move,x,y)        
            

answer1 = 1000* (x+1) + 4* (y+1) + facing
print(answer1)
