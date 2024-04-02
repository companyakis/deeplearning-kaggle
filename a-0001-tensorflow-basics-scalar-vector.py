import tensorflow as tf

import numpy as np

print(tf.__version__) # 2.15.0

# create a scalar/constant tensor

sc = tf.constant(22)

print(sc) # tf.Tensor(22, shape=(), dtype=int32)

print(type(sc)) # <class 'tensorflow.python.framework.ops.EagerTensor'>

print(sc.ndim) # 0

# create a vector

vec = tf.constant([3, 7, 22])

print(vec) # tf.Tensor([ 3  7 22], shape=(3,), dtype=int32)

print(type(vec)) # <class 'tensorflow.python.framework.ops.EagerTensor'>

print(vec.ndim) # 1

