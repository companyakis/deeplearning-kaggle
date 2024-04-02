m = tf.constant([[2018, 2019, 20202], [122, 132, 158]])

print(m)

print(type(m))

print(m.ndim)

"""
tf.Tensor(
[[ 2018  2019 20202]
 [  122   132   158]], shape=(2, 3), dtype=int32)
 
<class 'tensorflow.python.framework.ops.EagerTensor'>

2
"""
