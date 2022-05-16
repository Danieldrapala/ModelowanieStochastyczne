import numpy as np
import matplotlib.pyplot as plt

# parametry
beta = .5
gamma = .1
eta = .1
sigma = .1
N = 1000
T = 100
y = 1
dt = 1

T_ode = np.linspace(0, T, T * dt)


def SIS_ode(y0, beta, gamma, N, t):
    S = [N - 1]
    I = [y0]
    for i in range(t - 1):
        x = beta * I[-1] * S[-1] / N
        S.append(S[-1] - x + gamma * I[-1])
        I.append(I[-1] + x - gamma * I[-1])
    S = np.array(S)
    I = np.array(I)
    return S, I


def SEIRS_ode(y0, beta, gamma, eta, sigma, N, t):
    S = [N - 1]
    I = [y0]
    R = [0]
    E = [0]
    for i in range(t - 1):
        x = beta * I[-1] * S[-1] / N
        S.append(S[-1] - x + eta * R[-1])
        E.append(E[-1] + x - sigma * E[-1])
        I.append(I[-1] + sigma * E[-1] - gamma * I[-1])
        R.append(R[-1] + gamma * I[-1] - eta * R[-1])
    S = np.array(S)
    E = np.array(E)
    I = np.array(I)
    R = np.array(R)
    return S, I, R, E


def SIRS_ode(y0, beta, gamma, eta, N, t):
    S = [N - 1]
    I = [y0]
    R = [0]
    for i in range(t - 1):
        x = beta * I[-1] * S[-1] / N
        S.append(S[-1] - x + eta * R[-1])
        I.append(I[-1] + x - gamma * I[-1])
        R.append(R[-1] + gamma * I[-1] - eta * R[-1])
    S = np.array(S)
    I = np.array(I)
    R = np.array(R)
    return S, I, R


def SI_ode(y0, beta, N, t, deltat):
    S = [N - 1]
    I = [y0]
    for i in range(t - 1):
        x = beta * I[-1] * S[-1] / N
        S.append(S[-1] - deltat * x)
        I.append(I[-1] + deltat * x)
    S = np.array(S)
    I = np.array(I)
    return S, I


def SEIR_ode(y0, beta, gamma, sigma, N, t):
    S = [N - 1]
    I = [y0]
    R = [0]
    E = [0]
    for i in range(t - 1):
        x = beta * I[-1] * S[-1] / N
        S.append(S[-1] - x)
        E.append(E[-1] + x - sigma * E[-1])
        I.append(I[-1] + sigma * E[-1] - gamma * I[-1])
        R.append(R[-1] + gamma * I[-1])
    S = np.array(S)
    E = np.array(E)
    I = np.array(I)
    R = np.array(R)
    return S, I, R, E


def plot1(S,I,R,E, name, subplot):
    if S.size:
        subplot.plot(T_ode, S, label=r'$S_t$')
    if I.size:
        subplot.plot(T_ode, I, label=r'$I_t$')
    if R.size:
        subplot.plot(T_ode, R, label=r'$R_t$')
    if E.size:
        subplot.plot(T_ode, E, label=r'$E_t$')
    subplot.set_xlabel('Czas')
    subplot.set_ylabel('Liczba przypadków')
    subplot.set_title('Wykres liniowy dla ' + name)
    subplot.legend()
    subplot.grid()


def plot2(S, I, R, E, name, subplot):
    if S.size:
        subplot.plot(T_ode, S, label=r'$S_t$')
    if I.size:
        subplot.plot(T_ode, I, label=r'$I_t$')
    if R.size:
        subplot.plot(T_ode, R, label=r'$R_t$')
    if E.size:
        subplot.plot(T_ode, E, label=r'$E_t$')
    subplot.set_yscale('log')
    subplot.set_xlabel('Czas')
    subplot.set_ylabel('Liczba przypadków')
    subplot.set_title('Wykres semilog dla ' + name)
    subplot.legend()
    subplot.grid()


def plot3(S, I, R, E, name, subplot):
    if S.size:
        subplot.loglog(T_ode, S, label=r'$S_t$')
    if I.size:
        subplot.loglog(T_ode, I, label=r'$I_t$')
    if R.size:
        subplot.loglog(T_ode, R, label=r'$R_t$')
    if E.size:
        subplot.loglog(T_ode, E, label=r'$E_t$')
    subplot.set_xlabel('Czas')
    subplot.set_ylabel('Liczba przypadków')
    subplot.set_title('Wykres log-log dla ' + name)
    subplot.legend()
    subplot.grid()


def drawplots(S, I, R, E, name):
    figure, axis = plt.subplots(1, 3)
    figure.suptitle(name)
    plot1(S, I, R, E, name, axis[0])
    plot2(S, I, R, E, name, axis[1])
    plot3(S, I, R, E, name, axis[2])
    plt.show()

blank = np.array([])
S1, I1 = SIS_ode(y, beta, gamma, N, T)

drawplots(S1,I1,blank,blank, "SIS")

S2, I2, R2 = SIRS_ode(y, beta, gamma, eta, N, T)

drawplots(S2, I2, R2,blank, "SIRS")

S3, I3 = SI_ode(y, beta, N, T, dt)

drawplots(S3, I3, blank, blank, "SI")

S4, I4, R4, E4 = SEIRS_ode(y, beta, gamma, eta, sigma, N, T)

drawplots(S4, I4, R4, E4, "SEIRS")

S5, I5, R5, E5 = SEIR_ode(y, beta, gamma, sigma, N, T)

drawplots(S5, I5, R5, E5, "SEIR")

