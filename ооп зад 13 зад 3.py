import tkinter as tk
from random import randint
def roll():#функция броска кубиков
    number = randint(1, 6)#случайное числа от 1 до 6
    label.config(text=str(number))#вывод цифры которую сгенерировали
    #создание окна его тутильного названия и размеров
window = tk.Tk()
window.title('метай')
window.geometry('300x50')
label = tk.Label(window, text='крути')#создание метки
label.pack()
button = tk.Button(window, text='верти', command=roll)# кнопка с командой по клику
button.pack()
window.mainloop()#вызов окна