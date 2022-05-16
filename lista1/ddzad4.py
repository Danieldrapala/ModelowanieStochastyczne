import numpy as np
import matplotlib.pyplot as plt

dt = 1
mu = 0.04
sigma = 0.4

def brownA(value0):
    data = [value0]
    for i in range(1000):
        start = data[i] + dt*mu + sigma*np.random.normal(0,dt)
        data.append(start)
    return np.array(data)


x = np.linspace(0, 1000)
uxdt = x*mu
data1 = brownA(10)
data2 = brownA(10)
data3 = brownA(10)
plt.plot(x, (uxdt+10), color='black', label='trend')
plt.plot(data1, label='1')
plt.plot(data2, label='2')
plt.plot(data3, label='3')
plt.title('ABM plots \nsigma = %.2f\nmu = %.2f' % (sigma, mu))
plt.legend()
plt.show()
