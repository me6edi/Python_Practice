class Person:
    def __init___(self, name):
        self.name = name


    def __str__(self):
        return f'{self.__class__.__name__} class, obj name:
        {self.name}

p1 = Person("Bill")
p2 = Person("Steve")


print(p1)
print(p2)
