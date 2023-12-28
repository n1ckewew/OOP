from tkinter import *
from tkinter import messagebox
def clicked():#функция по выводу сообщения
    messagebox.showinfo('мяу', 'победа!')
def close_window():#функция по закрытию окна
    window.destroy()
    #создание окна его размеров и титульного названия
window=Tk()
window.title('гримпотевтис ')
window.geometry('400x100')
# Изменяем цвет и размер шрифта для метки
lab=Label(window, text='Первые успехи!', font=('Arial', 18), fg='blue')
lab.grid(column=1, row=0)
#создание кнопки, её положение и комадда по выводу сообщения
btn1=Button(window, text='приветствие', font=('Arial', 14), command=clicked)
btn1.grid(column=0, row=1)
#создание кнопки, её расположения и команды по закрытию окна
btn2=Button(window, text='закрыть', font=('Arial', 14), command=close_window)
btn2.grid(column=2, row=1)
window.mainloop()