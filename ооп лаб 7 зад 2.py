class A:
    def __init__(self, a, b):
        self.a=a
        self.b = b
    @property
    def c(self):
        return self.a**2 + 4*self.b
obj=A(2, 3)
print(obj.c)
