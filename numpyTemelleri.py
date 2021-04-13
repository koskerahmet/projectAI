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


#print("x : ", x) 



# vector
vektor = np.array([1, 2, 3, 4])


# matrix
matris = np.array([[8, 9, 7],
                   [4, 7, 6],
                   [4, 5, 7],
                   [8, 7, 4]])


#print("vektor :", vektor.shape[0])
#print("matris :", matris.shape[1])


c = np.zeros(5)

#print("c :", c)


def naive_relu(x):

	for i in range( x.shape[0] ):
		for j in range( x.shape[1] ):
			x[i, j] = max(x[i, j], 5)

	return x


def naive_add(x, y):

	for i in range( x.shape[0] ):
		for j in range( x.shape[1] ):
			x[i, j] += y[i, j]

	return x




# matrix
ornek = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])


# matrix
ornek2 = np.array([[13, 14, 15],
                   [16, 17, 18],
                   [19, 20, 21],
                   [22, 23, 24]])

#z = naive_relu(ornek)

#z = naive_add(ornek, ornek2)

#print(z)

dizi = np.array([5, 6, 2, 7])

x = np.maximum(8., 0.)

#print("maksimum :", x)


def naive_add_marix_and_vector(x, y):

	for i in range(x.shape[0]):
		for j in range(x.shape[1]):
			print(i, j)      

xe = np.random.random((5, 5 ))
#print(xe)



x = np.array([[1, 2],
              [3, 4]])

#print("x :", x)


y = np.array([5, 6])

#print("y :", y)


xy = np.dot(x, y)
#print(xy)



def naive_add_marix_and_vector(x, y):

	z = np.zeros((x.shape[0], x.shape[1]))

	print("x0 :", z)  

	for i in range(x.shape[0]):
		for j in range(x.shape[1]):
			
			z[(i, j)] += x[i, j] * y[j]

	print("z :", z)        


#naive_add_marix_and_vector(x, y)


def naive_vector_dot(x, y):

	z = 0.
	
	for i in range(x.shape[0]):
		
		z += x[i] * y[i]
		
	return z


def naive_matrix_vector_dot(x, y):
	 
	print(x.shape[0])
	z = np.zeros(x.shape[0])

	for i in range(x.shape[0]):
		z[i] = naive_vector_dot(x[i, :], y)

	return z 

# x matris
# y vektor
#xy = naive_matrix_vector_dot(x, y)


#print("xy :", xy)

#print("x[0, :]", x[0, :])


ornek3 = np.array([[13, 14, 15],
                   [16, 17, 18],
                   [19, 20, 21],
                   [22, 23, 24]])

#print(ornek3[0, :])


#tensör şekillendirme

x = np.array([[0., 1.],
              [2., 3.],
              [4., 5.]])


print("x shape ", x.shape)










