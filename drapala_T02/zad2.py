import numpy as np
from scipy.integrate import RK45
import matplotlib.pyplot as plt

# parametry:
beta = .5
gamma = .1
N = 1000
T = 100
dt = 1  # krok czasowy na wykresie - nie ma wpływu na dokładność rozwiązania
steps = int(T / dt)
eta = .1
sigma = .1


def SIS_ode(t, y, params):
    beta, gamma, N = params
    S0, I0 = y
    S1 = -beta * I0 * S0 / N + gamma * I0
    I1 = beta * I0 * S0 / N - gamma * I0
    return [S1, I1]


def SI_ode(t, y, params):
    beta, gamma, N = params
    S0, I0 = y
    S1 = -beta * I0 * S0 / N
    I1 = beta * I0 * S0 / N
    return [S1, I1]

def SIRS_ode(t, y, params):
    beta, gamma, eta, N = params
    S0, I0, R0 = y
    S1 = -beta * I0 * S0 / N + eta * R0
    I1 = beta * I0 * S0 / N - gamma * I0
    R1 = gamma * I0 - eta * R0
    return [S1, I1, R1]

def SEIRS_ode(t, y, params):
    beta, gamma, eta, sigma, N = params
    S0, I0, R0, E0, = y
    S1 = -beta * I0 * S0 / N + eta * R0
    E1 = beta * I0 * S0 / N - sigma * E0
    I1 = sigma * E0 - gamma * I0
    R1 = gamma * I0 - eta * R0
    return [S1, I1, R1, E1]

def SEIR_ode(t, y, params):
    beta, gamma, eta, sigma, N = params
    S0, I0, R0, E0, = y
    S1 = -beta * I0 * S0 / N
    E1 = beta * I0 * S0 / N - sigma * E0
    I1 = sigma * E0 - gamma * I0
    R1 = gamma * I0
    return [S1, I1, R1, E1]

def si_RK():
    T_ode = np.zeros(steps)
    Y = np.zeros((steps, 2))
    Y[0, :] = [N - 1, 1]  # [S_0, I_0]
    for T in range(steps - 1):
        ode_system = RK45(lambda t, y: SI_ode(t, y, [beta, gamma, N]), T_ode[T], Y[T, :], T_ode[T] + dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return T_ode, Y[:, 0] ,  Y[:, 1]


def sis_RK():
    T_ode = np.zeros(steps)
    Y = np.zeros((steps, 2))
    Y[0, :] = [N - 1, 1]  # [S_0, I_0]
    for T in range(steps - 1):
        ode_system = RK45(lambda t, y: SIS_ode(t, y, [beta, gamma, N]), T_ode[T], Y[T, :], T_ode[T] + dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return T_ode, Y[:, 0] ,  Y[:, 1]
def sirs_RK():
    T_ode = np.zeros(steps)
    Y = np.zeros((steps, 3))
    Y[0, :] = [N - 1, 1, 0]  # [S_0, I_0]
    for T in range(steps - 1):
        ode_system = RK45(lambda t, y: SIRS_ode(t, y, [beta, gamma, eta, N]), T_ode[T], Y[T, :], T_ode[T] + dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return T_ode, Y[:, 0], Y[:, 1], Y[:, 2]

def seirs_RK():
    T_ode = np.zeros(steps)
    Y = np.zeros((steps, 4))
    Y[0, :] = [N - 1, 1, 0, 0]  # [S_0, I_0]
    for T in range(steps - 1):
        ode_system = RK45(lambda t, y: SEIRS_ode(t, y, [beta, gamma, eta, sigma, N]), T_ode[T], Y[T, :], T_ode[T] + dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return T_ode, Y[:, 0], Y[:, 1], Y[:, 2], Y[:, 3]

def seir_RK():
    T_ode = np.zeros(steps)
    Y = np.zeros((steps, 4))
    Y[0, :] = [N - 1, 1, 0, 0]  # [S_0, I_0]
    for T in range(steps - 1):
        ode_system = RK45(lambda t, y: SEIR_ode(t, y, [beta, gamma, eta, sigma, N]), T_ode[T], Y[T, :], T_ode[T] + dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return T_ode, Y[:, 0], Y[:, 1], Y[:, 2], Y[:, 3]
def plot1(S,I,R,E, name, subplot, T_ode):
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


def plot2(S, I, R, E, name, subplot, T_ode):
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


def plot3(S, I, R, E, name, subplot, T_ode):
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


def drawplots(S, I, R, E, name, T):
    figure, axis = plt.subplots(1, 3)
    figure.suptitle(name)
    plot1(S, I, R, E, name, axis[0],T)
    plot2(S, I, R, E, name, axis[1], T)
    plot3(S, I, R, E, name, axis[2], T)
    plt.show()

blank = np.array([])
TSis, S1, I1 = sis_RK()

drawplots(S1,I1,blank,blank, "SIS", TSis)

Tsirs ,S2, I2, R2 = sirs_RK()

drawplots(S2, I2, R2,blank, "SIRS",Tsirs)

TSi, S3, I3 = si_RK()

drawplots(S3, I3, blank, blank, "SI",TSi)

TSEIR, S4, I4, R4, E4 =seir_RK()

drawplots(S4, I4, R4, E4, "SEIR", TSEIR)

TSEIRS, S5, I5, R5, E5 = seirs_RK()

drawplots(S5, I5, R5, E5, "SEIRS", TSEIRS)

