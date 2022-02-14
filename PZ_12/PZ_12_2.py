# Вариант №8

from tkinter import *


def avg_min_temp(vhod):
    b = {n.get().split(' ')[0]: [int(i) for i in n.get().split(' ')[1:6]]}
    d = {n.get().split(' ')[6]: [int(i) for i in n.get().split(' ')[7:]]}
    print(b, d)
    c['text'] = 'Средняя продажи апельсинов', sum(b['апельсины']) / len(b['апельсины'])
    g['text'] = 'Средняя продажи яблок', sum(d['яблоки']) / len(d['яблоки'])


root = Tk()
root.title('Расчёт синоптики')
root.geometry("550x120")
Label(text='Введите все входные данные').grid(row=1, column=0)
n = Entry(width=45, font='arial 10')
n.place(x=200, y=1)
button1 = Button(text="Рассчитать")
button1.place(x=320, y=25)
c = Label(width=45, font='arial 15')
c.place(x=35, y=50)
g = Label(width=45, font='arial 15')
g.place(x=35, y=80)
button1.bind('<Button-1>', avg_min_temp)
root.mainloop()
