class Bird:
    def __init__(self, name, mass, wingspan, habitat, food):
        self.__name=name
        self.__mass=mass
        self.__wingspan=wingspan
        self.__habitat=habitat
        self.__food=food

    @property
    def name(self):
        return self.__name

    @property
    def mass(self):
        return self.__mass

    @property
    def wingspan(self):
        return self.__wingspan

    @property
    def habitat(self):
        return self.__habitat

    @property
    def food(self):
        return self.__food

bird = Bird("Eagle", 5.2, 200, "Mountains", "Small animals")
print(bird.name)          # Output: Eagle
print(bird.mass)        # Output: 5.2
print(bird.wingspan)      # Output: 200
print(bird.habitat)       # Output: Mountains
print(bird.food)          # Output: Small animals
