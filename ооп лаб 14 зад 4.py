from tkinter import *
from tkinter import ttk
import math
# Определение функции для табулирования заданной функции
def tabulate_function():
    listbox.delete(0, END)  # Очистка списка
    step = 0.01  # Шаг
    beginning = 0.01  # Начальное значение аргумента
    end = 0.9  # Конечное значение аргумента
    iterations = int((end - beginning) / step) + 1  # Вычисление кол-ва итераций
    label_function_formula.config(text=' y=1+exp(2*x-1)')  # Обновление метки для отображения формулы
    listbox.insert(END, '    x            |            y')  # Вставка заголовка в список
    # Настройка полосы прогресса
    progress['maximum'] = iterations  # Максимальное значение прогресс-бара
    progress['value'] = 0  # Начальное значение прогресс-бара
    for i in range(iterations):
        x = beginning + i * step  # Вычисление значения аргумента
        y = y=1+math.exp(2*x-1)  # Вычисление значения функции
        result = f'   {x:.2f}              {y:.2f}'  # Форматирование результата
        listbox.insert(END, result)  # Всталяем результат в список
        progress['value'] = i + 1  # Обновляем значения прогресс шкалы
        window.update()  # Обновление окна для отображения прогресса
# Создание окна
window = Tk()
window.title('Табулирование функции')
# Метка для отображения формулы функции
label_function_formula = Label(window, text=' y=1+exp(2*x-1)', font=('Arial', 12))
label_function_formula.pack()
# Создание списка для отображения табелированных значений
listbox = Listbox(window, width=30)
listbox.pack()
# Создание полосы прогресса
progress = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
progress.pack()
# Создание кнопки для запуска
btn_tabulate = Button(window, text='Табулировать', command=tabulate_function)
btn_tabulate.pack()
window.mainloop()