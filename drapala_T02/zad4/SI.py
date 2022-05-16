import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import RK45


def SI_Eurel(y0, beta, N, t, dt):
    S = [N - 1]
    I = [y0]
    steps = int(t / dt) - 1
    for i in range(steps):
        x = beta * I[-1] * S[-1] / N
        S.append(S[-1] - dt * x)
        I.append(I[-1] + dt * x)
    S = np.array(S)
    I = np.array(I)
    return S, I


def SI_DOPRI(t, y, params):
    beta, N = params
    S0, I0 = y
    S1 = -beta * I0 * S0 / N
    I1 = beta * I0 * S0 / N
    return [S1, I1]


def DOPRI(stepsDOP):
    T_ode = np.zeros(stepsDOP)
    Y = np.zeros((stepsDOP, 2))
    Y[0, :] = [N - 1, 1]
    for T in range(stepsDOP - 1):
        ode_system = RK45(lambda t, y: SI_DOPRI(t, y, [beta, N]), T_ode[T], Y[T, :], T_ode[T] + dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t
    return Y


def SI_plots(S, I, T_ode, S_DOP, I_DOP,sbplot):
    sbplot[0].plot(T_ode, S, label=r'$S_t$', color="royalblue")
    sbplot[0].plot(T_ode, I, label=r'$I_t$', color="darksalmon")
    sbplot[0].plot(T_ode, S_DOP, label=r'$S_t^{DOPRI}$', ls='--', color="midnightblue")
    sbplot[0].plot(T_ode, I_DOP, label=r'$I_t^{DOPRI}$', ls='--', color="firebrick")
    sbplot[0].set_xlabel('Czas')
    sbplot[0].set_ylabel('Liczba przypadków')
    sbplot[0].set_title(f'Wykres liniowy dla SI gdzie dt = {dt}')
    sbplot[0].legend()
    sbplot[0].grid()

    sbplot[1].plot(T_ode, S, label=r'$S_t$', color="royalblue")
    sbplot[1].plot(T_ode, I, label=r'$I_t$', color="darksalmon")
    sbplot[1].plot(T_ode, S_DOP, label=r'$S_t^{DOPRI}$', ls='--', color="midnightblue")
    sbplot[1].plot(T_ode, I_DOP, label=r'$I_t^{DOPRI}$', ls='--', color="firebrick")
    sbplot[1].set_yscale('log')
    sbplot[1].set_xlabel('Czas')
    sbplot[1].set_ylabel('Liczba przypadków')
    sbplot[1].set_title(f'Wykres semi-logarytmiczny dla SI gdzie dt = {dt}')
    sbplot[1].legend()
    sbplot[1].grid()


# parametry
beta = .5
N = 1000
T = 100
y = 1
dt = 1

for i in range(4):
    time = np.linspace(0, T, int(T / dt))
    S, I = SI_Eurel(y, beta, N, T, dt)
    stepsDOP = int(T / dt)
    Y = DOPRI(stepsDOP)
    S1 = Y[:, 0]
    I1 = Y[:, 1]
    figure, axis = plt.subplots(1, 2)
    SI_plots(S, I, time, S1, I1, axis)
    plt.show()
    dt = dt / 10
