_author__ = 'Plinio H. Vargas, Medad Newman'
__date__ = "10/12/19"

import sys
import copy
import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt




points_coordinate = [[0.181,14.9],
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




matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')



n = len(matrix)
all_sets = []
g = {}
p = []
solution_indexes = [1]

def main():
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]

    print("minimum",get_minimum(1, range(2,n+1)))

    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    solution_indexes.append(solution[1][0])

    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                solution_indexes.append(solution[1][0])
                break
    print('1}')

    print(solution_indexes)


    return


def get_minimum(k, a):
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)

    # get minimum value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


def plot_graphs():
    # %% plot
    fig, ax = plt.subplots(1, 1)
    sorted_coords = sorted(points_coordinate,key = solution_indexes)

    ax.plot(sorted_coords[0,:], 'o-r')
    plt.show()



if __name__ == '__main__':
    main()
    sys.exit(0)
