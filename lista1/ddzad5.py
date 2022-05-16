import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
dt = 1
mu = 0.01
sigma = 0.04

size = 1000

def brownG():
    data = [10]
    for i in range(size-1):
        data.append(data[i] + dt*mu*data[i] + sigma*np.random.normal(0, dt)*data[i])
    return np.array(data)

x = np.linspace(0, size, size)

y = [10]
for i in range(size-1):
    y.append(y[-1]+mu*y[-1])
y = np.array(y)


data1 = brownG()
data2 = brownG()
data3 = brownG()
plt.plot(y, color='black', label='trend')
plt.plot(data1, label='set 1')
plt.plot(data2, label='set 2')
plt.plot(data3, label='set 3')
plt.title('GBM plots \nsigma = %.2f\nmu = %.2f' % (sigma, mu))

plt.legend()
plt.savefig('GBM plots')
plt.show()