import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import RK45


def SIRS_Eurel(y0, beta, gamma, eta, N, t, dt):
    S = [N - 1]
    I = [y0]
    R = [0]
    steps = int(t / dt) - 1
    for i in range(steps):
        x = beta * I[-1] * S[-1] / N
        S.append(S[-1] - dt * x + dt * (eta * R[-1]))
        I.append(I[-1] + dt * x - dt * (gamma * I[-1]))
        R.append(R[-1] + dt * (gamma * I[-1] - eta * R[-1]))
    S = np.array(S)
    I = np.array(I)
    R = np.array(R)
    return S, I, R


def SIRS_DOPRI(t, y, params):
    beta, gamma, eta, N = params
    S0, I0, R0 = y
    S1 = -beta * I0 * S0 / N + eta * R0
    I1 = beta * I0 * S0 / N - gamma * I0
    R1 = gamma * I0 - eta * R0
    return [S1, I1, R1]


def DOPRI(stepsDOP):
    T_ode = np.zeros(stepsDOP)
    Y = np.zeros((stepsDOP, 3))
    Y[0, :] = [N - 1, 1, 0]
    for T in range(stepsDOP - 1):
        ode_system = RK45(lambda t, y: SIRS_DOPRI(t, y, [beta, gamma, eta, N]), T_ode[T], Y[T, :], T_ode[T] + dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t
    return Y


def SIRS_plots(S, I, R, T_ode, S_DOP, I_DOP, R_DOP, subplot):
    subplot[0].plot(T_ode, S, label=r'$S_t$', color="royalblue")
    subplot[0].plot(T_ode, I, label=r'$I_t$', color="darksalmon")
    subplot[0].plot(T_ode, R, label=r'$R_t$', color="yellowgreen")
    subplot[0].plot(T_ode, S_DOP, label=r'$S_t^{DOPRI}$', ls='--', color="midnightblue")
    subplot[0].plot(T_ode, I_DOP, label=r'$I_t^{DOPRI}$', ls='--', color="firebrick")
    subplot[0].plot(T_ode, R_DOP, label=r'$I_t^{DOPRI}$', ls='--', color="forestgreen")
    subplot[0].set_xlabel('Czas')
    subplot[0].set_ylabel('Liczba przypadków')
    subplot[0].set_title(f'Wykres liniowy dla SIRS gdzie dt = {dt}')
    subplot[0].legend()
    subplot[0].grid()

    subplot[1].plot(T_ode, S, label=r'$S_t$', color="royalblue")
    subplot[1].plot(T_ode, I, label=r'$I_t$', color="darksalmon")
    subplot[1].plot(T_ode, R, label=r'$R_t$', color="yellowgreen")
    subplot[1].plot(T_ode, S_DOP, label=r'$S_t^{DOPRI}$', ls='--', color="midnightblue")
    subplot[1].plot(T_ode, I_DOP, label=r'$I_t^{DOPRI}$', ls='--', color="firebrick")
    subplot[1].plot(T_ode, R_DOP, label=r'$I_t^{DOPRI}$', ls='--', color="forestgreen")
    subplot[1].set_yscale('log')
    subplot[1].set_xlabel('Czas')
    subplot[1].set_ylabel('Liczba przypadków')
    subplot[0].set_title(f'Wykres semilogarytmiczny dla SIRS gdzie dt = {dt}')

    subplot[1].legend()
    subplot[1].grid()


# parametry
beta = .5
gamma = .1
eta = .1
N = 1000
T = 100
y = 1
dt = 1

for i in range(4):
    Time = np.linspace(0, T, int(T / dt))
    S, I, R = SIRS_Eurel(y, beta, gamma, eta, N, T, dt)
    stepsDOP = int(T / dt)
    Y = DOPRI(stepsDOP)
    S2 = Y[:, 0]
    I2 = Y[:, 1]
    R2 = Y[:, 2]
    figure, axis = plt.subplots(1, 2)
    SIRS_plots(S, I, R, Time, S2, I2, R2, axis)
    plt.show()
    dt = dt / 10
