#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])

# 理论上来讲这种操作不符合矩阵的加法运算
# numpy中有以下约定：
# 1.If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
# 2.The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.
# 3.The arrays can be broadcast together if they are compatible in all dimensions.
# 4.After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
# 5.In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension
# 1.如果数组不具有相同的等级，则用1来预先设置较低等级数组的形状，直到两个形状具有相同的长度。
# 2.如果这两个数组在维度中具有相同的大小，或者如果其中一个数组在该维度中的大小为1，则说这两个数组在维度上是兼容的。
# 3.如果阵列在所有维度上兼容，阵列可以一起广播。
# 4.广播后，每个阵列的行为就好像它的形状等于两个输入阵列的形状的元素最大值。
# 5.在一个数组的大小为1而另一个数组的大小大于1的任何维中，第一个数组的行为就好像它是沿着该维复制的

y = x + v  # Add v to each row of x using broadcasting
print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"