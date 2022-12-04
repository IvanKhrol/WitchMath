import numpy as np
import matplotlib.pyplot as plt


def C(n, k):
    return np.math.factorial(n) / np.math.factorial(k) / np.math.factorial(n -k)

def derivative(f, n, x, dh):
    if n == 0:
        return f(0)
    der = 0
    for k in range(n + 1):
        der += C(n, k) * ((-1)**(k % 2)) * f(x + (n - 2 * k) * dh)
    der = der / ((2*dh)**n)
    return round(der, 3)

def macloren(f, n, t, dt):
    macl_sum = 0
    for k in range(n + 1):
        macl_sum += derivative(f, k, 0, dt) * t**k / np.math.factorial(k)
    return round(macl_sum, 3)

# Иницилизация переменных
n_start = 0; n_max = 8; dt = 0.001
x_plt = []; y_plt = []
range_x = np.arange(0, 1, dt)

# SIN

f = np.math.sin

for n in range(n_start, n_max): #Цикл по количеству членов суммы ряда Маклорена
    sum = 0; count = 0
    for t in range_x: #Цикл по значениям x от 0 до 1
        sum   += abs(macloren(f, n, t, dt) - f(t))
        count += 1
    x_plt.append(n)
    y_plt.append(sum/count)

# Построение графика    
plt.figure(1)
plt.grid(True)
plt.title("Sin(x)")
plt.xlabel("Количество членов суммы ряда Маклорена n, шт")
plt.ylabel("Среднее отклонение по норме модуля")
plt.plot(x_plt, y_plt)

# EXP

f = np.math.exp
x_plt = []; y_plt = []

for n in range(n_start , n_max): #Цикл по количеству членов суммы ряда Маклорена
    sum = 0; count = 0

    for t in range_x: #Цикл по значениям x от 0 до 1
        sum   += abs(macloren(f, n, t, dt) - f(t))
        count += 1
    x_plt.append(n)
    y_plt.append(sum/count)

# Построение графика   
plt.figure(2)
plt.grid(True)
plt.title("Exp(x)")
plt.xlabel("Количество членов суммы ряда Маклорена n, шт")
plt.ylabel("Среднее отклонение по норме модуля")
plt.plot(x_plt, y_plt)
plt.show()