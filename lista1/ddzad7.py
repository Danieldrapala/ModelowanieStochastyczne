import pandas as pd
import numpy as np
from math import log, sqrt
import matplotlib.pyplot as plt

dt = 1

def zwrotylog(dataset):
    zl = []
    for i in range(len(dataset)-1):
        zl.append(log(dataset[i+1]/dataset[i]))
    return np.array(zl)

def zwroty(dataset):
    z = []
    for i in range(len(dataset)-1):
        z.append((dataset[i+1]-dataset[i]))
    return np.array(z)


def brownA(sigma, mu):
    data = [51.6]
    for i in range(26225):
        data.append(data[i] + dt*mu + sigma*np.random.normal(0, dt))
    return np.array(data)

def brownG(sigma, mu):
    data = [51.6]
    for i in range(26225):
        data.append(data[i] + dt*mu*data[i] + sigma*np.random.normal(0, dt)*data[i])
    return np.array(data)

djia = pd.read_csv('DJIA.txt', delimiter='\t')
djia = np.array(djia)

z1 = zwroty(djia)
z2 = zwrotylog(djia)


std1 = np.std(z1)
mean1 = np.mean(z1)

std2 = np.std(z2)
mean2 = np.mean(z2)

abm = brownA(std1, mean1)
gbm = brownG(std2,mean2 + (std2**2)/2)

plt.plot(djia[:], label='DJIA')
plt.plot(abm, label='ABM \nsigma = %.5f\nmu = %.5f' % ((std1), mean1))
plt.plot(gbm, label='GBM \nsigma = %.5f\nmu = %.5f' % ((std2), (mean2) + (std2**2)/2))
plt.title('Dopasowanie ruchów Browna do indeksy DJIA')
plt.legend()
plt.show()
