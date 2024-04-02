#mutable and immutable

var = tf.Variable([333, -222])

const = tf.constant([333, -222])

var[1].assign(-333)

print(var) # <tf.Variable 'Variable:0' shape=(2,) dtype=int32, numpy=array([ 333, -333], dtype=int32)>

#const[1].assign(555) #Throw an error!
