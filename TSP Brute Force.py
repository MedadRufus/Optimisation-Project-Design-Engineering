#!/usr/bin/env python3
"""Run and time an optimal TSP solution."""

import sys
import timeit
import itertools


RUNS = 1

pmin = 1000000

data =  [[0.181,14.9],
         [9.06,9.40],
         [9.38,29.6],
         [10.0,9.77],
         [14.0,0.915],
         [14.5,10.1],
         [14.9,11.8],
         [16.5,10.9],
         [19.0,22.4],
         [19.1,15.6],
         [20.0,6.26],
         [21.6,10.8],
         [24.1,17.3],
         [24.5,18.1],
         [26.3,9.85],
         [0,0]]




import math

def cost(route):
    sum = 0
    # Go back to the start when done.
    route.append(route[0])
    while len(route) > 1:
        p0, *route = route
        sum += math.sqrt((p0[0] - route[0][0])**2 + (p0[1] - route[0][1])**2)
    return sum



d = float("inf")
for p in itertools.permutations(data):
    c = cost(list(p))
    if c <= d:
        d = c
        pmin = p
print("Optimal route:", pmin)
print("Length:", d)

#print("Time (seconds, avg of {runs}):".format(runs=RUNS), timeit.timeit(code, setup, number=RUNS)/RUNS)
