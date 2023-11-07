class Quadrilateral:#создание класса четырёхуголькик
    def __init__(self, width, height=None):#инициализация сторон
        self.width=width
        self.height=height if height is not None \
            else width#в случае если высота не введена, она будет принята такой же как и ширина
    def __str__(self):
        if self.width==self.height:
            return (f'Куб размером {self.width}х{self.height}')#если высота равна ширине возвращает 'куб размером и произведение сторон'
        else:
            return (f'Прямоугольник размером {self.width}х{self.height}')#если высота не равна ширине возвращает
            # 'прямоугольник размером и аналогично как и выше'

    def __bool__(self):
        return self.width==self.height#если ширина равна высоте, вывод True, иначе False
    #проверка работостпособности по примеру
q1=Quadrilateral(10)
print(q1)
print(bool(q1))
q2=Quadrilateral(3, 5)
print(q2)
print(q2==True)