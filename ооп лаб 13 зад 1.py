from tkinter import *
def close_window():#создаём функцию по закрытию окна
    window.destroy()
window=Tk()#создание окна
window.title('проект 1')#задание названия титулу
window.geometry('400x100')#и его размеров
lab=Label(window, text='моя первая программа', font=('Arial', 14))#создание метки
lab.pack()
btn=Button(window, text='закрыть', font=('Arial', 14), command=close_window)#создайм кнопочку, которая выполнит команду по нажатию
btn.pack()
window.mainloop()#вызов окна