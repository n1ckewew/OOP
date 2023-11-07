class Vector:
    def __init__(self, *args):
        self.values=[]
        #если аргумент целое число, добавляем его в список и сортируем
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)
            self.values.sort()
            #проверка, если список пустой(вывод пустой вектор), иначе добавление в список
    def __str__(self):
        if len(self.values)==0:
            return 'пустой вектор '
        return f'вектор{tuple(self.values)}'
#функция по сложению
    def __add__(self, other):
        new_v=[]#создание списка для хранения значений вектора
        if isinstance(other, Vector):#проверка other на объект класса вектор
            if len(self.values) == len(other.values):#проверка равные ли у векторов длины
                for i in range(len(self.values)):#перебор элементов векторов
                    new_v.append(self.values[i] + other.values[i])#сложение элементов векторов
                return Vector(*[i for i in new_v])#возвращает только что созданный вектор после сложения
            else:# в противном случае вывод
                print('сложение разных векторов недопустимо')
        if isinstance(other, int):#проверка на целое число other
            for i in range(len(self.values)):#перебор элементов вектора
                new_v.append(self.values[i] + other)
            return Vector(*[i for i in new_v])#сложение каждого элемента с other
        if not isinstance(other, (Vector, int)):#если на целое, то вывод
            print(f'Вектор нельзя сложить с {other}')
            #аналогично как и со сложением, только здесь умножение
    def __mul__(self, other):
        new_v=[]
        if isinstance(other, Vector):
            if len(self.values)==len(other.values):
                for i in range(len(self.values)):
                    new_v.append(self.values[i]*other.values[i])
                return Vector(*[i for i in new_v])
            else:
                print('сложение разных векторов недопустимо')
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_v.append(self.values[i]*other)
            return Vector(*[i for i in new_v])
        if not isinstance(other, (Vector, int)):
            print(f'Вектор нельзя сложить с {other}')
                #проверка работоспособности
v1 = Vector(1,2,3)#1 объект класса
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)#2 объект класса
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2#3 объект класса
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5#4 объект класса
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2#5 объект класс
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"