import numpy as np
import matplotlib.pyplot as plt

k_0 = 1
q_0 = 1

T_bot = 1

def phi_1(t):
    return T_bot

def phi_2(t):
    return T_bot

def u_init(x):
    return 19 * np.exp(-10 * (x - 50)**2) + T_bot

def out_print(title, u, K, x):
    fig = plt.figure(figsize = (9, 6))
    plt.rc('font', **{'size' : 14})
    fig.suptitle(title)
    for k in range(0, K + 1, 100) :
        plt.subplot(2, 2, int(k/100) + 1)
        plt.title("k = " + str(k))
        plt.xlabel('$x$')
        plt.ylabel('$T$')
        plt.grid()
        plt.plot(x, u[k, :], color='r', ls='-', lw=2)
    fig.tight_layout()
    plt.show()

fl = int(input())
K = 200
N = 800
T = 0.5
X = 100
tau = T / K
h = X / N
# print(tau, h)

t = np.linspace(0, T, K + 1)
x = np.linspace(0, X, N + 1)

T = np.zeros((K + 1, N + 1))
for n in range(N + 1):
    T[0, n] = u_init(x[n])
for k in range(K + 1):
    T[k, 0] = phi_1(t[k])
    T[k, -1] = phi_2(t[k])


if(fl == 1): # For alpha + 1 > betta  
    alpha = 2
    beta = 2

    for k in range(K):
        A = np.zeros(N + 1)
        B = np.zeros(N + 1)
        C = np.zeros(N + 1)
        D = np.zeros(N + 1)
        P = np.zeros(N + 1)
        Q = np.zeros(N + 1)
        for n in range(N + 1):
            if n == 0 or n == N:
                B[n] = 1
                D[n] = T[k + 1, n]
            else:
                A[n] = -k_0 * tau * (0.5 * (T[k, n] + T[k, n - 1]))**alpha
                C[n] = -k_0 * tau * (0.5 * (T[k, n + 1] + T[k, n]))**alpha
                B[n] = h**2 - A[n] - C[n]
                D[n] = h**2 * (q_0 * tau * T[k, n]**beta + T[k, n])
        P[1] = 0
        Q[1] = D[0]
        for n in range(N):
            P[n + 1] = -C[n] / (A[n] * P[n] + B[n])
            Q[n + 1] = (D[n] - A[n] * Q[n]) / (A[n] * P[n] + B[n])
        T[k + 1, N] = (D[N] - A[N] * Q[N]) / (A[N] * P[N] + B[N])
        for n in range(N - 1, 0, -1):
            T[k + 1, n] = T[k + 1, n + 1] * P[n + 1] + Q[n + 1]

    out_print("$\\alpha + 1 > \\beta$", T, K, x)

elif(fl == 2): # For alpha + 1 = betta

    alpha = 1
    beta = 2
    tau = 0.001


    for k in range(K):
        A = np.zeros(N + 1)
        B = np.zeros(N + 1)
        C = np.zeros(N + 1)
        D = np.zeros(N + 1)
        P = np.zeros(N + 1)
        Q = np.zeros(N + 1)
        for n in range(N + 1):
            if n == 0 or n == N:
                B[n] = 1
                D[n] = T[k + 1, n]
            else:
                A[n] = -k_0 * tau * (0.5 * (T[k, n] + T[k, n - 1]))**alpha
                C[n] = -k_0 * tau * (0.5 * (T[k, n + 1] + T[k, n]))**alpha
                B[n] = h**2 - A[n] - C[n]
                D[n] = h**2 * (q_0 * tau * T[k, n]**beta + T[k, n])
        P[1] = 0
        Q[1] = D[0]
        for n in range(N):
            P[n + 1] = -C[n] / (A[n] * P[n] + B[n])
            Q[n + 1] = (D[n] - A[n] * Q[n]) / (A[n] * P[n] + B[n])
        T[k + 1, N] = (D[N] - A[N] * Q[N]) / (A[N] * P[N] + B[N])
        for n in range(N - 1, 0, -1):
            T[k + 1, n] = T[k + 1, n + 1] * P[n + 1] + Q[n + 1]

    out_print("$\\alpha + 1 = \\beta$", T, K, x)

elif(fl == 3): # For alpha + 1 < beta

    alpha = 1
    beta = 3
    tau = 0.0001
    h = 0.01

    for k in range(K):
        A = np.zeros(N + 1)
        B = np.zeros(N + 1)
        C = np.zeros(N + 1)
        D = np.zeros(N + 1)
        P = np.zeros(N + 1)
        Q = np.zeros(N + 1)
        for n in range(N + 1):
            if n == 0 or n == N:
                B[n] = 1
                D[n] = T[k + 1, n]
            else:
                A[n] = -k_0 * tau * (0.5 * (T[k, n] + T[k, n - 1]))**alpha
                C[n] = -k_0 * tau * (0.5 * (T[k, n + 1] + T[k, n]))**alpha
                B[n] = h**2 - A[n] - C[n]
                D[n] = h**2 * (q_0 * tau * T[k, n]**beta + T[k, n])
        P[1] = 0
        Q[1] = D[0]
        for n in range(N):
            P[n + 1] = -C[n] / (A[n] * P[n] + B[n])
            Q[n + 1] = (D[n] - A[n] * Q[n]) / (A[n] * P[n] + B[n])
        T[k + 1, N] = (D[N] - A[N] * Q[N]) / (A[N] * P[N] + B[N])
        for n in range(N - 1, 0, -1):
            T[k + 1, n] = T[k + 1, n + 1] * P[n + 1] + Q[n + 1]

    out_print("$\\alpha + 1 < \\beta$", T, K, x)
else:
    print("Unknown fl")