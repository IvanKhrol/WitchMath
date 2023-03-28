import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from methods import *

numOfIter = 30000
beg_t, end_t = 0, 4
step = (end_t - beg_t)/numOfIter

m, L, vx_0 = 2, 4, 4


begin = np.array([0, L, vx_0, 0, m/L*(vx_0**2) + m*9.82])
var('x, y, vx, vy, T, t') 
g  =  9.81 + 0.01 * cos(2 * pi * t)
dg = -0.01 * sin(2* pi *t) * 2 * pi
dvx = -x/m/L*T
dvy = -y/m/L*T + g
dT = 2* m/L * (vx * dvx + vy*dvy) + m*dg*y/L + m*g*vy/L
f =  Array([vx, vy, dvx, dvy, dT])
func = lambdify((t, [x, y, vx, vy, T]), f, 'numpy')


fl = input()
if fl == "R":
    points = Runge_Kutta4(func, beg_t, begin, numOfIter, step)
elif fl == "A":
    beginAddams = Runge_Kutta4(func, beg_t, begin, 3, step)
    points = Addams4(func, beg_t, beginAddams, numOfIter, step)
else: 
    print("Wrong input")
    exit(-1)

plt.plot([item[0] for item in points], [-item[1] for item in points])
plt.xlabel('x')
plt.ylabel('y')
plt.show()