#prediction 

X_head_five = X_test[:5]

y_predict_probability = model.predict(X_head_five)

#print(y_predict_probability)

#we should round values

print(y_predict_probability.round(2))

"""

[
  
[0.   0.   0.   0.   0.   0.01 0.   0.04 0.   0.94]

[0.   0.   1.   0.   0.   0.   0.   0.   0.   0.  ]

[0.   1.   0.   0.   0.   0.   0.   0.   0.   0.  ]

[0.   1.   0.   0.   0.   0.   0.   0.   0.   0.  ]

[0.16 0.   0.01 0.   0.   0.   0.83 0.   0.   0.  ]
 
 ]

"""
