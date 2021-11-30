# Вариант 8
# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
# четные числа в порядке убывания их индексов, а также их количество K.

import random
spisok = []
for i in range(10):
    spisok.append(random.randint(1,10))

spisok.sort(reverse=True)

k=0
for i in range(10):
    if spisok[i] % 2 == 0:
        print(spisok[i])
        k=k+1
print('Всего таких чисел ', k)