# создаем класса Student
class Student:
    def __init__(self,name, group, numbers):
        self.name=name
        self.group=group
        self.numbers=numbers
    def ball(self):
        return sum(self.numbers)/len(self.numbers)
    def info(self):
        print(f'Студент  {self.name}')
        print(f'Номер группы  {self.group}')
        print(f'Успеваемость  {", ".join(map(str, self.numbers))}')
        print(f'Средний балл  {self.ball()}\n')
students=[]
#ввод информации о студентах
for i in range(5):
    name=input('Введите фамилию и имя студента ')
    group=input('Введите номер группы ')
    numbers=[int(numbers) for numbers in input('Введите пять оценок через пробел ').split()]
    student=Student(name, group, numbers)
    students.append(student)
print('Информация о студентах ')
for student in students:
    student.info()
    #ввод информации о студентах
sortirovka=sorted(students, key=lambda x: x.ball())
print('Список студентов по возрастанию ср балла ')
for student in sortirovka:
    student.info()