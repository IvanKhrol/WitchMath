import numpy as np
from mpl_toolkits import mplot3d
import math
import matplotlib.pyplot as plt

# Функции задающие начальное уравнение 
def get_left_matrix(n, a):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if(i == j):
                matrix[i][j] = 2
            elif(i + 1 == j ):
                matrix[i][j] = - 1 - a
            elif(i - 1 == j ):
                matrix[i][j] = - 1 + a
    return matrix

def get_right_vector(n, a):
    vector = np.zeros(n)
    vector[0] = 1 - a
    if(n == 1):
        return vector
    vector[n - 1] = 1 + a
    return vector

def get_answer_vector(n, a):
    if(n == 1):
        vector = np.array([(1 - a) / 2])
        return vector
    vector = np.ones(n)
    return vector

def get_zeidel_param(matrix, vector):
    C = np.zeros(matrix.shape)
    d = np.zeros(vector.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if(i == j):
                C[i][j] = 0
            else:
                C[i][j] = -matrix[i][j] / matrix[i][i]
        d[i] = vector[i] / matrix[i][i]
    return (C, d)

def zeidel(C, d, res_k):
    res = d.copy()
    for i in range(d.shape[0]):
        j = 0
        while(i != 0 and j <= i -1):
            res[i] += C[i][j] * res[j]
            j += 1
        while(j < d.shape[0]):
            res[i] += C[i][j] * res_k[j]
            j += 1
    return res

def norm(vector):
    res = 0
    for v in vector:
        res += v**2 
    return np.sqrt(res)


# Иницилизация переменных
d_alfa = 0.01
dx = 0.1 
alfa_arr = np.arange(0, 1 + d_alfa, d_alfa)
n_max = 10
itter_max = 100000
n_array = np.zeros(0)
a_array = np.zeros(0)
k_array = np.zeros(0)



for n in range(1, n_max + 1):
    for alfa in alfa_arr:
        # alfa = 0.5
        A = get_left_matrix (n, alfa)
        f = get_right_vector(n, alfa)
        ans = get_answer_vector(n, alfa)

        # Итерации методом Зейделя
        itter_count = 1
        cor = get_zeidel_param(A, f)
        C = cor[0]
        d = cor[1]
        # print(C)
        itter_ans = np.zeros(d.shape)
        delta = norm(ans - itter_ans)
        while(delta > dx):
            if(itter_count == itter_max): break
            itter_ans = zeidel(C, d, itter_ans)
            # print(itter_ans)
            delta = norm(ans - itter_ans)
            # print(delta)
            itter_count += 1

        # print(itter_count)
        # Массивы для графика    
        if(itter_count < itter_max):
            n_array = np.append(n_array, n)
            a_array = np.append(a_array, alfa)
            k_array = np.append(k_array, itter_count)

# Построение графика
n_array = np.flip(n_array)
a_array = np.flip(a_array)
k_array = np.flip(k_array)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(n_array, a_array, k_array, 'red')
ax.view_init(30, 240)
plt.show()
