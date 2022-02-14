 # Вариант 8
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Combobox
root = Tk()
var=IntVar()
var1=IntVar()

root['bg']= '#fafafa'
root.title("Sing up")
root.geometry('559x665')
root.iconbitmap('перо.ico')
root['bg'] = 'black'
root.resizable(width=False, height=False)

Canvas(root, bg='orange', height=30, width=665).place(x=0,y=0)

Label(text= "First Name", width=14, fg='yellow', bg='black', font='arial 10').place(x=17, y=55)
Entry(textvariable=StringVar(value="Enter First Name"), width=30, fg='gray', font='arial 18').place(x=130,y=50)

Label(text="Last Name", width=14,fg='yellow', bg='black',font='arial 10').place(x=17,y=95)
Entry(textvariable=StringVar(value="Enter Last Name"), width=30, fg='gray', font='arial 18').place(x=130,y=90)

Label(text="Screen Name",width=14,fg='yellow', bg='black',font='arial 10').place(x=17,y=135)
Entry(textvariable=StringVar(value="Enter Screen Name"),width=30, fg='gray', font='arial 18').place(x=130,y=130)

Label(text= "Date of Birth", width=14, fg='yellow', bg='black', font='arial 10').place(x=17, y=195)
combo=Combobox(root)
combo['values']=('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентрябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
combo.current(0)
combo.place(x=130,y=195)

combo_1=Combobox(root, width='5')
combo_1['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
combo_1.current(0)
combo_1.place(x=300,y=195)

combo_2=Combobox(root)
combo_2['values']=('1995','1996','1997','1998','1999','2000','2001','2002','2003','2004')
combo_2.current(0)
combo_2.place(x=380,y=195)

Label(text= "Gender", width=14, fg='yellow', bg='black', font='arial 10').place(x=17, y=250)
Radiobutton(root, text="Male  ", fg='yellow', bg='black', variable=var, value=1).place(x=130, y=250)
Radiobutton(root, text="Female", fg='yellow', bg='black', variable=var, value=0).place(x=220, y=250)

Label(text= "Country", width=10, fg='yellow', bg='black', font='arial 12').place(x=16, y=300)
combo_3=Combobox(root, width=62)
combo_3['values']=('USA','China','Italy','Russia')
combo_3.current(0)
combo_3.place(x=130,y=300)

Label(text="E-mail",width=10,fg='yellow',bg='black',font='arial 10').place(x=22,y=360)
Entry(text="Enter E-mail", width=30,fg='yellow',font='arial 18').place(x=130,y=355)

Label(text="Phone", width=10,fg='yellow',bg='black',font='arial 14').place(x=13,y=405)
Entry(text="Enter Phone", width=30, font='arial 18').place(x=130,y=400)

Label(text="Password", width=14,fg='yellow',bg='black',font='arial 8').place(x=17,y=450)
Entry(width=30, font='arial 18').place(x=130,y=450)

Label(text="Confirm Password", width=14,fg='yellow',bg='black',font='arial 8').place(x=17,y=500)
Entry(width=30, font='arial 18').place(x=130,y=500)

Checkbutton(root,text=u'I agree to the Terms of Use', fg='yellow', bg='black', variable=var1, onvalue=1, offvalue=0).place(x=200,y=550)


Canvas(root, bg='orange', height=70, width=665).place(x=1,y=600)
Button(text="submit",width=5,height=1,bg='green',fg='white',font='arial 10').place(x=450,y=620)
Button(text="Cancel",width=5,height=1,bg='red',fg='white',font='arial 10').place(x=500,y=620)

root.mainloop()
