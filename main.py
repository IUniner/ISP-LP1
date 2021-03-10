import numpy as np

# Матрица (левая часть системы)
M6 = np.matrix([[1., 1., 1.], [1., -1., 1], [2, 1, 0]])
# Вектор (правая часть системы)
v6 = np.matrix([1., 1., 1.])
v6 = v6.T
X = np.linalg.solve(M6, v6)
print(X)
