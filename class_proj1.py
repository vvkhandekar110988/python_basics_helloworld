class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name }")


vishal = Person("Vishal Khandekar")
# print(.name)
vishal.talk()

tushar = Person("Tushar Khandekar")
tushar.talk()
