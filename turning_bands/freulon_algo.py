# -*- coding: utf-8 -*-
__author__ = 'gogo40'

# Implementation of the Freulon algorithm to generate directions weakly discrepant;
#
# (c) 2016, LPM/UFRGS, Péricles Lopes Machado (eu@gogo40.com)

from math import *

def get_f(b, n):
    u = 0
    p = float(b)
    while n > 0:
        u = u + (n % b) / p
        n = n / b
        p = p * b
    return u

def get_u(n):
    return get_f(2, n)

def get_v(n):
    return get_f(3, n)

def get_dir(k):
    u = get_u(k)
    v = get_v(k)
    f = sqrt(1 - v * v)
    return (cos(2 * pi * u) * f, sin(2 * pi * u) * f, v)

def get_dirs(n):
    dirs = []
    for i in xrange(0, n):
        dirs.append(get_dir(i))
    return dirs

