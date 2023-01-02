# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:04:21 2023

@author: friso
#deel 2 duurt vijf minuten
"""
#import numpy as np
import networkx as nx
import time
tic = time.perf_counter()

def test_deeper(time, pressure, to_open, position, wait, olifant, oliwait):
    #[time_remaining, released pressure, unopened valves, current pos,
    #    time till next move, elephant position, time till next olimove]

    if wait>oliwait: #so wait<=oliwait
        position, wait, olifant, oliwait =  olifant, oliwait, position, wait
    if wait > 0:
        return test_deeper(time-wait, pressure, to_open, position, 0, olifant, oliwait-wait)
    #vanaf hier wait=0
  
    finalpressure = [pressure]
    
    for goal in to_open:
        if oliwait==0: #beiden gaan stap doen
            for oligoal in to_open:
                if (oligoal!= goal) and (time> dist[position][goal]) and (time> dist[olifant][oligoal]):
                    
                    newpressure = pressure + (time-dist[position][goal]-1)*flow[goal] + (time-dist[olifant][oligoal]-1)*flow[oligoal]
                    new_to_open = list(to_open)
                    new_to_open.remove(goal)
                    new_to_open.remove(oligoal)
                    finalpressure.append(test_deeper(time-1, newpressure, new_to_open, goal, dist[position][goal], oligoal, dist[olifant][oligoal]))   
        else: #slechts één gaat nieuwe stap doen, olifant is onderweg
            if (time> dist[position][goal]):
                
                newpressure = pressure + (time-dist[position][goal]-1)*flow[goal]
                new_to_open = list(to_open)
                new_to_open.remove(goal)
                finalpressure.append(test_deeper(time-1, newpressure, new_to_open, goal, dist[position][goal], olifant, oliwait-1))  
                    
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
starttijd = 30

#10000 dient om olifant stil te zetten
answer1 = test_deeper(starttijd, 0, working_valves, "AA", 0, "AA", 10000)   
print(f"Part 1 has the solution: {answer1}")

toc = time.perf_counter()
print(f"Finished part1 in {toc - tic:0.4f} seconds")

answer2 = test_deeper(starttijd-4, 0, working_valves, "AA", 0, "AA", 0)
print(f"Part 2 has the solution: {answer2}")
toc = time.perf_counter()
print(f"Finished in {toc - tic:0.4f} seconds")