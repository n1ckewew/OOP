class Firm:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class Department:
    def __init__(self, name, num_employees):
        self._name = name
        self._num_employees = num_employees

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def num_employees(self):
        return self._num_employees

    @num_employees.setter
    def num_employees(self, value):
        self._num_employees = value

class Employee:
    def __init__(self, name, position, salary):
        self._name = name
        self._position = position
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def calculate_salary(self):
        return self._salary

class RegularEmployee(Employee):
    def __init__(self, name, position, salary, bonus):
        super().__init__(name, position, salary)
        self._bonus = bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if value < 0:
            raise ValueError("Премия не может быть отрицательной")
        self._bonus = value

    def calculate_salary(self):
        try:
            return self._salary + self._bonus
        except Exception as e:
            print(f"Ошибка при расчете зарплаты: {e}")

class ContractEmployee(Employee):
    def calculate_salary(self):
        try:
            return self._salary
        except Exception as e:
            print(f"Ошибка при расчете зарплаты: {e}")
            # Создание экземпляров классов
firm = Firm("ООО 'Рога и копыта'")
department = Department("Отдел продаж", 10)
regular_employee = RegularEmployee("Иванов Иван", "менеджер", 50000, 10000)
contract_employee = ContractEmployee("Петров Петр", "консультант", 30000)

            # Вывод информации о фирме, отделе и сотрудниках
print(f"Фирма: {firm.name}")
print(f"Отдел: {department.name}, количество сотрудников: {department.num_employees}")
print(f"Штатный сотрудник: {regular_employee.name}, должность: {regular_employee.position}, зарплата: {regular_employee.calculate_salary()}")
print(f"Сотрудник по контракту: {contract_employee.name}, должность: {contract_employee.position}, зарплата: {contract_employee.calculate_salary()}")

