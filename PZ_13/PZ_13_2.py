#  Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.

def finding_letters(n):
    yield from [i.upper() for i in n]

letters = input('Введите буквы в левом нижнем регистре:  ')
print(letters)
print(''.join([e for e in finding_letters(letters)]))