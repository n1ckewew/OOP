from tkinter import *  # Импортируем все из модуля tkinter
window = Tk()  # Создаем окно
window.geometry('250x200')  # Устанавливаем размер окна
# Создаем первый Listbox с высотой 5 строк, шириной 15 символов и возможностью выбора нескольких элементов
list1 = Listbox(window, height = 5, width = 15, selectmode = EXTENDED)
# Создаем второй Listbox с высотой 5 строк, шириной 15 символов и возможностью выбора только одного элемента
list2 = Listbox(window, height = 5, width = 15, selectmode = SINGLE)
# Создаем два списка городов
lst1 = ['Минск', 'Молодечно', 'Борисов', 'Жодино', 'Воложин']
lst2 = ['Гродно', 'Ивье', 'Новогрудок', 'Ошмяны', 'Островец']
# Заполняем первый Listbox городами из первого списка
for i in lst1:
    list1.insert(END, i)
# Заполняем второй Listbox городами из второго списка
for i in lst2:
    list2.insert(END, i)
# Размещаем Listbox'ы в окне с помощью менеджера геометрии pack
list1.pack()
list2.pack()
window.mainloop()  # Вызов окна