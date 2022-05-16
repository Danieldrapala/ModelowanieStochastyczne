import numpy as np
from matplotlib import pyplot as plt


def SIR_g(y0, beta, gamma, N, t):
    S = N - 1
    I = y0
    R = 0
    sus = []
    inf = []
    rec = []
    t_ = 0
    limit = []
    while t_ < t:
        x = (beta * I * S / N)
        S, I, R = S - x, I + x - gamma * I, R + gamma * I
        sus.append(S)
        inf.append(I)
        rec.append(R)
        if R >= N - 1:
            limit.append(t_)
        t_ += 1
    if not limit:
        limit.append(t_)
    return sus, inf, rec, limit[0]


def plot(S, I, R, T, title, limit,subplot):

    subplot[0].plot(T, I, label=r'$I_t$')
    subplot[0].plot(T, S, label=r'$S_t$')
    subplot[0].plot(T, R, label=r'$R_t$')
    subplot[0].set_xlabel('Czas')
    subplot[0].set_xlim(0, limit)
    subplot[0].set_ylabel('Liczba przypadków')
    subplot[0].set_title('Wykres liniowy dla SI ' + title)
    subplot[0].legend()

    subplot[0].grid()

    subplot[1].plot(T, I, label=r'$I_t$')
    subplot[1].plot(T, S, label=r'$S_t$')
    subplot[1].plot(T, R, label=r'$R_t$')
    subplot[1].set_yscale('log')
    subplot[1].set_xlabel('Czas')
    subplot[1].set_xlim(0, limit)
    subplot[1].set_ylabel('Liczba przypadków')
    subplot[1].set_title('Wykres log dla SI ' + title)
    subplot[1].legend()
    subplot[1].grid()


I0 = 1
beta = .5
N = 1000
T = 500
dt = 1
gamma_arr = [.07, .035, .05, .025]
dict_I = []
dict_S = []
dict_R = []
dict_T = []
limit_arr = []
for gamma in gamma_arr:
    T_lin = np.linspace(0, T, T)
    t = T_lin.size
    S, I, R, limit = SIR_g(y0=1, beta=beta, gamma=gamma, N=N, t=t)
    dict_R.append({'R': R})
    dict_I.append({'I': I})
    dict_S.append({'S': S})
    dict_T.append({'T': T_lin})
    limit_arr.append(limit)
    title_SI_1 = f' $\\gamma = ' + f'{gamma}$'
    figure, axis = plt.subplots(1, 2)
    figure.suptitle(title_SI_1)
    plot(S, I, R, T_lin, title_SI_1, limit, axis)
    plt.show()

plt.plot(dict_T[0].get('T'), dict_I[0].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[0]}')
plt.plot(dict_T[1].get('T'), dict_I[1].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[1]}')
plt.plot(dict_T[2].get('T'), dict_I[2].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[2]}')
plt.plot(dict_T[3].get('T'), dict_I[3].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[3]}')
plt.plot(dict_T[0].get('T'), dict_S[0].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[0]}')
plt.plot(dict_T[1].get('T'), dict_S[1].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[1]}')
plt.plot(dict_T[2].get('T'), dict_S[2].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[2]}')
plt.plot(dict_T[3].get('T'), dict_S[3].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[3]}')
plt.plot(dict_T[0].get('T'), dict_R[0].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[0]}')
plt.plot(dict_T[1].get('T'), dict_R[1].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[1]}')
plt.plot(dict_T[2].get('T'), dict_R[2].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[2]}')
plt.plot(dict_T[3].get('T'), dict_R[3].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[3]}')
plt.xlabel('Czas')
plt.xlim(0, max(limit_arr))
plt.ylabel('Liczba przypadków')
plt.title('Wykres liniowy dla SIR')
plt.legend()
plt.show()

plt.plot(dict_T[0].get('T'), dict_I[0].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[0]}')
plt.plot(dict_T[1].get('T'), dict_I[1].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[1]}')
plt.plot(dict_T[2].get('T'), dict_I[2].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[2]}')
plt.plot(dict_T[3].get('T'), dict_I[3].get('I'), label=r'$I_t$ G = 'f'{gamma_arr[3]}')
plt.plot(dict_T[0].get('T'), dict_S[0].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[0]}')
plt.plot(dict_T[1].get('T'), dict_S[1].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[1]}')
plt.plot(dict_T[2].get('T'), dict_S[2].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[2]}')
plt.plot(dict_T[3].get('T'), dict_S[3].get('S'), label=r'$S_t$ G = 'f'{gamma_arr[3]}')
plt.plot(dict_T[0].get('T'), dict_R[0].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[0]}')
plt.plot(dict_T[1].get('T'), dict_R[1].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[1]}')
plt.plot(dict_T[2].get('T'), dict_R[2].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[2]}')
plt.plot(dict_T[3].get('T'), dict_R[3].get('R'), label=r'$R_t$ G = 'f'{gamma_arr[3]}')
plt.xlabel('Czas')
plt.xlim(0, max(limit_arr))
plt.yscale('log')
plt.xlabel('Czas')
plt.ylabel('Liczba przypadków')
plt.title('Wykres log dla SIR')
plt.legend()
plt.show()

