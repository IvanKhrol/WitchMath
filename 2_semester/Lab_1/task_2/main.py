import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from methods import *

numOfIter = 30000
beg_t, end_t = 0, 16
step = (end_t - beg_t)/numOfIter

m = 0.01227747
M = 1 - m
f_0 = 0 

begin = np.array([0.994, 0, 0, -2.031732629557337])
var('x, y, vx, vy, t') 
r_1 = ((x + m)**2 + y**2)**(1/2)
r_2 = ((x - M)**2 + y**2)**(1/2)
dvx = 2*vy + x - M*(x+m)/r_1**3 - m * (x - M)/r_2**3 - f_0 * vx
dvy = -2*vx + y - M * y/r_1**3 - m * y/r_2**3 - f_0 * vy
f =  Array([vx, vy, dvx, dvy])
func = lambdify((t, [x, y, vx, vy]), f, 'numpy')

fl = input()
if fl == "4":
    points = Runge_Kutta4(func, 0, begin, numOfIter, step)
elif fl == "2":
    points = Runge_Kutta2(func, 0, begin, numOfIter, step)
else: 
    print("Wrong input")
    exit(-1)

plt.plot([item[0] for item in points], [item[1] for item in points])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()