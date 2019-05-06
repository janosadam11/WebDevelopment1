class Animal:
    count = []


    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count.append(name)

    def get_number_of_animals(self):
        return len(self.count)

class Dog(Animal):
    def __init__(self, name, age, paw):
        super().__init__(name, age) #Itt hivjuk meg az ősosztalyt
        self.paw = paw

    def communicate(self):
        print("Wuff")

class Fish(Animal):
    def __init__(self, fin, swim):
        self.fin = fin
        self.swim = swim

a = Animal("Bello", 12)
b = Animal("Goofy", 14)


c = Dog("Bob", 4, 5)
c.communicate()

print(a.get_number_of_animals())