# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое, количество символов, принадлежащих к
# группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста

import string

text = open('text18-8.txt', encoding="utf8").read()    # чтение текста из файла и трансляция его в консоль
print(text)

for p in string.punctuation + '\n':    # удаление пунктуации для последующего подсчета букв
    if p in text:
        text = text.replace(p, '')

keys = list(set(text.lower().replace(" ", "")))    # список букв для подсчета их повторов
count = dict()
for i in keys:    # в словарь заносятся ключи - буквы и значения - количество повторов ключа-буквы в тексте
    count[i] = text.count(i)
print('Количество символов, принадлежащих к группе букв', count)

# новый файл с удаленной буквой "с"
new_file = open('new_10_2.txt', 'w', encoding="utf8")
print(open('text18-8.txt', encoding="utf8").read().lower().replace('с', ""), file=new_file)