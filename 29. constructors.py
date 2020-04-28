# Mozmy tworzyc "punkt" bez tworzenia wspolrzednych x i y, a to nie mialoby sensu, poniewaz punkt zawsze musi miec
# te wspolrzedne, bo inaczej taki punkt jest po nic
# Do tego uzywamy "constructorow". W tym przypaku "init". Tworzymy kolejna funkje w klaie "point"
# Init uzywane jest do definiowania atrybutow, czyli np imienia, wieku, wszystkiego...

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# Dodajac "init" i podajac tej funkcji wspolrzedne x i y bedzemy mogli podac wspolrzednego punktowi, jak pokazane na dole
point = Point(10, 20)
print(point.x)


#ZADANIE Stworzyc klase "osoba". Ma ona miec funkcje "mowienia" i "imie"
class Person:
    def __init__(self, name, age, is_pretty):
        self.name = name
        self.age = age
        self.is_pretty = is_pretty
    def desc(self):
        print(f"Hi, I am {self.name}, i am {self.age} y/o and i'm {self.is_pretty} ")


patryk = Person("Patryk", 22, "pretty :)")
patryk.desc()

bob = Person("Bob", 14, "ugly :(")
bob.desc()
