# Created by Medad Rufus Newman on 07/12/2019

import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

num_points = 16
seed = 10
np.random.seed(seed = None)


points_coordinate = np.random.rand(num_points, 2)  # generate coordinate of points
print(points_coordinate)

points_coordinate = np.array([[0.181,14.9],
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
                    [0,0]
                              ])
print(points_coordinate)






distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')


def cal_total_distance(routine):
    '''The objective function. input routine, return total distance.
    cal_total_distance(np.arange(num_points))
    '''
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])


# %% do GA

from sko.GA import GA_TSP

ga_tsp = GA_TSP(func=cal_total_distance, n_dim=num_points, size_pop=300, max_iter=800, prob_mut=0.05)
best_points, best_distance = ga_tsp.run()
print(best_points, best_distance)

# %% plot
fig, ax = plt.subplots(1, 1)
best_points_ = np.concatenate([best_points, [best_points[0]]])
best_points_coordinate = points_coordinate[best_points_, :]
ax.plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1], 'o-r')
plt.show()
