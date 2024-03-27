#we can see model layers, weights and biases

#initial weights are random values and they'll be updated

print(model.layers)

"""
[<keras.src.layers.reshaping.flatten.Flatten object at 0x7c20ae5f8a30>, 
<keras.src.layers.core.dense.Dense object at 0x7c208f60e500>, 
<keras.src.layers.core.dense.Dense object at 0x7c208f60fa90>, 
<keras.src.layers.core.dense.Dense object at 0x7c208f60cb20>]
"""

hidden_layer_1 = model.layers[1]

weights, biases = hidden_layer_1.get_weights()

print(weights)

print(biases)
