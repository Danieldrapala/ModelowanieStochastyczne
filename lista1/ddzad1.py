import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ndtri
from scipy.stats import norm


def rule_of_dozen(a=0, b=1, size =1000):
    rod = np.zeros(size)
    for i in range(len(rod)):
        v = np.random.uniform(a, b, 12)
        rod[i] = np.sum(v) - 6
    return rod


def inverse_transform(a=0, b=1, size=1000):
    invtrans = np.random.uniform(a, b, size)
    invtrans = np.sort(invtrans)
    val = np.zeros(invtrans.shape[0])
    for i in range(invtrans.shape[0]):
        val[i] = ndtri(invtrans[i])
    return val


def Box_Muller(a=0, b=1, size=1000):
    U1 = np.random.uniform(a, b, size)
    U2 = np.random.uniform(a, b, size)
    R = np.sqrt(-2 * np.log(U1))
    Theta = 2 * np.pi * U2
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    return X, Y


def empirical_distribution(data):
    v = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        v[i] = i / data.shape[0]
    return v


def plot1(dataset, mu, sigma, axis ):
    count, bins, ignored = axis.hist(dataset, 100, density=True, color='blue')
    axis.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r', label='standard', alpha=0.5)
    axis.legend()
    name = 'Hist'
    axis.set_title(name)
    axis.grid()



def plot2(dataset, mu, sigma, subplot):
    dataset = np.sort(dataset)
    y = np.linspace(0, 1, dataset.shape[0])
    k = np.linspace(min(dataset), max(dataset), dataset.shape[0])
    g = norm.cdf(k)
    subplot.plot(dataset, y,
             linewidth=2, color='blue')
    subplot.plot(k, g,
             linewidth=2, color='r', label='theory',alpha=0.5)
    subplot.legend()
    name = ' linear dist '
    subplot.set_title(name)
    subplot.grid()

def plot3(dataset, mu, sigma,subplot):
    dataset = np.sort(dataset)
    y = np.linspace(0, 1, dataset.shape[0])
    k = np.linspace(min(dataset), max(dataset), dataset.shape[0])
    g = norm.cdf(k)
    subplot.semilogy(dataset, y,
             linewidth=2, color='blue')
    subplot.semilogy(k, g,
             linewidth=2, color='r', label='theory',alpha=0.5)
    subplot.legend()
    name = 'semi-log dist'
    subplot.set_title(name)
    subplot.grid()


def plot4(dataset, mu, sigma, subplot):
    onlypositive = []
    for i in range(len(dataset)):
        if dataset[i]>0:
            onlypositive.append(dataset[i])
    onlypositive = np.sort(dataset)
    y = np.linspace(0, 1, onlypositive.shape[0])
    k = np.linspace(min(onlypositive), max(onlypositive), onlypositive.shape[0])
    g = norm.cdf(k)
    subplot.loglog(1-onlypositive, y,
             linewidth=2, color='blue')
    subplot.loglog(1-k, g,
             linewidth=2, color='r', label='theory',alpha=0.5)

    subplot.legend()
    name = 'log-log dist'
    subplot.set_title(name)
    subplot.grid()


def plots(dataset, name):
    mu, sigma = 0, 1
    figure, axis = plt.subplots(2, 2)
    figure.suptitle(name)

    plot1(dataset, mu, sigma, axis[0][0])
    plot2(dataset, mu, sigma, axis[0][1])
    plot3(dataset, mu, sigma, axis[1][0])
    plot4(dataset, mu, sigma, axis[1][1])
    figure.tight_layout()
    plt.show()

tw = rule_of_dozen()
it = inverse_transform()
bm1, bm2 = Box_Muller()


plots(tw, 'Rule Of Dozen')
plots(it, 'Inverse Transform')
plots(bm1, 'Box-Muller set1')
plots(bm2, 'Box-Muller set2')
