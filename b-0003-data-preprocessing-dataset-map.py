raw = [2 * i - 7 for i in range(10)]

print(raw) # [-7, -5, -3, -1, 1, 3, 5, 7, 9, 11]

tf_dataset = tf.data.Dataset.from_tensor_slices(raw)

for item in tf_dataset.map(lambda a: 2 * a + 1):
  print("New item: ", item.numpy())

"""
New item:  -13
New item:  -9
New item:  -5
New item:  -1
New item:  3
New item:  7
New item:  11
New item:  15
New item:  19
New item:  23

"""
