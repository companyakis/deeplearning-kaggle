"""
784 * 0 = 0
784 * 300 + 300 = 235500 (300 bias)
300 * 100 + 100 = 30100 (100 bias)
100 * 10 + 10 = 1010 (10 bias)
"""

model.summary()


"""
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 flatten (Flatten)           (None, 784)               0         
                                                                 
 dense (Dense)               (None, 300)               235500    
                                                                 
 dense_1 (Dense)             (None, 100)               30100     
                                                                 
 dense_2 (Dense)             (None, 10)                1010  
"""
