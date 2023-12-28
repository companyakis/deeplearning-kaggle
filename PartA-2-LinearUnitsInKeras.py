# The easiest way to create a model in Keras is through keras.Sequential

# We could define a linear model accepting three input features (a, b, and c)
# and producing a single output (d)

from tensorflow import keras
from tensorflow.keras import layers

# we are creating a network with 1 linear unit

model = keras.Sequential([layers.Dense(units=1, input_shape=[3])])

# we define how many outputs we want (units, output d)
# setting input_shape=[3] ensures the model will accept three features as input (a, b and c)
