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

# t_x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# x   = [1, 0.8, 0.5, 0.307, 0.2, 0.137, 0.1, 0.075, 0.06, 0.047, 0.039]

# t_y = [-0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# y   = [0.02, 0.079, 0.175, 0.303, 0.459, 0.638, 0.831, 1.03, 1.23, 1.42]

test_x = np.array([0.0, 1.0, 2.0, 3.0])
test_y = np.array([-2.0, -5.0, 0.0, -4.0])
f_coef = Newton_polynomial_coef(test_x, test_y)

P = []
P_x = np.arange(0, 3, 0.1)
for x in P_x:
    P.append(Newton_polynomial(x, f_coef, test_x))

plt.grid(True)
plt.title("График test")
plt.plot(test_x, test_y)
plt.plot(P_x, P, "red")
plt.show()

# plt.grid(True)
# plt.title("График x(t)")
# plt.plot(t_x, x)
# plt.show()

# plt.grid(True)
# plt.title("График y(t)")
# plt.plot(t_y, y)
# plt.show()