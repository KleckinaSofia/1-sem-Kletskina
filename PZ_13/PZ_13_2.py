def finding_letters(a):
    yield from [i.upper() for i in a]
letters=input('Введите буквенные символы, которые хотите преобразовать:  ')
print(''.join([e for e in finding_letters(letters)]))