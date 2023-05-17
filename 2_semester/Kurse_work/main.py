import numpy as np
import matplotlib.pyplot as plt


def S(W_0, t): # Source power function
    if(t == 0): return W_0
    return (W_0*np.sin(t)/t)



#====================================================================================================================================
#                                       						 Init							
#====================================================================================================================================

input_str = input("Enter initial data: W0, Lx, Ly, lambda, N_x, Ny: ")
if(len(input_str) > 0):
    W_0, L_x, L_y, lambda__, N_x, Ny = list(map(int, input_str.split(" "))) # User data
else:
    W_0, L_x, L_y, lambda__, N_x, N_y = 1, 100, 100, 10, 300, 300

# end_time = 10
# end_time = 200
end_time = 1e3

Hx = L_x/N_x
Hy = L_y/N_y
dt = (Hx * Hy)/(Hx + Hy)/lambda__ # Courant criterion
# dt = end_time/N_t
print(dt)
delta_x = Hx
delta_y = Hy
T = np.zeros((N_x, N_y))

Tb = 240;
Tb0 = 0;


#====================================================================================================================================
#                                       						Main code							
#====================================================================================================================================


for t in range(int(end_time)):
    for i in range(N_y):
        for j in range(N_x):
            Tc = T[i, j]
            delta_x = Hx

            Tw = 0
            Te = 0
            if (i == N_y - 1):
                Ts = Tb0
                delta_y = Hy / 2
            else:
                Ts = T[i + 1, j]

            FluxS = (-lambda__ * Hx) / delta_y

            if (i == 0) :
                Tn = Tb0
                delta_y = Hy / 2
            else:
                Tn = T[i - 1, j]
            FluxN = (-lambda__ * Hx) / delta_y

            if (j == N_x - 1):
                Te = Tb0
                delta_x = Hx / 2
            else:
                Te = T[i, j + 1]
            FluxE = (-lambda__ * Hy) / delta_x

            if (j == 0):
                Tw = S(W_0, t)
                delta_x = Hx / 2
            else:
                Tw = T[i, j - 1]
            FluxW = (-lambda__ * Hy) / delta_x

            FluxC = FluxE + FluxW + FluxN + FluxS

            T[i, j] = Tc + dt * (FluxC * Tc - (FluxE * Te + FluxW * Tw + FluxN * Tn + FluxS * Ts))



Z = [[0 for i in range(N_y)] for j in range(N_x)]
for i in range(N_y-1, -1, -1):
    for j in range(N_x):
        Z[N_y-i-1][j] = T[i][j]
plt.xlim([0, 60])
# plt.ylim([0, 60])
plt.contourf (Z, cmap='Reds') 
plt.colorbar () 
plt.show()

