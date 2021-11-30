# Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
# этого элемента и его соседей.

import random
spisok = []
for i in range(int(input('Введите длину списка(N): '))):
    spisok.append(random.randint(1,50))

def recreateSpisok(spisok):
    newspisok = []
    for i in range(len(spisok)):
        if i == 0:
            newspisok.append((spisok[i]+spisok[i+1])/2)
        elif i == len(spisok)-1:
            newspisok.append((spisok[len(spisok)-1]+spisok[len(spisok)-2])/2)
        else:
            newspisok.append((spisok[i-1]+spisok[i]+spisok[i+1])/3)
    return newspisok
print('Список:' ,spisok)
print('Новый список:',recreateSpisok(spisok))