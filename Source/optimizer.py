import numpy as np
from neupy import algorithms
from neupy.layers import *

x_train = np.array([[1, 2], [3, 4]])
y_train = np.array([[1], [0]])

optimizer = algorithms.QuasiNewton(
    Input(2) >> Sigmoid(3) >> Sigmoid(1),
    update_function='bfgs')

optimizer.train(x_train, y_train, epochs=10)
