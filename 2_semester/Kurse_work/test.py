import numpy as np
import matplotlib.pyplot as plt


delt = 0.2
FaceArea = 1
k = 1
dh = 1
imax = 3
jmax = 3
T = np.zeros((imax, jmax))

dx = 0;
Tb = 240;
Tb0 = 0;

for t in range(100):
    for i in range(imax):
        for j in range(jmax):
            Tc = T[i, j];
            dx = dh;

            Tw = 0
            Te = 0
            if (i == imax - 1):
                Ts = Tb
                dx = dh / 2
            else:
                Ts = T[i + 1, j]

            FluxS = (-k * FaceArea) / dx

            if (i == 0) :
                Tn = Tb0
                dx = dh / 2
            else:
                Tn = T[i - 1, j]
            FluxN = (-k * FaceArea) / dx

            if (j == jmax - 1):
                Te = Tb0
                dx = dh / 2
            else:
                Te = T[i, j + 1]
            FluxE = (-k * FaceArea) / dx

            if (j == 0):
                Tw = Tb0
                dx = dh / 2
            else:
                Tw = T[i, j - 1]
            FluxW = (-k * FaceArea) / dx

            FluxC = FluxE + FluxW + FluxN + FluxS

            T[i, j] = Tc + delt * (FluxC * Tc - (FluxE * Te + FluxW * Tw + FluxN * Tn + FluxS * Ts))
            # print(T)

# print(T)
Z = [[0 for i in range(imax)] for j in range(jmax)]
for i in range(imax-1, -1, -1):
    for j in range(jmax):
        Z[imax-i-1][j] = T[i][j]
plt.contourf (Z, cmap='Reds') 
plt.colorbar () 
plt.show()
