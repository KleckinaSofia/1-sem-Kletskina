# Вариант 8.
# 2. В матрице элементы последней строки заменить на 0.

from random import randint
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print("Исходная матрциа:")
for i in matrix:
    print(*i)
for i in range(n):
    matrix[-1][i] = 0
print('Полученная матрица:')
for i in matrix:
    print(*i)
