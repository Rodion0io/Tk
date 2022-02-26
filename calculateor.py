from tkinter import *



#Функции

def number_button(num):
    text1.insert(END, str(num))

def clear1():
    text1.delete(0,END)

def clear2():
    n = text1.get()
    text1.delete(len(n)-1)

def ravno():
    s = text1.get()
    try:
        result = eval(s)
        clear1()
        text1.insert(0,result)
    except EXCEPTION:
        clear1()
        text1.insert(0,"Error")

root =Tk()
root.title('Калькулятор')

# Создание Фреймов
root.resizable(0,0)

frame1 = Frame(root)
frame1.pack(side = TOP, pady = 5)

frame2 = Frame(root)
frame2.pack(side=LEFT,anchor=N, pady=5, padx=5)

text1 = Entry(frame1, font = 'Arial 30', justify = 'right', bd = 20, insertwidth = -1)
text1.pack(side = RIGHT, anchor = N)

# 1 ряд
b_7 = Button(frame2, text = '7', width = 3, bd = 8, fg = 'black', font = 'Arial 30',command = lambda: number_button(7))
b_7.grid(row = 1, column = 1)
b_8 = Button(frame2,text = '8', width = 3, bd = 8, fg = 'black', font = 'Arial 30', command = lambda: number_button(8))
b_8.grid(row = 1,column = 2)
b_9 = Button(frame2, text = '9', width = 3, bd = 8, fg = 'black', font = 'Arial 30', command = lambda: number_button(9))
b_9.grid(row = 1, column = 3)
b_d = Button(frame2, text='/', width=3, bd=8, fg="red", font='Arial 30',command = lambda : number_button('/'))
b_d.grid(row = 1, column = 4)
b_c = Button(frame2, text = 'C', width = 4, bd = 8, fg = 'red', font = 'Arial 30', command = clear1)
b_c.grid(row = 1, column = 5)

# 2 ряд
b_4 = Button(frame2, text = '4', width = 3, bd = 8, fg = 'black',font = 'Arial 30', command =lambda: number_button(4))
b_4.grid(row = 2, column = 1)
b_5 = Button(frame2, text = '5', width = 3, bd = 8, fg = 'black',font = 'Arial 30', command =lambda: number_button(5))
b_5.grid(row = 2, column = 2)
b_6 = Button(frame2, text = '6', width = 3, bd = 8, fg = 'black',font = 'Arial 30', command =lambda: number_button(6))
b_6.grid(row = 2, column = 3)
b_u = Button(frame2, text='*', width=3, bd=8, fg="red",font='Arial 30',command = lambda : number_button('*'))
b_u.grid(row = 2, column = 4)
b_CE = Button(frame2, text='CE', width=4, bd=8, fg="red",font='Arial 30', command = clear2)
b_CE.grid(row = 2, column = 5)

# 3 ряд
b_1 = Button(frame2, text='1', width=3, bd=8, fg="black",font='Arial 30',command = lambda : number_button('1'))
b_1.grid(row = 3, column = 1)
b_2 = Button(frame2, text='2', width=3, bd=8, fg="black",font='Arial 30',command = lambda : number_button('2'))
b_2.grid(row = 3, column = 2)
b_3 = Button(frame2, text='3', width=3, bd=8, fg="black",font='Arial 30',command = lambda : number_button('3'))
b_3.grid(row = 3, column = 3)
b_m = Button(frame2, text='-', width=3, bd=8, fg="red",font='Arial 30',command = lambda : number_button('-'))
b_m.grid(row = 3, column = 4)
b_r = Button(frame2, text='=', width=4, bd=8, fg="blue",font='Arial 30', height=3, command = ravno )
b_r.grid(row =3, column = 5, rowspan=2)

# 4 ряд
b_0 = Button(frame2, text='0', width=8, bd=8, fg="black",font='Arial 30',command = lambda : number_button('0'))
b_0.grid(row = 4, column = 1, columnspan = 2)
b_z = Button(frame2, text=',', width=3, bd=8, fg="black",font='Arial 30',command = lambda : number_button('.'))
b_z.grid(row = 4, column = 3)
b_p = Button(frame2, text='+', width=3, bd=8, fg="red",font='Arial 30',command = lambda : number_button('+'))
b_p.grid(row = 4, column = 4)

root.mainloop()