#  Дан список размера N. Найти количество участков, на которых его элементы
# монотонно возрастают.

import random
spisok = []
for i in range(int(input('Введите длину списка(N):  '))):
    spisok.append(random.randint(1,50))

print('Список:  ', spisok)
k=0
m=0
for i in range(len(spisok)-1):
    if spisok[i+1]>spisok[i]:
        m=m+1
    else:
        if m>0:
            k=k+1
            m=0
if m>0:
    k=k+1
print('Количество', k)