import random

for i in range(2):
    print(random.random())
print(random.randint(0, 1000))

members = ["John", 'Patryk', 'Gabi', 'Dorothy']
leader = random.choice(members)
print(leader)


#ZADANIE Rzucam kostka. Mam stworzyc klase, ktora ma fukcje roll
# Ta funkcja ma wyswietlac "tuples" np (4,2)

class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1,6)
        rolled = (a,b)
        return rolled

dice = Dice()
print(dice.roll())