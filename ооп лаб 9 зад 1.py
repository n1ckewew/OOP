class Rectangle:
    def __init__(self, a, b):#инициализация сторон
        self.a=a
        self.b=b
    def get_area(self):#ф поиска площади
        return self.a*self.b
class Square:#создание класса квадрат
    def __init__(self, a):#инициализация стороны
        self.a=a
    def get_area(self):#функция поиска площади
        return self.a**2
class Circle:#создание класса круг
    def __init__(self, r):#инициализация радиуса
        self.r=r
    def get_area(self):#функция поиска площади
        return 3.14*self.r**2
    #создание экземпляров класса
rect1=Rectangle(3, 4)
rect2=Rectangle(12, 3)
sq1=Square(2)
cirl=Circle(3)
figure=[rect1, rect2, sq1, cirl]
#вывод для всех фигур их площади путём вызова общей функции
for figure in figure:
    print(figure.get_area())