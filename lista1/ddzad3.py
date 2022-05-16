import statistics

import numpy as np

a = 1
b = 3

def mean_confidence_interval(data, confidence=0.96):

    m = np.mean(data)
    se = statistics.variance(data)
    h = se * ((1 +confidence)/ np.sqrt(len(data)))
    print(2*(m-h), 2*(m+h))

def fun(x):
    return x ** 2 + x

def funkcja(x):
    y = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        y[i] = fun(x[i])
    return y


def scalar(u, min, max):
    for i in range(u.shape[0]):
        u[i] = u[i] * (max - min) + min
    return u


def mc(ux, uy):
    under = []
    for i in range(ux.shape[0]):
        if fun(ux[i]) >= uy[i]:
            under.append([ux[i], uy[i]])
    return  under



x = scalar(np.random.uniform(0, 1, 1000),a,b)
y1 = funkcja(x)
uy1 = scalar(np.random.uniform(0, 1, 1000),0,np.max(y1))
good = mc(x, uy1)
ratio = len(good) / len(x)
field = (b - a) * (np.max(y1))
print(ratio * field)
mean_confidence_interval(y1)

