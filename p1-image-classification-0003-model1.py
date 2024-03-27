#create model

#28*28 images => input_shape = [28, 28]

#for hidden layers, we use relu activation 

#we have 10 classes, we use softmax activation for output (here, classification)

tf.random.set_seed(42)

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape = [28, 28]),
    tf.keras.layers.Dense(300, activation = "relu"),
    tf.keras.layers.Dense(100, activation = "relu"),
    tf.keras.layers.Dense(10, activation = "softmax")
])
