__author__ = 'gogo40'

import freulon_algo as fa
import random
from math import *
import matplotlib.pyplot as plt

def generate_spherical_covariance(a, C, L, n_lines):
    f = 2 * sqrt(C * 3.0 / n_lines)
    offset = random.uniform(0, a)
    n_intervals = int(L/a)
    s = []
    x = []
    for i in xrange(0, n_intervals):
        v = random.uniform(0, 1)
        x.append(i * a)
        if v < 0.5:
            s.append(-f)
        else:
            s.append(f)

    return (offset, s, x)

def generate_gaussian_covariance(a, C, L, n_lines):
    f = 2 * sqrt(C * 3.0 / n_lines)
    n_intervals = int(L/a)
    phase = random.uniform(0, 2 * pi)
    (t1, t2, t3) = (random.gauss(0, 1), random.gauss(0,1), random.gauss(0,1))
    spec = sqrt(2*3*(t1 * t1 + t2 * t2 + t3 * t3))
    s = []
    x = []
    for i in xrange(0, n_intervals):
        v = f * cos(spec * i * a + phase)
        x.append(i * a)
        s.append(v)
    return (0, s, x)

def simulate(model, dir, pts, a, C, n_lines):
    pt = pts[0]
    rmin = rmax = dir[0] * pt[0] + dir[1] * pt[1] + dir[2] * pt[2] # compute the projection

    for pt in pts:
        r = dir[0] * pt[0] + dir[1] * pt[1] + dir[2] * pt[2] # compute the projection
        if r < rmin:
            rmin = r
        elif r > rmax:
            rmax = r

    L = rmax - rmin
    (offset, s, x) = model(a, C, L, n_lines)

    n_intervals = len(s)

    sim = []
    for pt in pts:
        r = dir[0] * pt[0] + dir[1] * pt[1] + dir[2] * pt[2] # compute the projection
        interval = int((r - rmin - offset) / a)

        if interval > -1 and interval < n_intervals:
            sim.append(s[interval])
        else:
            sim.append(random.gauss(0, C))

    return sim

n = 1000 #number of bands
dirs = fa.get_dirs(n)

a = 10
C = 10
L = 1000

(offset, s, x) = generate_spherical_covariance(a, C, L, n)

plt.plot(x, s)
plt.show()

(offset, s, x) = generate_gaussian_covariance(a, C, L, n)

plt.plot(x, s)
plt.show()
