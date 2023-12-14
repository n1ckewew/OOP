class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}'

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        return super().__str__() + f', Университет: {self.university}'

class Father(Person):
    def __init__(self, name, age, children=2):
        super().__init__(name, age)
        self.children = children

    def __str__(self):
        return super().__str__() + f', Дети: {self.children}'

class StudentFather(Student, Father):
    def __init__(self, name, age, university, children):
        Student.__init__(self, name, age, university)
        Father.__init__(self, name, age, children)

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Университет: {self.university}, Дети: {self.children}'

# Создание экземпляров классов
person = Person("Иван", 30)
student = Student("Анна", 20, "МГУ")
father = Father("Сергей", 40, ["Анна", "Мария"])
student_father = StudentFather("Алексей", 35, "МГТУ", ["Иван", "Мария"])

# Вывод информации об экземплярах классов
print(person)
print(student)
print(father)
print(student_father)
