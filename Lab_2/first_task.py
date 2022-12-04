import numpy as np
import matplotlib.pyplot as plt

def Newton_polynomial(x_arr, y_arr):
    f = np.copy(y_arr)
    for j in range(1, x_arr.size):
        for i in range(x_arr.size - 1, j - 1, -1):
            f[i] = round((f[i] - f[i - 1])/(x_arr[j] - x_arr[0]), 3)
    return f

# t_x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# x   = [1, 0.8, 0.5, 0.307, 0.2, 0.137, 0.1, 0.075, 0.06, 0.047, 0.039]

# t_y = [-0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# y   = [0.02, 0.079, 0.175, 0.303, 0.459, 0.638, 0.831, 1.03, 1.23, 1.42]




test_x = np.array([0.0, 1.0, 2.0, 3.0])
test_y = np.array([-2.0, -5.0, 0.0, -4.0])
f_coef = Newton_polynomial(test_x, test_y)

P = lambda x: (f_coef[0] + f_coef[1]*(x - test_x[0]) + f_coef[2]*(x - test_x[0])*(x - test_x[1]) + f_coef[3]*(x - test_x[0])*(x - test_x[1])*(x - test_x[2]))
P_x = np.arange(0, 3, 0.1)


plt.grid(True)
plt.title("График test")
plt.plot(test_x, test_y)
plt.plot(P_x, P(P_x), "red")
plt.show()



















# plt.grid(True)
# plt.title("График x(t)")
# plt.plot(t_x, x)
# plt.show()

# plt.grid(True)
# plt.title("График y(t)")
# plt.plot(t_y, y)
# plt.show()