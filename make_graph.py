#!/usr/bin/env python
# coding: utf-8

# In[1]:
'''
2次元配列を受け取ってグラフを作成する

def scatter: 配列x[2, n]の散布図を、xy平面（x = x[0], y = x[1]）で図示

def line: 直線 w11 * x1 + w12 * x2 + b1 = w21 * x1 + w22 * x2 * b2
          をxy平面で図示
'''


import matplotlib.pyplot as plt
import numpy as np

def scatter(x, Color = None, Marker = None):
    n = len(x)
    for i in range(n):
        plt.scatter(x[i, 0], x[i, 1], color = Color, marker = Marker)

def line(w, b, Min = -4, Max = 14, Index = [0, 1],\
         Color = None, Marker = None):
    p = Index[0]
    q = Index[1]
    x = np.arange(Min, Max)
    y = ((w[0, p] - w[0, q]) * x + b[p] - b[q]) / (w[1, q] - w[1, p])
    plt.plot(x, y, color = Color, marker = Marker)
        


# In[ ]:




