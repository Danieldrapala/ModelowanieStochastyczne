import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ndtri
from math import log, exp, sqrt, pi, erf


def pareto(a=0, b=1, size=1000):
    pareto = np.random.uniform(a, b, size)
    pareto = np.sort(pareto)
    paretoval = np.zeros(pareto.shape[0])
    for i in range(pareto.shape[0]):
        paretoval[i] = 1 * pow(pareto[i], -1 / 3)
    return paretoval


def wykladniczy(a=0, b=1, size=1000):
    wykl = np.random.uniform(a, b, size)
    wykl = np.sort(wykl)
    wyklval = np.zeros(wykl.shape[0])
    for i in range(wykl.shape[0]):
        wyklval[i] = (-1 / 1) * log(wykl[i])
    return wyklval


def logarytmiczny(a=0, b=1, size=1000):
    wykl = np.random.uniform(a, b, size)
    wykl = np.sort(wykl)
    wyklval = np.zeros(wykl.shape[0])
    for i in range(wykl.shape[0]):
        wyklval[i] = exp(ndtri(wykl[i]))
    return wyklval


def paretp(z):
    return (2 * pow(1, 2)) / (pow(z, 2 + 1))


def paretd(z):
    return 1 - pow((1 / z), 2)


def wykp(z):
    return 1 * exp(-1 * z)


def wykd(z):
    return 1 - exp(-1 * z)


def logp(z):
    return (1 / (sqrt(2 * pi) * 1 * z)) * (exp((- pow(log(z - 0), 2)) / 2 * pow(1, 2)))


def logd(z):
    return (1 / 2 + (1 / 2) * erf((log(z)) / sqrt(2)))


def plots1(dataset, name, subplot):
    k = np.linspace(min(dataset), max(dataset), dataset.shape[0])
    g = []
    if name == 'pareto':
        for i in range(len(k)):
            g.append(paretp(k[i]))
    elif name == 'lognormal':
        for i in range(len(k)):
            g.append(logp(k[i]))
    else:
        for i in range(len(k)):
            g.append(wykp(k[i]))
    subplot.hist(dataset, 100, density=True, color='blue', label=name)
    subplot.plot(k, g,
             linewidth=2, color='r', label='theory')
    subplot.legend()
    name = 'Histogram ' + name
    subplot.set_title(name)
    subplot.grid()


def plots2(dataset, name, subplot):
    k = np.linspace(min(dataset), max(dataset), dataset.shape[0])
    g = []
    if name == 'pareto':
        for i in range(len(k)):
            g.append(paretd(k[i]))
    elif name == 'lognormal':
        for i in range(len(k)):
            g.append(logd(k[i]))
    else:
        for i in range(len(k)):
            g.append(wykd(k[i]))
    dataset = np.sort(dataset)
    y = np.linspace(0, 1, dataset.shape[0])
    subplot.plot(dataset, y, label=name,
             linewidth=2, color='blue')
    subplot.plot(k, g,
             linewidth=2, color='r', label='theory')
    subplot.legend()
    name = 'distribution function linear scale '
    subplot.set_title(name)
    subplot.grid()


def plots3(dataset, name, subplot):
    k = np.linspace(min(dataset), max(dataset), dataset.shape[0])
    g = []
    if name == 'pareto':
        for i in range(len(k)):
            g.append(paretd(k[i]))
    elif name == 'lognormal':
        for i in range(len(k)):
            g.append(logd(k[i]))
    else:
        for i in range(len(k)):
            g.append(wykd(k[i]))
    dataset = np.sort(dataset)
    y = np.linspace(0, 1, dataset.shape[0])

    subplot.semilogy(dataset, y, label=name,
             linewidth=2, color='blue')
    subplot.semilogy(k, g,
             linewidth=2, color='r', label='theory')
    subplot.legend()
    name = 'distribution function semi-log scale'
    subplot.set_title(name)
    subplot.grid()


def plots4(dataset, name, subplot):
    k = np.linspace(min(dataset), max(dataset), dataset.shape[0])
    g = []
    if name == 'pareto':
        for i in range(len(k)):
            g.append(paretd(k[i]))
        dataset = dataset -1
        k= k-1
    elif name == 'lognormal':
        for i in range(len(k)):
            g.append(logd(k[i]))
    else:
        for i in range(len(k)):
            g.append(wykd(k[i]))
    dataset = np.sort(dataset)

    y = np.linspace(0, 1, dataset.shape[0])

    subplot.loglog(1-dataset, y, label=name,
             linewidth=1, color='blue')
    subplot.loglog(1-k, g,
             linewidth=1, color='r', label='theory')

    subplot.legend()
    name = 'distribution function log-log ' + name
    subplot.set_title(name)
    subplot.grid()


def plots(dataset, name):
    figure, axis = plt.subplots(2, 2)
    figure.suptitle(name)

    plots1(dataset, name, axis[0][0])
    plots2(dataset, name, axis[0][1])
    plots3(dataset, name, axis[1][0])
    plots4(dataset, name, axis[1][1])
    figure.tight_layout()
    plt.show()


par = pareto()
wyk = wykladniczy()
loga = logarytmiczny()
plots(par, 'pareto')
plots(wyk, 'wykladniczy')
plots(loga, 'lognormal')
