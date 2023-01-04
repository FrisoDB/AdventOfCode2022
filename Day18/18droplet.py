# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 05:11:47 2023

@author: friso
"""

import numpy as np
import networkx as nx

def Get_connections(droplet, shape, x,y,z):
    connections = []
    current = f"{x},{y},{z}"
    #find all surrounding part that are not droplet
    if (x>0) and (not droplet[x-1,y,z]):
        connections.append((current, f"{x-1},{y},{z}"))
    if (x+1<shape[0]) and (not droplet[x+1,y,z]):
        connections.append((current, f"{x+1},{y},{z}"))
    if (y>0) and (not droplet[x,y-1,z]):
        connections.append((current, f"{x},{y-1},{z}"))
    if (y+1<shape[1]) and (not droplet[x,y+1,z]):
        connections.append((current, f"{x},{y+1},{z}"))
    if (z>0) and (not droplet[x,y,z-1]):
        connections.append((current, f"{x},{y},{z-1}"))
    if (z+1<shape[2]) and (not droplet[x,y,z+1]):
        connections.append((current, f"{x},{y},{z+1}"))
    return connections

file = '18cubetest.txt'
file = '18cube.txt'
cubes = np.loadtxt(file, delimiter=',', dtype=int)

exposed = 0
for cube in cubes:
    touching = (np.sum(np.abs(cubes - cube),axis=1)==1)
    exposed += 6 - np.sum(touching)

#part1
print(exposed)

shape = tuple(np.max(cubes, axis=0)+2)
droplet = np.zeros(shape, dtype=bool)
for cube in cubes:
    droplet[cube[0],cube[1],cube[2]] = True

edges = []
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            
            if not droplet[i,j,k]:
                #point is not part op droplet
                edges.extend( Get_connections(droplet, shape, i, j, k) )

G = nx.Graph()
G.add_edges_from(edges)

#compartments = sorted(nx.connected_components(G), key=len, reverse=True)
compartments = list(nx.node_connected_component(G, "0,0,0"))

outside = np.zeros_like(droplet)
for point in compartments: #[0]:
    pos = eval(point)
    outside[pos[0],pos[1],pos[2]] = True

inside = ~outside #contains both airpockets and dropletcubes

exposed2 = 0
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            if inside[i,j,k]:
                exposed2 += sum([outside[i+1,j,k], outside[i-1,j,k], outside[i,j+1,k], \
                                 outside[i,j-1,k], outside[i,j,k+1], outside[i,j,k-1]])
#part2
print(exposed2)                    
                    


