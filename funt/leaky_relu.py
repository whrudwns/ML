import numpy as np
import matplotlib.pyplot as plt

a = 0.1
def leaky_relu(x):
    return np.maximum(a*x,x)


x = np.arange(-5.0, 5.0, 0.1)
y = leaky_relu(x)
plt.axhline(y = 0, color = "r", linestyle = ":")
plt.title("Leaky Relu")
plt.plot(x,y)
plt.show()
