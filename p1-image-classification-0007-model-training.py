#model-training1.py

#training and fit method

#30 epochs

model_training = model.fit(X_train, y_train, epochs = 30, validation_data = (X_validation, y_validation))

"""
Epoch 23/30
1719/1719 [==============================] - 9s 5ms/step - loss: 0.2561 - accuracy: 0.9082 - val_loss: 0.3392 - val_accuracy: 0.8738
Epoch 24/30
1719/1719 [==============================] - 8s 4ms/step - loss: 0.2505 - accuracy: 0.9095 - val_loss: 0.3196 - val_accuracy: 0.8810
Epoch 25/30
1719/1719 [==============================] - 9s 5ms/step - loss: 0.2464 - accuracy: 0.9110 - val_loss: 0.3218 - val_accuracy: 0.8794
Epoch 26/30
1719/1719 [==============================] - 8s 5ms/step - loss: 0.2428 - accuracy: 0.9130 - val_loss: 0.3143 - val_accuracy: 0.8856
Epoch 27/30
1719/1719 [==============================] - 7s 4ms/step - loss: 0.2376 - accuracy: 0.9148 - val_loss: 0.3233 - val_accuracy: 0.8830
Epoch 28/30
1719/1719 [==============================] - 8s 5ms/step - loss: 0.2349 - accuracy: 0.9155 - val_loss: 0.3139 - val_accuracy: 0.8858
Epoch 29/30
1719/1719 [==============================] - 8s 5ms/step - loss: 0.2313 - accuracy: 0.9165 - val_loss: 0.3244 - val_accuracy: 0.8830
Epoch 30/30
1719/1719 [==============================] - 8s 4ms/step - loss: 0.2274 - accuracy: 0.9193 - val_loss: 0.3115 - val_accuracy: 0.8836

"""
