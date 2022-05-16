import pandas as pd
import numpy as np
from math import log, sqrt
import matplotlib.pyplot as plt
from scipy.special import ndtri

dt = 1
size = 26225
mu = 0.04
sigma = 0.4

ρ = [0, 0.25, 0.5, 0.75, 0.95]

size = 1000

def dBgenerator(p):
    dB=[]
    covi = [[1, p],
            [p, 1]]
    for i in range(size):
        nor = np.random.multivariate_normal([0, 0], covi)
        dB.append(nor)
    return np.array(dB)


def brownA(sigma, mu, rdb):
    start1 = 0
    start2 = 0
    data1 = [0]
    data2 = [0]
    for i in range(size):
        start1 = start1 + dt * mu + sigma * rdb[i, 0]
        data1.append(start1)
        start2 = start2 + dt * mu + sigma * rdb[i, 1]
        data2.append(start2)
    data1 = np.array(data1)
    data2 = np.array(data2)
    return data1, data2


for i in ρ:
    dB1 = dBgenerator(i)
    data11, data12 = brownA(sigma, mu, dB1)
    plt.plot(data11)
    plt.plot(data12)
    plt.title('zależne trajektorie ABM\nρ = %.2f' % i)
    plt.show()