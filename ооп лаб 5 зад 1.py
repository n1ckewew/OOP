class C:
    def __init__(self, a, b=5):
        self.a=a
        self.b=a

    def c(self):
        return self.a+self.b

    def d(self):
        return self.a-self.b

a1=C(5)
print(f'{a1.a}+{a1.b}={a1.c()}')
a2=C(4,6)
print(f'{a2.a}-{a2.b}={a2.d()}')