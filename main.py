# ------------------------
# Tanzila Islam
# Created Date: 15.01.2020
#-------------------------

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
from numpy import sin, cos

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")
ax.set_autoscale_on(True)


# cube
# r = [-10, 10]
# for s, e in combinations(np.array(list(product(r, r, r))), 2):
#     if np.sum(np.abs(s-e)) == r[1]-r[0]:
#         ax.plot3D(*zip(s, e), color="b")


# cube
d = [-2, 2]
# for s, e in combinations(np.array(list(product(d, d, d))), 2):
#     if np.sum(np.abs(s-e)) == d[1]-d[0]:
#         ax.plot3D(*zip(s, e), color="g")

theta = np.radians(45)
for s, e in combinations(np.array(list(product(d, d, d))), 2):
    if np.sum(np.abs(s-e)) == d[1]-d[0]:
        s_rotated = [s[0] * cos(theta) - s[1] * sin(theta),
                     s[0] * sin(theta) + s[1] * cos(theta),
                     s[2]]
        e_rotated = [e[0] * cos(theta) - e[1] * sin(theta),
                     e[0] * sin(theta) + e[1] * cos(theta),
                     e[2]]
        ax.plot3D(*zip(s_rotated, e_rotated), color="g")

plt.show()


