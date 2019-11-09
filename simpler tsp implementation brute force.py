# Created by Medad Rufus Newman on 09/11/2019


# Python3 program to implement traveling salesman
# problem using BRUTE FORCE naive approach.
from sys import maxsize
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

        # store minimum weight Hamiltonian Cycle
    min_path = maxsize

    while True:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

        if not next_permutation(vertex):
            break

    return min_path

# next_permutation implementation
def next_permutation(L):

    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True

# Driver Code
if __name__ == "__main__":

    # matrix representation of graph
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    graph = [
        [0, 0.268188, 1.0861600, 0.284266, 2.1870300, 2.90507, 1.06443, 0.641625, 0.191624, 3.44142],
        [0.1609330, 0, 0.6911510, 0.464564, 1.4049800, 1.96431, 0.168696, 0.654258, 1.41509, 2.98196],
        [0.3580770, 0.379707, 0, 1.249930, 0.0821726, 0.408356, 1.74232, 2.37079, 2.95341, 3.90037],
        [0.0818823, 0.223001, 1.0921200, 0, 2.1872100, 2.89526, 0.942284, 0.56915, 0.872503, 2.75427],
        [0.3714430, 0.397651, 0.0423335, 1.289620, 0, 0.315516, 1.82914, 2.46966, 3.06793, 3.87276],
        [0.4166200, 0.46945, 0.1776410, 1.441470, 0.2664210, 0, 2.15881, 2.82956, 3.44337, 3.90929],
        [0.1427810, 0.0377101, 0.7089300, 0.438806, 1.4446600, 2.01924, 0, 0.526249, 1.24782, 3.13342],
        [0.0799607, 0.135875, 0.8962080, 0.246239, 1.8121500, 2.45884, 0.488912, 0, 0.76215, 3.14592],
        [0.0228630, 0.281361, 1.0688800, 0.361399, 2.1552200, 2.86474, 1.10989, 0.729676, 0, 3.6366],
        [0.4020280, 0.580519, 1.3821200, 1.117020, 2.6638000, 3.18444, 2.72886, 2.94897, 3.56066, 0],
    ]

    s = 0
    print(travellingSalesmanProblem(graph, s))

# This code is contributed by
# sanjeev2552
