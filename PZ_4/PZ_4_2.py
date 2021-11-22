# Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада увеличивается
# на P процентов от имеющейся суммы (P — вещественное число, 0 < P < 25). По данному P
# определить, через сколько месяцев размер вклада превысит 1100 руб., и вывести найденное
# количество месяцев K (целое число) и итоговый размер вклада S (вещественное число).
while True:
    # Проверка на тип данных переменной P
    try:
        P =int(input('P ='))
        if 0 < P < 25:  # Проверка на натуральность переменной и соответсвии условию
            break  # Прерывание цикла
        else:
            print('Неверные данные:/')

    except ValueError:
        print('Неправильно ввели:/')
K = 0
S = 1000
while S < 1100:
    K +=1
    S += S * (P/100)
print('Через', K, 'месяцев')
print('Итоговый размер вклада=', S)