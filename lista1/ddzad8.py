import numpy as np
import matplotlib.pyplot as plt

dt = 1
alfa = 0.1
beta = 8
sigma = 0.4

size = 500

def dyf():
    data = [20]
    for i in range(1,size):
        data.append(data[i-1] +(alfa*(beta - data[i-1]) + sigma*np.random.normal(0, dt)))
    return np.array(data)

def trend():
    y = [20]
    for i in range(1,size-1):
        y.append(y[i-1] + alfa*(beta - y[i-1]))
    return np.array(y)

y = trend()
data1 = dyf()
data2 = dyf()
data3 = dyf()

plt.plot(y, color='black', label='trend', linewidth=0.3)
plt.plot(data1, label='mean 1', linewidth=0.5)
plt.plot(data2, label='mean 2', linewidth=0.5)
plt.plot(data3, label='mean 3', linewidth=0.5)
plt.title('trajektorie dyfuzji powracającej')
plt.legend()
plt.show()
