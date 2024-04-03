raw = [2 * i - 7 for i in range(10)]

print(raw) # [-7, -5, -3, -1, 1, 3, 5, 7, 9, 11]

tf_dataset = tf.data.Dataset.from_tensor_slices(raw)

#buffer_size = 4 means 4 numbers

for number in tf_dataset.shuffle(buffer_size = 4):
  print(number.numpy(), end = " ") # -5 1 -1 -3 7 3 -7 5 11 9 (Note: Your result can be different)
