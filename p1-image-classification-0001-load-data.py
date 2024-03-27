import tensorflow as tf
import numpy as np

# load fashion mnist dataset
fashion_mnist_data = tf.keras.datasets.fashion_mnist.load_data()

print(type(fashion_mnist_data)) #<class 'tuple'>

#print(fashion_mnist_data[0])
