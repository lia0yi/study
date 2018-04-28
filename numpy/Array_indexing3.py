#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print(a,'\n')

# An example of integer array indexing.
# 对应(0,0)(1,1)(2,0),前后分别对应好
print(a[[0, 1, 2], [0, 1, 0]],'\n')  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]),'\n')  # Prints "[1 4 5]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]],'\n')  # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]),'\n')  # Prints "[2 2]"