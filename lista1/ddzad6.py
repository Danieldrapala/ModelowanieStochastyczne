import pandas as pd
import numpy as np
from math import log, sqrt
import matplotlib.pyplot as plt

def plots1(dataset, av, var, name):
    mu, sigma = av, sqrt(var)

    count, bins, ignored = plt.hist(dataset, 100, density=True, color='blue', label=name)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r', label='norm')
    plt.legend()
    name = 'Histogram ' + name
    plt.title(name)
    plt.show()



def plots2(dataset, av, var, name):
    norm = np.random.normal(av, sqrt(var),dataset.shape[0])
    norm = np.sort(norm)
    dataset = np.sort(dataset)
    y = np.linspace(0, 1, dataset.shape[0])

    plt.plot(dataset, y, label=name,
             linewidth=2, color='blue')
    plt.plot(norm, y, label='norm',
             linewidth=2, color='r')
    plt.legend()
    name = 'empiric distribution linear scale '
    plt.title(name)
    plt.show()

def plots3(dataset, av, var, name):
    norm = np.random.normal(av, sqrt(var),dataset.shape[0])
    norm = np.sort(norm)
    dataset = np.sort(dataset)
    y = np.linspace(0, 1, dataset.shape[0])

    plt.plot(dataset, y, label=name,
             linewidth=2, color='blue')
    plt.plot(norm, y, label='norm',
             linewidth=2, color='r')
    plt.yscale('log')
    plt.legend()
    name = 'empiric distribution scale semi-log'
    plt.title(name)
    plt.show()

def plots4(dataset, av, var, name = 'tak'):
    norm = np.random.normal(av, sqrt(var),dataset.shape[0])
    norm = np.sort(norm)
    dataset = np.sort(dataset)
    y = np.linspace(0, 1, dataset.shape[0])

    plt.plot(1-dataset, y, label=name,
             linewidth=2, color='blue')
    plt.plot(1-norm, y, label='norm',
             linewidth=2, color='r')
    plt.yscale('log')
    plt.xscale('log')
    plt.legend()
    name = 'empiric distribution log-log scale'
    plt.title(name)
    plt.show()

def plots(dataset, av, var, name):
    plots1(dataset, av, var, name)
    plots2(dataset, av, var, name)
    plots3(dataset, av, var, name)
    plots4(dataset, av, var, name)

def zwrotylog(dataset):
    zl = []
    for i in range(len(dataset)-1):
        zl.append(log(dataset[i+1]/dataset[i]))

    return np.array(zl)

djia = pd.read_csv('DJIA.txt', delimiter='\t')
djia = np.array(djia)
z1 = zwrotylog(djia)

av = np.average(z1)
var = np.var(z1)
print(var, av)
plots(z1, av, var, 'zwroty log')
