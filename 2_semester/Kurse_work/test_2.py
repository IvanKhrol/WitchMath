import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = np.sin(X*2+Y)*3 + np.cos(Y+5)
plt.contourf (X, Y, Z, cmap='Reds') 
plt.show()