# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:14:25 2022

@author: friso
Geïnspireerd door Jelle, tnx
"""

import networkx as nx

def Get_height(char):
    if char=='S':
        return ord('a')
    elif char=='E':
        return ord('z')
    else:
        return ord(char)
    
def Get_connections(heights, x,y):
    connections = []
    limit = heights[x][y]+1
    current = f"{x}-{y}"
    if (x>0) and (heights[x-1][y]<=limit):
        connections.append((current, f"{x-1}-{y}"))
    if (x+1<len(heights)) and (heights[x+1][y]<=limit):
        connections.append((current, f"{x+1}-{y}"))
    if (y>0) and (heights[x][y-1]<=limit):
        connections.append((current, f"{x}-{y-1}"))
    if (y+1<len(heights[x])) and (heights[x][y+1]<=limit):
        connections.append((current, f"{x}-{y+1}"))
    return connections

def Shortest_path(graph,start,end):
    try:
        return len(nx.dijkstra_path(graph,start,end))-1
    except:
        return 66666
    
file = open('12doolhoftest.txt')
file = open('12doolhof.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
kaart = [list(line.replace('\n','')) for line in data0]

heights = [ [Get_height(char) for char in line] for line in kaart]

edges = []
startingSquares = []
for i in range(len(heights)):
    for j in range(len(heights[i])):
        edges.extend( Get_connections(heights, i, j) )
        
        if kaart[i][j]=='a':
            startingSquares.append(f"{i}-{j}")
        elif kaart[i][j]=='S':
            startingSquares.append(f"{i}-{j}")
            S = f"{i}-{j}"
        elif kaart[i][j]=='E':
            E = f"{i}-{j}"

graph =  nx.DiGraph()
graph.add_edges_from(edges)

answer1 = Shortest_path(graph, S, E)
print(answer1)

answer2 =  [ Shortest_path(graph,start,E) for start in startingSquares]
print(min(answer2))

