# Вариант 8
# Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A до B
# включительно.

A = input('Введите первое число (A < B): ')
B = input('Введите второе число (A < B): ')

while type(A) != float:
    try:
        A = float(A)
    except ValueError:
        print('Введено неверное число')
        A = input('Введите число : ')

while type(B) != float:
    try:
        B = float(B)
    except ValueError:
        print('Введено неверное число')
        B = input('Введите число : ')

    try:
        while A > B:
            print('Введено неверное число')
            A = input('Введите заново первое число (A < B): ')
            B = input('Введите заново ыторое число (A < B): ')
    except TypeError:
        continue
    S = 0
    while A <= B:
        print (A)
        A += 1
    S = S + A**2
    print('Сумма квадратов: ', S)