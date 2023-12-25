class Supermarket:
    def __init__(self, department_name, product_name, country, price, supplier):
        self.department_name = department_name
        self.product_name = product_name
        self.country = country
        self.price = price
        self.supplier = supplier

    def __str__(self):
        return f"Отдел: {self.department_name}, Товар: {self.product_name}, Страна-производитель: {self.country}, Цена: {self.price}, Поставщик: {self.supplier}"

class Toys(Supermarket):
    def __init__(self, department_name, product_name, country, price, supplier, age_group, type):
        super().__init__(department_name, product_name, country, price, supplier)
        self.age_group = age_group
        self.type = type

    def __str__(self):
        return super().__str__() + f", Возрастная группа: {self.age_group}, Тип: {self.type}"

class Fruits(Supermarket):
    def __init__(self, department_name, product_name, country, price, supplier, max_storage_time, storage_temperature):
        super().__init__(department_name, product_name, country, price, supplier)
        self.max_storage_time = max_storage_time
        self.storage_temperature = storage_temperature

    def __str__(self):
        return super().__str__() + f", Максимальное время хранения: {self.max_storage_time}, Температура хранения: {self.storage_temperature}"

class BulkyGoods(Supermarket):
    def __init__(self, department_name, product_name, country, price, supplier, height, width, length):
        super().__init__(department_name, product_name, country, price, supplier)
        self.height = height
        self.width = width
        self.length = length

    def __str__(self):
        return super().__str__() + f", Высота: {self.height}, Ширина: {self.width}, Длина: {self.length}"

# Пример использования
toy = Toys("Игрушки", "Мягкая игрушка", "Россия", 1500, "ООО Игрушки", "3+", "мягкая игрушка")
fruit = Fruits("Фрукты", "Яблоки", "Беларусь", 3000, "ООО Фрукты", "7 дней", "+1-+4")
bulky_good = BulkyGoods("Габаритный товар", "Шкаф", "Беларусь", 75000, "ООО Мебель", 200, 80, 50)

print(toy)
print(fruit)
print(bulky_good)
