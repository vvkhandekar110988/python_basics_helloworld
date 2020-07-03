class Mammel:
    def walk(self):
        print("Walk")


class Dog(Mammel):
    def bark(self):
        print("bark")


class Cat(Mammel):
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()
