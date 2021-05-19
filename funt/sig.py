import numpy as np
import matplotlib.pyplot as plt
def sig(x):
    y = 1/(1+np.exp(-x))
    return y

x = np.arange(-5.0,5.0,0.1)
y = sig(x)
plt.plot([0,0],[1.0,0.0], ':') # 가운데 점선 추가
plt.title("sigmoid funciton")
plt.plot(x,y)
plt.show()
