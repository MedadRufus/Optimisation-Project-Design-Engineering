# Created by Medad Rufus Newman on 12/12/2019

import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
import sys

#file_name = sys.argv[1] if len(sys.argv) > 1 else 'data/nctu.csv'
#points_coordinate = np.loadtxt(file_name, delimiter=',')
num_points = 16


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

distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
distance_matrix = distance_matrix  # 1 degree of lat/lon ~ = 111000m


def cal_total_distance(routine):
    '''The objective function. input routine, return total distance.
    cal_total_distance(np.arange(num_points))
    '''
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])


# %%
from sko.SA import SA_TSP

sa_tsp = SA_TSP(func=cal_total_distance, x0=range(num_points), T_max=100, T_min=1, L=1000 * num_points)

best_points, best_distance = sa_tsp.run()
print(best_points, best_distance, cal_total_distance(best_points))
# %% Plot the best routine
from matplotlib.ticker import FormatStrFormatter

fig, ax = plt.subplots(1, 2)
fig.suptitle("Plots showing the results of using Simulated Annealing to optimise the path")

best_points_ = np.concatenate([best_points, [best_points[0]]])
best_points_coordinate = points_coordinate[best_points_, :]
ax[0].plot(sa_tsp.best_y_history)
ax[0].set_ylabel("Distance")
ax[0].set_xlabel("Iteration")
ax[0].set_title('Distance improvements over each iteration')

ax[1].plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1],
           marker='o', markerfacecolor='b', color='c', linestyle='-')
ax[1].xaxis.set_major_formatter(FormatStrFormatter('%.3f'))
ax[1].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
ax[1].set_title('Final minimum travelled path: minimum distance = {0:.2f}km '.format(best_distance))
ax[1].set_xlabel("Longitude")
ax[1].set_ylabel("Latitude")
plt.show()

# %% Now Plot the animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

best_x_history = sa_tsp.best_x_history

fig2, ax2 = plt.subplots(1, 1)
ax2.set_title('title', loc='center')
line = ax2.plot(points_coordinate[:, 0], points_coordinate[:, 1],
                marker='o', markerfacecolor='b', color='c', linestyle='-')
ax2.xaxis.set_major_formatter(FormatStrFormatter('%.3f'))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
ax2.set_xlabel("Longitude")
ax2.set_ylabel("Latitude")
plt.ion()
p = plt.show()


def update_scatter(frame):
    ax2.set_title('iter = ' + str(frame))
    points = best_x_history[frame]
    points = np.concatenate([points, [points[0]]])
    point_coordinate = points_coordinate[points, :]
    plt.setp(line, 'xdata', point_coordinate[:, 0], 'ydata', point_coordinate[:, 1])
    return line


ani = FuncAnimation(fig2, update_scatter, blit=True, interval=25, frames=len(best_x_history))
plt.show()

#ani.save('sa_tsp.gif', writer='pillow')


