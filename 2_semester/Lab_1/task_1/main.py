
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from methods import *

step = 0.001
numOfIter = 10000

m, L, vx_0 = 2, 4, 4


begin = np.array([0, L, vx_0, 0, m/L*(vx_0**2) + m*9.82])
var('x, y, vx, vy, T, t') 
g  =  9.81 + 0.01 * cos(2 * pi * t)
g_t = -0.01 * sin(2* pi *t) * 2 * pi
vx_t = -x/m/L*T
vy_t = -y/m/L*T + g
T_t = 2* m/L * (vx * vx_t + vy*vy_t) + m*g_t*y/L + m*g*vy/L
f =  Array([vx, vy, vx_t, vy_t, T_t])
func = lambdify((t,[x,y,vx,vy, T]), f, 'numpy')


fl = input()
if fl == "R":
    points = Runge_Kutta4(func, 0, begin, numOfIter, step)
elif fl == "A":
    beginAddams = Runge_Kutta4(func, 0, begin, 3, step)
    points = Addams4(func, 0, beginAddams, numOfIter, step)
else: 
    print("Wrong input")
    exit(-1)

plt.plot([item[0] for item in points], [-item[1] for item in points])
plt.xlabel('x')
plt.ylabel('y')
plt.show()