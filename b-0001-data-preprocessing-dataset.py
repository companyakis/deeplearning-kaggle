import tensorflow as tf
import numpy as np

raw = tf.range(8)

#print(raw) # tf.Tensor([0 1 2 3 4 5 6 7], shape=(8,), dtype=int32)

dataset = tf.data.Dataset.from_tensor_slices(raw)

for i in dataset:
  print(i.numpy(), end = " ") # 0 1 2 3 4 5 6 7 


listed = list(dataset.as_numpy_iterator())

print(listed) # [0, 1, 2, 3, 4, 5, 6, 7]

# take the desired items

for i in dataset.take(4):
  print(i.numpy(), end = "--") # 0--1--2--3--
