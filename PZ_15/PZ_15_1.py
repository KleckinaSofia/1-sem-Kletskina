# Вариант 8.
# 1. В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.

from random import randint
m, n, y, z, r = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ", 'Столбец = ')]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print("Исходная матрциа:")
for i in matrix:
    print(*i)
for i in range(m):
    matrix[i][r-1] = matrix[i][r-1] ** 2
print('Полученная матрица:')
for i in matrix:
    print(*i)
