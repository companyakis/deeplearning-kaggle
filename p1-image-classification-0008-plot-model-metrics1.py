import matplotlib.pyplot as plt

import pandas as pd

df = pd.DataFrame(model_training.history)

print(df.head())

"""
       loss  accuracy  val_loss  val_accuracy
0  0.714981  0.766545  0.500281        0.8298
1  0.485118  0.832200  0.458894        0.8340
2  0.440155  0.845345  0.426192        0.8524
3  0.415888  0.854491  0.395892        0.8626
4  0.395279  0.861618  0.392725        0.8604

"""
