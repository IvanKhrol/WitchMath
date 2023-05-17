import numpy as np
import matplotlib.pyplot as plt

def u_0x(x):
    if x >= 1 and x <= 3:
        return 1
    else:
        return 0

def u_t0(t):
    return 0

def out_print(title, u, K, x):
    fig = plt.figure(figsize = (9, 6))
    plt.rc('font', **{'size' : 14})
    fig.suptitle(title)
    for k in range(0, K + 1, 100) :
        plt.subplot(int(np.sqrt(K/100)) + 1, int(np.sqrt(K/100)) + 1, int(k/100) + 1)
        plt.title("k = " + str(k))
        plt.xticks(np.linspace(0, 10, 6))
        plt.xlabel('$x$')
        plt.yticks(np.linspace(0, 2, 6))
        plt.ylabel('$u$')
        plt.grid()
        plt.plot(x, u[k, :], color='r', ls='-', lw=2)
    fig.tight_layout()
    plt.show()


#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

scheme = input("Enter schema type:\nL -> Lux scheme\nL-W -> Lux-Wendorf scheme\nLC -> left corner scheme\nRC -> right corner scheme\n")

# Init
K = 400
T = 8
tau = T / K
N = 400
X = 10
h = X / N
print(tau, h)
t = np.linspace(0, T, K + 1)
x = np.linspace(0, X, N + 1)

u = np.zeros((K + 1, N + 1))
for n in range(N + 1):
    u[0, n] = u_0x(x[n])
for k in range(K + 1):
    u[k, 0] = u_t0(t[k])

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

if(scheme == "L"):# Lux scheme
    for k in range(K):
        for n in range(1, N):
            u[k + 1, n] = 0.5 * (u[k, n + 1] + u[k, n - 1] - 0.5 * tau * (u[k, n + 1]**2 - u[k, n - 1]**2) / h)
    out_print("Схема Лакса", u, K, x)
    
elif(scheme == "L-W"): # Lux-Wendorf scheme 
    for k in range(K):
        for n in range(1, N):
            u_left = 0.5 * (u[k, n] + u[k, n - 1] - 0.5 * tau * (u[k, n]**2 - u[k, n - 1]**2) / h)
            u_right = 0.5 * (u[k, n + 1] + u[k, n] - 0.5 * tau * (u[k, n + 1]**2 - u[k, n]**2) / h)
            u[k + 1, n] = u[k, n] - 0.5 * tau * (u_right**2 - u_left**2) / h
    out_print("Схема Лакса-Вендроффа", u, K, x)

elif(scheme == "LC"): # Left corner scheme
    for k in range(K):
        for n in range(1, N + 1):
            u[k + 1, n] = u[k, n] - 0.5 * tau * (u[k, n]**2 - u[k, n - 1]**2) / h
    out_print("Явный левый уголок", u, K, x)

elif(scheme == "RC"): # Right corner scheme
    for k in range(K):
        for n in range(1, N):
            u[k + 1, n] = u[k, n] - 0.5 * tau * (u[k, n + 1]**2 - u[k, n]**2) / h
    out_print("Явный правый уголок", u, K, x)

else:
    print("Unknown scheme\nExit!")

    