# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:04:21 2023

@author: friso
"""
#import numpy as np
import networkx as nx
import time
tic = time.perf_counter()

def test_deeper(time, pressure, to_open, position):
    #[time_remaining, released pressure, unopened valves, current pos]
    to_open.remove(position)
    
    finalpressure = [pressure]
    for goal in to_open:
        if (time> dist[position][goal]):
            #verplaatsing past nog binnen de tijd
            finalpressure.append(test_deeper(time-dist[position][goal]-1, \
                                             pressure + (time-dist[position][goal]-1)*flow[goal], list(to_open), goal ))
    return max(finalpressure)


file = open('16valvestest.txt')
file = open('16valves.txt')
data0 = file.readlines()
#preprocessing to remove newline \n from datastrings
data = [line.replace('=',' ').replace(',','').replace(';','').split() for line in data0]

valves = [[line[1], int(line[5]), line[10:]] for line in data]
edges = [ (node[0],second)  for node in valves for second in node[-1]]
flow = { valve[0]:valve[1] for valve in valves}

G = nx.Graph()
G.add_edges_from(edges)

dist = dict(nx.all_pairs_shortest_path_length(G))

for node in dist: #verwijdert stappen naar zichzelf, beperkt infinite loop risico
    dist[node].pop(node)

working_valves = [line[0] for line in valves if line[1]!=0]
working_valves.append('AA') #beetje hack om functie te laten werken

answer1 = test_deeper(30, 0, working_valves, "AA")
print(answer1)
toc = time.perf_counter()
print(f"Finished in {toc - tic:0.4f} seconds")