# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd

x = np.linspace(-10.0, 10.0, num = 10000)
y = (2*x**4 - 3*x**3 + 8*x**2 + 1*x - 1)
def function_y(x):
    return(2*x**4 - 3*x**3 + 8*x**2 + 1*x - 1)
dy = 8*x**3 - 9*x**2 +16*x + 1
def loss_function_y(x):
    return(8*x**3 - 9*x**2 +16*x + 1)
plt.plot(x, y, "b")

def GD(start_point, max_times, learning_rate):
    start_x = start_point
    start_y = function_y(start_point)
    x_list, y_list = [start_x], [start_y]
    for step in range(max_times):
        new_x = start_x - learning_rate * loss_function_y(start_x)
        new_y = function_y(new_x)
        if loss_function_y(start_point) == 0:
            break
        if new_x == start_x:
            break
        x_list.append(new_x)
        y_list.append(new_y)
        start_x = new_x
        start_y = new_y
    return(x_list, y_list)





origin = rd.randint(0, 20) - 10
result = GD(origin, 1000, 0.001)
for i in range(len(result[0])):
    plt.plot(result[0][i], result[1][i], "ro")
plt.xlim((-10, 10)) 
plt.ylim((0, 20000))

plt.show()  