#Даны два целых числа: A, B. Проверить истинность высказывания:
#«Каждое из чисел A и B нечетное».
a = int(input("введите число A: "))
b = int(input("введите число B: "))
while type(a) != int:
    try:
        a= int(a)
    except ValueError:
        print('Вы ввели нецельное число А')
        a = input('Введите число А: ')
else:
    pass
while type(b) != int:
     try:
         b = int(b)
     except ValueError:
         print('Вы ввели нецельное число В')
         b = input('Введите число В: ')
else:
    pass
t = (a % 2 == 1) and (b % 2 == 1)
if t == True:
     print('Данное высказывание истинно')
else:
    print('данное высказываение ложно')