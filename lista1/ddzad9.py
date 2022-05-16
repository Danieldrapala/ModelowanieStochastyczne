import numpy as np
import matplotlib.pyplot as plt


ρ = [0, 0.25, 0.5, 0.75, 0.95]

size = pow(10, 5)

for i in ρ:
    matrix = [[1, i],
            [i, 1]]
    nor = np.random.multivariate_normal([0,0], matrix, size)
    print(nor)
    plt.scatter(nor[:, 1], nor[:, 0], marker='.', color='blue', s=1.5)
    plt.title('skorelowany dwuwymiarowy rozkład normalny\nρ = %.2f' % i)
    plt.show()