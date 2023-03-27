import numpy as np
import matplotlib.pyplot as plt

def Newton_polynomial_coef(x_arr, y_arr):
    f = np.copy(y_arr)
    for j in range(1, x_arr.size):
        for i in range(x_arr.size - 1, j - 1, -1):
            f[i] = round((f[i] - f[i - 1])/(x_arr[j] - x_arr[0]), 3)
    return f

def Newton_polynomial(x, f, x_arr):
    y = f[0]
    tmp = 1
    for i in range(1, f.size):
        tmp *= (x - x_arr[i - 1])
        y += f[i]*tmp
    return y

def draw_plt(plt_num, plt_title, x_arr, y_arr, plt_color = "blue"):
    plt.figure(plt_num)
    plt.grid(True)
    plt.title(plt_title)
    plt.plot(x_arr, y_arr, plt_color)

t_x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
x   = np.array([1, 0.8, 0.5, 0.307, 0.2, 0.137, 0.1, 0.075, 0.06, 0.047, 0.039])

f_coef_x = Newton_polynomial_coef(t_x, x)
P_x = []
P_t = np.arange(0, 1, 0.01)
for t in P_t:
    P_x.append(Newton_polynomial(t, f_coef_x, t_x))

draw_plt(1, "График x(t)", t_x, x)
draw_plt(1, "График P(t)", P_t, P_x, "red")


t_y = np.array([-0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
y   = np.array([0.02, 0.079, 0.175, 0.303, 0.459, 0.638, 0.831, 1.03, 1.23, 1.42])

f_coef_y = Newton_polynomial_coef(t_y, y)
M_y = []
M_t = np.arange(-0.8, 1, 0.01)
for t in M_t:
    M_y.append(Newton_polynomial(t, f_coef_y, t_y))

draw_plt(2, "График y(t)", t_y, y)
draw_plt(2, "График M(t)", M_t, M_y, "red")

y_x = []
for t in P_x:
    y_x.append(Newton_polynomial(t, f_coef_y, t_y))
draw_plt(3, "График y(x)", P_x, y_x)

plt.show()