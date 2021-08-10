# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:04:21 2021

@author: Pimchanok Duang-In 640631125
"""

from scipy.optimize import linprog
obj = [-2,-3]

A = [[0.5, 0.2],
     [1., 1.]]
b = [10, 30]

bnd = [(0, float('inf')),
       (0, float('inf'))]

opt = linprog(c = obj, A_ub = A, b_ub = b,
              bounds=bnd, method='revised simplex')
print(opt)
print()
print('x1, x2 = ', opt.x)
print('Optimize profit is:', opt.fun*(-1))
