class Student: # Определение класса Student
    class Counter: # Определение вложенного класса Counter
        def __init__(self): # Метод инициализации объекта класса Counter
            self.value = 0  # Инициализация переменной value значением 0
        def start_from(self, value=0):   # Метод устанавливающий начальное значение счетчика
            self.value = value   # Метод устанавливающий начальное значение счетчика
        def increment(self): # Метод увеличивающий значение счетчика на 1
            self.value += 1 # Увеличение значения переменной value на 1
        def display(self): # Метод вывода текущего значения счетчика
            print(f"Текущее значение счетчика = {self.value}")  # Вывод текущего значения переменной value
        def reset(self): # Метод сброса значения счетчика на 0
            self.value = 0 # Установка значения переменной value равным 0
    c1 = Counter()
    c1.start_from()
    c1.increment()
    c1.display()  # печатает "Текущее значение счетчика = 1"
    c1.increment()
    c1.display()  # печатает "Текущее значение счетчика = 2"
    c1.reset()
    c1.display()  # печатает "Текущее значение счетчика = 0"
    c2 = Counter()
    c2.start_from(3)
    c2.display()  # печатает "Текущее значение счетчика = 3"
    c2.increment()
    c2.display()  # печатает "Текущее значение счетчика = 4"
