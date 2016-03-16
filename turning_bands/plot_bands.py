__author__ = 'gogo40'

import freulon_algo

#generate the directions
dirs = []
xa = []
ya = []
za = []

n = 1000 #number of bands

for i in xrange(1, n + 1):
    dir = freulon_algo.get_dir(i)
    dirs.append(dir)
    xa.append(dir[0])
    ya.append(dir[1])
    za.append(dir[2])

#Plot the bands

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for dir in dirs:
    ax.plot([0, dir[0]], [0, dir[1]], [0, dir[2]]);

ax.scatter(xa, ya, za, marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
