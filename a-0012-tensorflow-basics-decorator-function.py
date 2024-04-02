#optimized function

@tf.function
def square(x: int):
  return x ** 2

data = tf.constant(np.arange(5,10))

print(square(data))

"""
tf.Tensor([25 36 49 64 81], shape=(5,), dtype=int64)
"""
