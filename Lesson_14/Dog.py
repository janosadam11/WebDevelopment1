from Lesson_14.Animal import Animal


class Dog(Animal):
    def __init__(self, name, age, paw, comm):
        super().__init__(name, age) #Itt hivjuk meg az ősosztalyt
        self.paw = paw
        self.comm = comm

    def communicate(self):
        print("Wuff")