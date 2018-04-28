#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

x = np.array([[1,2],
			  [3,4]])
y = np.array([[5,6],
			  [7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print('向量内积：\n')
print(v.dot(w))#向量内积
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print('矩阵乘向量：\n')
print(x.dot(v))#矩阵乘法
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print('矩阵乘矩阵：\n')
print(x.dot(y))
print(np.dot(x, y))