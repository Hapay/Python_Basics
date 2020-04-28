# Po utworzeniu klasy dodajemy w nawiasie przy tworzeniu klase, z ktorej ma ona dziedzyczyc. W tym przypadku
# jest to klasa "mammal", z ktorej jest dziedziczone.
# Mozemy nawet po dziedziczeniu dodawac osobne funkcje, argumenty do danych klas.
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("barking")

class Cat(Mammal):
    def be_annoying(self):
        print("I am being annying...")


mammal = Mammal()
mammal.walk()
dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.be_annoying()
