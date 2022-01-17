# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# 1.Исходные данные:
# 2.Количество элементов:
# 3.Индекс последнего минимального элемента:
# 4.Сумма элементов больших 10 во второй половине:

from random import randint

file_data = []     # генерация содрежимого исходного файла
count = 0
while count < 15:
    file_data.append(str(randint(-10, 100)))
    count += 1


print(",".join(file_data), file=open('file_10_1.txt', 'w'))     # запись содержимого в исходный файл

new_file = open('file_new10_1.txt', 'w')     # новый .txt файл
print('Исходные данные:', open('file_10_1.txt').read(), file=new_file)    # 1
print('Количество элементов:', len(open('file_10_1.txt').read().split(',')), file=new_file)    # 2


new_file_data = list(map(int, open('file_10_1.txt').read().split(',')))  # получение списка из файла с исходными данными
reverse = new_file_data[::-1]
print('Индекс последнего минимального элемента:', 14 - reverse.index(min(reverse)), file=new_file) #3

half = new_file_data[int(round(len(new_file_data))/2):]    # срез половины списка
summa = 0
for element in half:
    if element > 10:
        summa += element
print('Сумма элементов больших 10 во второй половине:', sum(half), file=new_file)    #4

new_file.close()