# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:22:44 2023

@author: friso
"""

def take_steps(move,x,y,facing):
    for i in range(move):
        #track.append([x,y])
        xnew,ynew,facingnew = x,y,facing
        match facing:
            case 0:
                #moving rightward
                ynew = (y+1)
                if (ynew==len(board[x])) or (board[x][ynew]==' '):
                    xnew,ynew,facingnew = change_region(x,ynew,facing)
                if board[xnew][ynew]=='.':
                    x,y,facing = xnew,ynew,facingnew
                    continue
                elif board[xnew][ynew]=='#':
                    
                    break
            case 2:
                #moving leftward
                ynew = (y-1)
                if (ynew==-1) or (board[x][ynew]==' '):
                    xnew,ynew,facingnew = change_region(x,ynew,facing)
                if board[xnew][ynew]=='.':
                    x,y,facing = xnew,ynew,facingnew
                    continue
                elif board[xnew][ynew]=='#':
                    
                    break
            case 1:
                #moving downward
                xnew = (x+1)
                if (xnew==len(board)) or (board[xnew][y]==' '):
                    xnew,ynew,facingnew = change_region(xnew,y,facing)
                if board[xnew][ynew]=='.':
                    x,y,facing = xnew,ynew,facingnew
                    continue
                elif board[xnew][ynew]=='#':
                    
                    break
            case 3:
                #moving upward
                xnew = (x-1)
                if (xnew==-1) or (board[xnew][y]==' '):
                    xnew,ynew,facingnew = change_region(xnew,y,facing)
                if board[xnew][ynew]=='.':
                    x,y,facing = xnew,ynew,facingnew
                    continue
                elif board[xnew][ynew]=='#':
                    
                    break
    return x,y,facing

def change_region_test(x,y,facing):
    if (0<=x<4) and (y==12) and (facing==0):
        xnew = 11-x
        ynew = 15
        facingnew = 2    
    elif  (4<=x<8) and (y==12) and (facing==0):
        xnew = 8
        ynew = 19-x #x=4->ynew=15, x=7->ynew=12
        facingnew = 1
    elif (x==7) and (12<=y<16) and (facing==3):
        xnew = 19-y
        ynew = 12
        facingnew = 0
    elif (8<=x<12) and (y==16) and (facing==0):
        xnew = 11-x
        ynew = 12
        facing = 2
    elif (x==12) and (12<=y<16) and (facing==1):
        xnew = 19-y     #y=12 -> xnew=7, y=15->xnew=4
        ynew = 0
        facingnew = 0
    elif (x==12) and (8<=y<12) and (facing==1):
        xnew = 7     
        ynew = 11-y     #8>3, 11>0
        facingnew = 3
    elif (8<=x<12) and (y==7) and (facing==2):
        xnew = 7
        ynew = 15-x  #x=8>y=7, x=11>y=4
        facingnew = 3
    elif (x==8) and (4<=y<8) and (facing==1):
        xnew = 15-x
        ynew = 8
        facing = 0
    elif (x==8) and (0<=y<4) and (facing==1):
        xnew = 11
        ynew = 11-y
        facingnew = 3
    elif (4<=x<8) and (y==-1) and (facing==2):
        xnew = 11
        ynew = 19-x
        facingnew =3
    elif (x==3) and (0<=y<4) and (facing==3):
        xnew = 0
        ynew = 11-y
        facingnew = 1
    elif (x==3) and (4<=y<8) and (facing==3):
        xnew = y-4
        ynew = 8
        facingnew = 0
    elif (0<=x<4) and (y==7) and (facing==2):
        xnew = 4
        ynew = x+4
        facingnew = 1
    elif (x==-1) and (8<=y<12) and (facing==3):
        xnew = 4
        ynew = 11-y
        facingnew = 1
    return xnew, ynew, facingnew

def change_region(x,y,facing):
    if Test:
        return change_region_test(x, y, facing)
    
    if (x==-1) and (50<=y<100) and (facing==3):
        xnew = 100+y
        ynew = 0
        facingnew = 0
    elif (x==-1) and (100<=y<150) and (facing==3):
        xnew = 199
        ynew = y-100
        facingnew = 3
    elif (0<=x<50) and (y==150) and (facing==0):
        xnew = 149-x
        ynew = 99
        facingnew = 2
    elif (x==50) and (100<=y<150) and (facing==1):
        xnew = y-50    #y=100>x=50
        ynew = 99
        facingnew = 2
    elif (50<=x<100) and (y==100) and (facing==0):
        xnew = 49
        ynew = x+50
        facingnew = 3
    elif (100<=x<150) and (y==100) and (facing==0):
        xnew = 149-x
        ynew = 149
        facingnew = 2
    elif (x==150) and (50<=y<100) and (facing==1):
        xnew = y+100
        ynew = 49
        facingnew = 2
    elif (150<=x<200) and (y==50) and (facing==0):
        xnew = 149
        ynew = x-100
        facingnew = 3
    elif (x==200) and (0<=y<50) and (facing==1):
        xnew = 0
        ynew = y+100
        facingnew = 1
    elif (150<=x<200) and (y==-1) and (facing==2):
        xnew = 0
        ynew = x-100
        facingnew = 1
    elif (100<=x<150) and (y==-1) and (facing==2):
        xnew = 149-x  #100>49, 149>0
        ynew = 50
        facingnew = 0
    elif (x==99) and (0<=y<50) and (facing==3):
        xnew = y+50
        ynew = 50
        facingnew = 0
    elif (50<=x<100) and (y==49) and (facing==2):
        xnew = 100
        ynew = x-50
        facingnew = 1
    elif (0<=x<50) and (y==49) and (facing==2):
        xnew = 149-x
        ynew = 0
        facingnew = 0
    return xnew, ynew, facingnew


Test = False

file0 = open('22board.txt')
file1 = open('22moves.txt')
if Test:
    file0 = open('22testboard.txt')
    file1 = open('22testmoves.txt')

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
        x,y,facing = take_steps(move,x,y,facing)        
            

answer2 = 1000* (x+1) + 4* (y+1) + facing
print(answer2)
