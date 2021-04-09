#!/usr/bin/env python3

from keras.datasets import mnist
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


print("number of axis :",train_images.ndim)
print("number of image :",train_images.shape)
print("data type of image :",train_images.shape)


#plt.imshow(train_images[5], cmap=plt.cm.binary)
#plt.show()

my_slice = train_images[10:100]
print("my slice :",my_slice.shape)

















