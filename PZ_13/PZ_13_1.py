# Вариант 8.
# В последовательности на n целых элементов найти количество пар, для которых
# произведение элементов делится на 3 (элементы пары в последовательности являются
# соседними).

#import random

#dlina = int(input('Введите длину списка: '))
#lst = [random.randint(-10, 10) for i in range(dlina)]


lst = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
def double(lst, n=2):
     lst.append(0) if len(lst)%2!=0 else ...
     return [lst[i:i + n] for i in range(0, len(lst), n)]
print(f'Начальный список: {lst} \nОтвет:{list(filter(lambda x: x[0]*x[1]%3==0 and x[0]*x[1]!=0, double(lst)))}')