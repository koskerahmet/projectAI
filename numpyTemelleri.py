#!/usr/bin/env python3

#include numpy library
import numpy as np



# scalar
x = np.array(4)


# vector
x = np.array([1, 2, 3, 4])


# matrix
x = np.array([[8, 9, 7],
             [4, 7, 6],
             [4, 5, 7]])


# 3D and More Dimensional Tensors 

x = np.array([ [[5, 8, 9],
                [1, 2, 3],
                [8, 9, 4]],

               [[5, 8, 9],
                [1, 2, 3],
                [8, 9, 4]],
              
               [[5, 8, 9],
                [1, 2, 3],
                [8, 9, 4]] ])


print("x : ", x) 

