#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

x = np.array([[1,2], [3,4]])
print('原矩阵：\n',x)    # Prints "[[1 2]
            #          [3 4]]"
print('转置后：\n',x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
print('秩1向量转置没效果')
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"