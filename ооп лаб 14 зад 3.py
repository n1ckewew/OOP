from tkinter import *  # Импортируем все из модуля tkinter
from tkinter import ttk  # Импортируем модуль ttk, который содержит тематические виджеты
window = Tk()  # Создаем окно
window.geometry('300x400')  # Устанавливаем размер окна
value_var = IntVar()  # Создаем переменную целого типа для отслеживания прогресса
# Создаем горизонтальный прогресс-бар длиной 280 пикселей, связанный с переменной value_var
pb = ttk.Progressbar(window, orient='vertical', length=280, mode='determinate', variable=value_var)
pb.pack(pady=5)
def start():
    pb.start(40)  # Функция для запуска прогресс-бара
def stop():
    pb.stop()  # Функция для остановки прогресс-бара
# Создаем кнопку "Start", которая при нажатии вызывает функцию start
start_btn = ttk.Button(window, text='Start', command=start)
start_btn.pack()  # Размещаем кнопку "Start" в окне
# Создаем кнопку "Stop", которая при нажатии вызывает функцию stop
stop_btn = ttk.Button(window, text='Stop', command=stop)
stop_btn.pack()  # Размещаем кнопку "Stop" в окне
window.mainloop()  # Вызов окна