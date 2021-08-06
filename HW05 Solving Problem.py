# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:04:21 2021

@author: User
"""

import numpy as np
from scipy.linalg import solve

A = np.array([[0.5, 0.2], [1., 1.]])
b = np.array([10., 30.])
x = solve(A,b)
print('x1, x2 = ', x)

vanilla = x[0]
strawberry = x[1]
max_profit = 2*vanilla + 3*strawberry
print('max profit = ', max_profit)